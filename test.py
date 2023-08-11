import requests

BASE = "http://127.0.0.1:5000/"

#data = [{"likes": 130, "name": "Brawl Stars GIVEAWAY", "views": 4500000},
#        {"likes": 500, "name": "How to build your own keyboard", "views": 1500000000},
#        {"likes": 1000, "name": "How to build your own PC", "views": 950000000}]

#for i in range(len(data)):
#    response = requests.put(BASE + "video/" + str(i), data[i])
#    print(response.json())

#input()

def displayVideos(videos):
    for video in videos:
        print("Video ID:", video["id"])
        print("Name:", video["name"])
        print("Views:", video["views"])
        print("Likes:", video["likes"])

response = requests.put(BASE + "video/2", {"name": "How to build your own PC", "views": 100, "likes": 50})

print(response.json())

response = requests.put(BASE + "video/3", {"name": "How to build your ROBLOX game", "views": 100000, "likes": 550})
print(response.json())

response = requests.patch(BASE + "video/2", {"name": "[UPDATED] How to build your own PC", "views": 750, "likes": 150})
print(response.json())

response = requests.get(BASE + "video/")
if response.status_code != 200:
    print(f"Error: received status code {response.status_code}")
    exit()
print("Raw Response:", response.text)

try:
    data = response.json()
except ValueError:
    print("Error")
    exit()






# videos = data if isinstance(data, list) else []
# displayVideos(videos)

videoIDToDelete = 2

response = requests.delete(BASE + "video/" + str(videoIDToDelete))

if response.status_code == 204:
    print(f"Video with ID {videoIDToDelete} has been successfully deleted")
else:
    print(f"Error: Received Status Code {response.status_code}: {response.text}")


response = requests.get(BASE + "video/")

if response.status_code != 200:
    print(f"Get Error: Received status code {response.status_code}")
    exit()
videos = response.json()
displayVideos(videos)
