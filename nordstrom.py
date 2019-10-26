import requests
import random
import json

def nordstrom(query):
	res = []
	space_escaped = query.replace(" ", "%20") + "/"
	url = "https://shop.nordstrom.com/api/search/"+space_escaped
	querystring = {"top":"72","isMobile":"false","origin":"keywordsearch"}
	headers = {
		'User-Agent': "PostmanRuntime/7.18.0",
		'Accept': "*/*",
		'Cache-Control': "no-cache",
		'Host': "shop.nordstrom.com",
		'Accept-Encoding': "gzip, deflate",
		'Cookie': "bm_sz=FBB9F415370D36157D34441867D23A0B~YAAQJGDcF0F3UghuAQAAJzQKCQX7I5u91biq3mlGiKDaE9BK1Ja+Tmr4jauQPpgnTzBoI9lI5Pko9n/ESMmQIeius9Db/CbjZ6QDBN0yF3KSRa7+oom56mMMnpg6lTPja6AQ5grk8C3YMYMWumHUCul+fTHc5AvPDN5xEBkbjNCFPmA5r7n6AtMny0C21z3CYVmI; _abck=4AF27599045ECF5290CBB943BA16FD9A~-1~YAAQJGDcF0J3UghuAQAAJzQKCQLNm+8EofV+u2XA6MZMHxb/p5WIyoPbB3QUgOr3rqwC8mKqavD1pludDjMnwltzu22fakIX7k/oJPS4QYsI0Pxp8Yg/ibulGyI3nzgAe5kc8rf4hAbxJ7vxqi2v8e0kRRwiXbrcruZuzJZbH0UCr/giaxFhY1FWpkrq6JPcExHKvpxZGg2I2BqBYRV8nK3HVrUUHtLQm5B/55t991R7jxJoyO0gjkhtvWnqHLdRfoxXwb4JoOP8/VIevRTP+rVIiJvTtLOY~-1~-1~-1",
		'Connection': "keep-alive",
		'cache-control': "no-cache"
		}

	response = requests.request("GET", url, headers=headers, params=querystring)
	json_data = json.loads(response.text)
	count = 0
	for key in json_data["productsById"].keys():
		if count >5:
			break
		count +=1
		title = json_data["productsById"][key]["name"]
		print(title)
		price = json_data["productsById"][key]["pricesById"]["original"]["minItemPrice"]
		# print("Original Price: ", price)
	   # sale_price =  json_data["productsById"][key]["pricesById"]["sale"]["minItemPrice"]
		# print("Sale Price: ",sale_price)
		media = json_data["productsById"][key]["mediaById"]
		img_url= ""
		for k in media.keys():
			if media[k]["group"]=="main":
				img_url = media[k]["src"]
				break
		# print("Image URL:",img_url )
		prodPageUrl = "nordstom.com"+str(json_data["productsById"][key]["productPageUrl"])
		# print("Product Page Url: ",prodPageUrl)
		res.append({"title": title,
					"description": query,
					"link": prodPageUrl,
					"img_url": img_url,
					"price": price})
	
	results =  json.dumps({"results":res})
	print(results)
	return results

import requests
def getresults(query):
	URL = "https://query.ecommerce.api.nordstrom.com/api/queryresults/keywordsearch/"


	PARAMS = {"Keyword": query,
		"IncludeFacets": "false",
		"top": 5}
	r = requests.get(url = URL, params = PARAMS, headers={"Origin": "https://shop.nordstrom.com", "Authorization": "apikey 8ea31c48-95c3-4bcf-9db1-d6ada47565f2", "NordApiVersion": "1"})

	data = r.json()
	#print(data['Products'])
	res = []

	for d in data['Products']:
		print(d['Name'])
		print(d['Media'][1]['Path'])
		print(d['Price']['CurrentMinPrice'])
		print(d['PathAlias'])
		print(d['Id'])

getresults("jeans")

# q = "Air Jordan"
# results = nordstrom(q)