#!/usr/bin/env python

import requests

pageLink = "https://www.dknmu.in/Manage/StudentView/studentdetail.aspx?mid=01309civ008"
page = requests.get(pageLink)

with open('/home/elitem/Downloads/Dashboard.html', "w") as file:
	file.write(page.text)