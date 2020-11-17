#!/usr/bin/env python

import urllib.request
import urllib.parse

#x = urllib.request.urlopen('https://www.google.com')
#print(x.read())

url = 'http://pythonprogramming.net'
values = {'s':'basic','submit':'search'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respdata = resp.read()
print(respdata)