from flask import Flask
app = Flask('hotline')

@app.route('/')
def hello_world():
	return 'hello world!'
