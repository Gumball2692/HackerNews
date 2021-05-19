import time
import requests_html

s = requests_html.HTMLSession()

resp = s.get("https://hn.algolia.com/?q=sql")

time.sleep(1)
resp.html.render()
time.sleep(1)
print(len(resp.html.html), " chars")
for idx, i in enumerate(resp.html.xpath('//div[@class="Story_title"]'), start=1):
	print(idx, i.text)
