from flask import Flask, render_template, url_for, request, session, redirect, jsonify, flash
from flask_bootstrap import Bootstrap
from datetime import datetime
import json

# Init processes
app = Flask(__name__)
Bootstrap(app)

# Route to index page
@app.route('/')
def index():
	return render_template('index.html')

# Route to Resources page page
@app.route('/resources')
def resources():
	return render_template('resources.html')

# Route to main Forum page
@app.route('/forum')
def forum():
	return render_template('forum.html')

# Route to main Forum page
@app.route('/create-post')
def post():
	return render_template('create-post.html')


if __name__ == '__main__':
	app.run('localhost', 8080, debug=True)