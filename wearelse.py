from flask import Flask,render_template,url_for
app = Flask(__name__)

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
def query(items_list=None):
	print(url_for('static', filename='main.css'))
	return render_template('hello.html', items=items_list, main_css=url_for('static', filename='main.css'))
