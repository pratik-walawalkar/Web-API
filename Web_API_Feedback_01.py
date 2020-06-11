#! /usr/bin/env python3

import os
import requests

folder = "/data/feedback/"
#content = {}
keys = ["title", "name", "date", "feedback"]

for files in os.listdir(folder):
  #print(files)
  #for file in files:
    keycount = 0
    content = {}
    #print(folder+files)
    #if os.path.isfile(folder+files):
    #print(files)
    with open(folder+files) as f:
      for line in f:
        value = line.strip()
        content[keys[keycount]] = value
        keycount += 1
        #print(value)
        #content[key] = value.strip()
        #content = {"title": value[0], "name": value[1], "date": value[2], "feedback":value[$
    print(content)
    response = requests.post("http://35.193.145.141/feedback", json=content)

print(response.request.body)
print(response.status_code)
