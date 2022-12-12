import json
import requests

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url=target)

users = response.json()

name_list = []
for user in users:
    name_list.append(user['name'])

print(name_list)
