#! /usr/bin/env python3
import os
import requests

# Path to the data
path = "/data/feedback/"
url = "http://35.193.145.141/feedback/"
#keys of dictionary
keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)

for file in folder:
    keycount = 0
    content = {}
    with open(path + file) as f:
        for line in f:
            value = line.strip()
            content[keys[keycount]] = value
            keycount += 1
    print(content)
    #post content to Web API
    response = requests.post(url,json=content)

print(response.request.body)
print(response.status_code)
