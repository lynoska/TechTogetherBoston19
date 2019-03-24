from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
import json
import pyrebase
import config

# Init processes
app = Flask(__name__)
Bootstrap(app)

# Temporarily replace quote function
def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote


firebase = pyrebase.initialize_app({
	"apiKey" : config.apiKey,
	"authDomain" : config.authDomain,
	"databaseURL" : config.databaseURL,
	"storageBucket" : config.storageBucket,
	})

db = firebase.database()

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
	return render_template('forum.html', posts=posts)

# Route to main Forum page
@app.route('/create-post', methods=['GET'])
def post():
	return render_template('create-post.html')

# Route to submit form
@app.route('/submit-forum', methods=['POST'])
def submit_forum():
	data = request.form
	
	# Since firebase doesn't have a counter, we have to make one of our own
	# By getting the last post we have a dictionary with the last post # used
	post = db.child("post").order_by_child("post_id").limit_to_last(1).get().val()
	
	# Cleaning up the brackets from the list. Changes the dict to list
	data = {k.strip("[\"\'"): v.strip("[\"\'") for k, v in data.items()}
	data = {k.strip("]\"\'"): v.strip("]\"\'") for k, v in data.items()}
	
	# Increases the count 
	data['post_id'] = list(post.values())[0]['post_id'] + 1
	db.child("post").push(data)

	return redirect(url_for('forum'))

@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404

if __name__ == '__main__':
	app.run('localhost', 8080, debug=True)