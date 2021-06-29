import requests, json

URL = 'https://hacker-news.firebaseio.com/v0/item/8863.json?print=pretty'
request = requests.get(url = URL)
r = request.json()

print(r['title'], r['by'], r['url'], )

