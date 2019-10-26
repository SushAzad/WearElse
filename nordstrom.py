import requests
import random
import json

def nordstrom(query):
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
    key = random.choice(list(json_data["productsById"].keys()))
    print("Original Price: ", json_data["productsById"][key]["pricesById"]["original"]["minItemPrice"])
    print("Sale Price: ", json_data["productsById"][key]["pricesById"]["sale"]["minItemPrice"])
    media = json_data["productsById"][key]["mediaById"]
    im = random.choice(list(media.keys()))
    print("Image URL:", json_data["productsById"][key]["mediaById"][im]["src"])
    prodPageUrl = "nordstom.com"+str(json_data["productsById"][key]["productPageUrl"])
    print("Product Page Url: ",prodPageUrl)

q = "Natori Rose Dream Custom Coverage Underwire Bra"
nordstrom(q)