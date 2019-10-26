from flask import Flask,render_template,url_for
app = Flask(__name__)

test = '''
[
	{"title": "Black turtleneck sweater", "description": "100% cotton, from H&M!", "link": "http://google.com", 
    "img_url": "http://jiaqiwu.com/portrait_2019.jpeg", "price": 8.99, "sale_price": 8.99}, 
  {"title": "Purple turtleneck sweater", "description": "100% cotton, from H&M!", "link": "http://google.com", 
    "img_url": "http://jiaqiwu.com/portrait_2019.jpeg", "price": 8.99, "sale_price": 8.99}, 
  {"title": "Pink turtleneck sweater", "description": "100% cotton, from H&M!", "link": "http://google.com", 
    "img_url": "http://jiaqiwu.com/portrait_2019.jpeg", "price": 8.99, "sale_price": 8.99}, 
]
'''

# @app.route('/')
# def hello_word():
# 	return 'Hello, World!'

@app.route('/')
def hello(name=None):
    return render_template('index.html', name=name)

'''
Items list has JSON object of 
img, title, price for each item.
'''
@app.route('/results')
def get_search_results(items_list=None):
	
	return render_template('results.html', items=test)

