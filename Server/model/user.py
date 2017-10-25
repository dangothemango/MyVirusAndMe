import json

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
		