from flask import Flask, render_template, url_for, request, redirect
import random
import requests
import configparser
import json
from apis import getNordstromResults, getEtsyResults

app = Flask(__name__)


test = [
	{"title": "Black turtleneck sweater", "description": "100% cotton, from H&M!", "link": "http://google.com", 
    "img_url": "http://jiaqiwu.com/portrait_2019.jpeg", "price": 8.99, "sale_price": 8.99}, 
  {"title": "Purple turtleneck sweater", "description": "100% cotton, from H&M!", "link": "http://google.com", 
    "img_url": "http://jiaqiwu.com/portrait_2019.jpeg", "price": 8.99, "sale_price": 8.99}, 
  {"title": "Pink turtleneck sweater", "description": "100% cotton, from H&M!", "link": "http://google.com", 
    "img_url": "http://jiaqiwu.com/portrait_2019.jpeg", "price": 8.99, "sale_price": 8.99}, 
]


@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)


@app.route('/handle_data', methods=['GET'])
def handle_data():
	# print(request.args['query'])
    #projectpath = request.form['projectFilepath']
	# print(request.args.get('query'))
	nordstromResults = json.loads(getNordstromResults(request.args.get('query')))
	etsyResults = json.loads(getEtsyResults(request.args.get('query')))

	total = nordstromResults["results"] + etsyResults["results"]
	result = json.dumps({"results": total})
	#r = requests.post(url_for('get_search_results'), data = result)
	pretty_query = request.args.get('query')
	pretty_query = pretty_query[1:-1]
	return render_template('results.html', items=total, query=pretty_query)
'''
Items list has JSON object of 
img, title, price for each item.
'''
@app.route('/results', methods=["POST"])
def get_search_results(items_list=None):
	json_dict = request.get_json()
	items_list = json_dict["results"]
	return render_template('results.html', items=items_list)

