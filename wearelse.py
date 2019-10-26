from flask import Flask, render_template, url_for, request
import random
import requests
import configparser
import json
from apis import getNordstromResults, getEtsyResults

app = Flask(__name__)


@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/handle_data', methods=['GET'])
def handle_data():
	# print(request.args['query'])
    #projectpath = request.form['projectFilepath']
	print(request.args.get('query'))
	nordstromResults = json.loads(getNordstromResults(request.args.get('query')))
	etsyResults = json.loads(getEtsyResults(request.args.get('query')))

	total = nordstromResults["results"] + etsyResults["results"]
	return str(total)
'''
Items list has JSON object of 
img, title, price for each item.
'''
@app.route('/results')
def query(items_list=None):
	print(url_for('static', filename='main.css'))
	return render_template('hello.html', items=items_list, main_css=url_for('static', filename='main.css'))
