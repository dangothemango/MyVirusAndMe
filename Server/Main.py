from flask import Flask, render_template, url_for, request, redirect, session
from flask.json import JSONEncoder,JSONDecoder

import json

#Ideally this will be moved into another file but i dont feel like figuring that out now
userDatabase= "./data/users/"

class User(object):

	def __init__(self, arg,json = False):
		super(User, self).__init__()
		self.name = arg
		self.password = ""
		self.score = 0
		if (json):
			self.fromJson(arg)
		else:
			self.load(arg)

	def fromJson(self,jsonString):
		userDict=json.loads(jsonString)
		self.name=userDict['name']
		self.password=userDict['password']
		self.score=userDict['score']

	def load(self,uname):
		with open(userDatabase+uname+'.json') as userF:
			userDict = json.load(userF)
		if (userDict['name'] != self.name):
			exit(-1)
		self.password=userDict['password']
		self.score=userDict['score']

	def toJson(self):
		userDict={'name':self.name, 'password':self.password,'score':self.score}
		return json.dumps(userDict)

	def save(self):
		userDict={'name':self.name, 'password':self.password,'score':self.score}
		with open(userDatabase+self.name+'.json','w') as userF:
			json.dump(userDict,userF)
		
	def checkPassword(self,password):
		return password==self.password


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
leaderboard = [("1", "6", "Dan"), ("5", "300", "Molly"), ("6", "200", "Harrison")]

with open('./data/keys.json') as f:
	keysDict = json.load(f)

@app.route('/')
def login():
	return render_template('login.html',vars =vars)

@app.route('/', methods = ['POST'])
def loginPost():
	user = request.form['username']
	for char in user:
		if char in specialCharacters:
			return render_template('login.html',error = "username may not contain "+specialCharacters)
	
	user = User(user)
	if (request.form['password'] == user.password):
		session['user'] = user
		return redirect(url_for('key'))
	else:
		return render_template('login.html',error = user.password+request.form['password'])#"Invalid username or password")

@app.route('/key')
def key():
	return render_template('key.html',leaderboard = leaderboard)

@app.route('/key', methods = ['POST'])
def keyPost():
	if request.form['key'].lower() in keysDict:
		u = User(session['user'],json=True)
		u.score +=1
		u.save()
		session['user']=u
		return keysDict[request.form['key'].lower()]

	else:
		return "You Suck"
