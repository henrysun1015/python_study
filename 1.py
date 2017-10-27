# -*- coding: UTF-8 -*-
from  urllib import request
url = input('plase input you url( with http or https): ')

def gethtml(url):
	page = request.urlopen(url)
	html = page.read()
	return html
html = gethtml(url)
print(html)
