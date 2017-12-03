from flask import Flask, render_template, url_for, request, redirect, session
from flask.json import JSONEncoder,JSONDecoder

import json, time
import os.path

#Ideally this will be moved into another file but i dont feel like figuring that out now
userDatabase= "./data/users/"

class User(object):

	def __init__(self, arg,json = False):
		super(User, self).__init__()
		self.name = arg
		self.password = ""
		self.score = 0
		self.eggScore = 0;
		if (json):
			self.fromJson(arg)
		else:
			self.load(arg)

	def fromJson(self,jsonString):
		userDict=json.loads(jsonString)
		self.name=userDict['name']
		self.password=userDict['password']
		self.score=userDict['score']
		self.eggScore=userDict['eggScore']

	def load(self,uname):
		with open(userDatabase+uname+'.json') as userF:
			userDict = json.load(userF)
		if (userDict['name'] != self.name):
			exit(-1)
		self.password=userDict['password']
		self.score=userDict['score']
		self.eggScore=userDict['eggScore']

	def toJson(self):
		userDict={'name':self.name, 'password':self.password,'score':self.score, 'eggScore':self.eggScore}
		return json.dumps(userDict)

	def save(self):
		userDict={'name':self.name, 'password':self.password,'score':self.score, 'eggScore':self.eggScore}
		with open(userDatabase+self.name+'.json','w') as userF:
			json.dump(userDict,userF)
		
	def checkPassword(self,password):
		return password==self.password

	@staticmethod
	def validateName(uname):
		for char in uname:
			if char in specialCharacters:
				return False
		return True

	@staticmethod
	def exists(uname):
		return os.path.isfile(userDatabase+uname+'.json')

	@staticmethod
	def newUser(name, password):
		newUser={}
		newUser['name']=name
		newUser['password']=password
		newUser['score']=0
		newUser['eggScore']=0
		user = User(json.dumps(newUser),True)
		user.save()
		return user

leaderboardFile= "./data/leaderboard/leaderboard.json"

class Leaderboard(object):

	def __init__(self):
		super(Leaderboard, self).__init__()
		self.levels = []
		self.eggLevels = []
		self.load()

	def load(self):
		with open(leaderboardFile) as f:
			leaderboard = json.load(f)
		self.levels = leaderboard['levels']
		self.eggLevels = leaderboard['eggLevels']

	def save(self):
		leaderboard={'levels':self.levels, 'eggLevels':self.eggLevels}
		with open(leaderboardFile,'w') as f:
			json.dump(leaderboard,f)

	def onSuccess(self, level, levelName,uname):
		if (level>=0):
			if (level == len(self.levels)):
				self.levels.append([levelName,1,uname,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
			else:
				self.levels[level][1]+=1
		else:
			level = level*-1
			if (level > len(self.eggLevels)):
				self.eggLevels.append([levelName,1,uname,time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
			else:
				self.eggLevels[level-1][1]+=1
		self.save()

	def getLeaderboard(self):
		return list(reversed(self.levels))+self.eggLevels


app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R8XHH!jmN]LWX/,?RT'

class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return obj.toJson()
        else:
            JSONEncoder.default(self, obj)

# Now tell Flask to use the custom class
app.json_encoder = CustomJSONEncoder

vars = {}
specialCharacters ="~#%&*{}\\:<>?/+|\""

with open('./data/PlaytestKeys.json') as f:
	keysDict = json.load(f)

leaderboard = Leaderboard()

@app.route('/')
def login():
	return render_template('login.html')

@app.route('/', methods = ['POST'])
def loginPost():
	if 'signup' in request.form:
		if (len(request.form['username']) == 0 or len(request.form['password']) ==0):
			return render_template('login.html', error="Username and password must be specified")
		if not User.validateName(request.form['username']):
			return render_template('login.html',error = "username may not contain "+specialCharacters)
		if User.exists(request.form['username']):
			return render_template('login.html',error = "Username is already taken")
		session['user']=User.newUser(request.form['username'],request.form['password'])
		return redirect(url_for('key'))
		
	if 'login' in request.form:
		user = request.form['username']
		if not User.validateName(user):
			return render_template('login.html',error = "username may not contain "+specialCharacters)

		if not User.exists(user):
			return render_template('login.html',error = "Invalid username or password")
		
		user = User(user)
		if (request.form['password'] == user.password):
			session['user'] = user
			return redirect(url_for('key'))
		else:
			return render_template('login.html',error ="Invalid username or password")
	

@app.route('/key')
def key():
	if not ('user' in session):
		return redirect(url_for('login'))
	return render_template('key.html',leaderboard = leaderboard.getLeaderboard())

@app.route('/key', methods = ['POST'])
def keyPost():
	if not ('user' in session):
		return redirect(url_for('login'))
	if request.form['key'].lower() in keysDict:
		u = User(session['user'],json=True)
		k = keysDict[request.form['key'].lower()]

		if(k["level"]<0):
			if u.eggScore > k["level"]+1:
				return render_template('key.html',leaderboard = leaderboard.getLeaderboard())
			if u.eggScore > k["level"]:
				u.eggScore-=1
				u.save()
				session['user']=u

				leaderboard.onSuccess(k['level'], str(k['level']), u.name)	
			return followLevel(leaderboard,k)

		if (u.score<k['level']):
			return render_template('key.html',leaderboard = leaderboard.getLeaderboard())

		if (u.score>k['level']):
			return followLevel(leaderboard,k)

		u.score+=1
		u.save()
		session['user']=u

		##using str(k['level']) as a temp place holder for the level name till we think of something better
		leaderboard.onSuccess(k['level'], str(k['level']), u.name)	

		return followLevel(leaderboard,k)

	return render_template('key.html',leaderboard = leaderboard.getLeaderboard())

def followLevel(leaderboard,key):
	if ("redirect" in key and key["redirect"] != None):
		return redirect(url_for(key["redirect"]))
	return render_template('key.html',leaderboard = leaderboard.getLeaderboard(),response=key['response'])

@app.route('/telgraph')
def telgraph():
	if not ('user' in session):
		return redirect(url_for('login'))
	u = User(session['user'],json=True)
	if (u.eggScore > -1):
		return redirect(url_for('key'))
	return render_template('telegraph.html')

@app.route('/codenames')
def codenames():
	if not ('user' in session):
		return redirect(url_for('login'))
	u = User(session['user'],json=True)
	if (u.eggScore > -3):
		return redirect(url_for('key'))
	return render_template('codenames.html')

@app.route('/love')
def love():
	if not ('user' in session):
		return redirect(url_for('login'))
	u = User(session['user'],json=True)
	if (u.eggScore > -5):
		return redirect(url_for('key'))
	return render_template('love.html')

@app.route('/telegraph')
def telegraph():
	if not ('user' in session):
		return redirect(url_for('login'))
	u = User(session['user'],json=True)
	if (u.eggScore > -4):
		return redirect(url_for('key'))
	return render_template('telegraph2.html')

@app.route('/robots.txt')
def robots():
	return app.send_static_file('robots.txt')
