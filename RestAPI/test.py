import requests
import json

year = 2011
competition = "UEFA Champions League"

URL = "https://jsonmock.hackerrank.com/api/football_competitions"
match_URL = "https://jsonmock.hackerrank.com/api/football_matches"

params = {
    'name': competition,
    'year': str(year)
}
response = requests.get(url=URL, params=params).json()
winner = response.get('data')[0]['winner']

print(winner)