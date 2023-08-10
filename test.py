#import pip._vendor.requests
import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 130, "name": "Brawl Stars GIVEAWAY", "views": 4500000},
        {"likes": 500, "name": "How to build your own keyboard", "views": 1500000000},
        {"likes": 1000, "name": "How to build your own PC", "views": 950000000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())
input()
response = requests.delete(BASE + "video/0")
print(response.json())
input()
response = requests.get(BASE + "video/2")
print(response.json())

