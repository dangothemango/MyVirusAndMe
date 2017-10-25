from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

vars = {}

@app.route('/')
def login():
    return render_template('login.html',vars = vars)

@app.route('/', methods = ['POST'])
def loginPost():
	if (request.form['username'] == "admin" and request.form['password'] == 'password'):
		return redirect(url_for('key'))
	else:
		return render_template('login.html',error = "Invalid username or password")

@app.route('/key')
def key():
	return render_template('key.html',vars = vars)

@app.route('/key', methods = ['POST'])
def keyPost():
	if (request.form['key'].lower()=="andhereiswhereitallbegins"):
		return "Insert Key Here"

	else:
		return render_template('key.html',vars = vars)
