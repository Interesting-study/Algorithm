import requests
import json

def clean_data():
  r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
  removable_value = set(('N/A', '', '-'))
  r = r.json()
  answer = {}

  for key, value in r.items():
    if type(value) is dict:
      temp = {}
      for k, v in value.items():
        if v not in removable_value:
          temp[k] = v
      answer[key] = temp
    elif type(value) is list:
      answer[key] = [v for v in value if v not in removable_value]
    else:
      if value not in removable_value:
        answer[key] = value

  return answer

print(clean_data())