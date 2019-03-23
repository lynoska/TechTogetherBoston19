from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
import json
import pyrebase
import config

# Init processes
app = Flask(__name__)
Bootstrap(app)

firebase = pyrebase.initialize_app({
	"apiKey" : config.apiKey,
	"authDomain" : config.authDomain,
	"databaseURL" : config.databaseURL,
	"storageBucket" : config.storageBucket
	})

db = firebase.database()

# all_user = db.child("post")


# Route to index page
@app.route('/')
def index():
	return render_template('index.html')

# Route to Resources page page
@app.route('/resources')
def resources():
	return render_template('resources.html')

# Route to main Forum page
@app.route('/forum', methods=['GET'])
def forum():
	posts = db.child("post").get().val()
	print(posts)
	return render_template('forum.html', posts=posts)

# Route to main Forum page
@app.route('/create-post', methods=['POST'])
def post():
	return render_template('create-post.html')


if __name__ == '__main__':
	app.run('localhost', 8080, debug=True)