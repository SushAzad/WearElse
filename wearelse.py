from flask import Flask, render_template, url_for
import requests
import configparser
import json

app = Flask(__name__)

# @app.route('/')
# def hello_word():
# 	return 'Hello, World!'

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

def getEbayResults(query):
	URL = "https://openapi.etsy.com/v2/listings/active"

	parser = configparser.ConfigParser()
	try:
		parser.read('config.ini')
		PARAMS = {"api_key": parser.get('ebay_api', 'api_key'),
	#PARAMS = {"api_key": "xhshosdpo1y0alvwy572r4gc",
			"keywords": query,
			"category": "Clothing",
			"limit": 5}
		r = requests.get(url = URL, params = PARAMS)

		data = r.json()
		print(data)
		res = []
		for d in data['results']:
			URL2 = "https://openapi.etsy.com/v2/listings/" + str(d['listing_id']) + "/images"
			PARAMS2 = {"api_key": "xhshosdpo1y0alvwy572r4gc"}
			r2 = requests.get(url = URL2, params = PARAMS2)
			data2 = r2.json()
			
			print(d['title'])
			print(d['description'])
			print(d['price'])
			print(d['url'])
			print(data2['results'][0]['url_570xN'])

			res.append({"title": d['title'],
				"description": d['description'],
				"price": d['price'],
				"link": d['url'],
				"img_url": data2['results'][0]['url_570xN']})

		return json.dumps({"results": res})
	except:
		print("ERROR: config.ini not created or request is bad")


'''
Items list has JSON object of 
img, title, price for each item.
'''
@app.route('/results')
def query(items_list=None):
	print(url_for('static', filename='main.css'))
	return render_template('hello.html', items=items_list, main_css=url_for('static', filename='main.css'))
