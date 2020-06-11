#! /usr/bin/env python3

import os
import requests

# Path to the data
path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

feedback_folder = os.listdir(path)
for file in feedback_folder:
    key_count = 0
    fb_dict = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            fb_dict[keys[key_count]] = value
            key_count += 1
    print(fb_dict)
    response = requests.post("http://104.197.247.162/feedback/", json=fb_dict)
print(response.request.body)
print(response.status_code)