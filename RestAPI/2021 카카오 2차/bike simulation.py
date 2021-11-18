import requests
import json

URL = "https://kox947ka1a.execute-api.ap-northeast-2.amazonaws.com/prod/users"

def startAPI():
    headers = {
        'X-Auth-Token': 'a53ca4e818a0d1a63e15653c3c8ca7bc',
        'Content-Type': 'application/json',
    }

    data = '{ "problem": 1 }'

    response = requests.post(url=URL+'/start', headers=headers, data=data)

    Auth_data = response.json()
    Auth_json = json.loads(json.dumps(Auth_data))
    Auth_key = Auth_json.get("auth_key")
    Auth_time = Auth_json.get("time")

    return Auth_key

startAPI()