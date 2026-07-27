import requests

TOKEN = "HDEV-57ff8186-8393-4fd7-87f0-925db739f08f"
HEADERS = {"Authorization": TOKEN}

def mmr(name, tag):
    url = f"https://api.henrikdev.xyz/valorant/v3/mmr/{name}/{tag}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def matches(name, tag):
    url = f"https://api.henrikdev.xyz/valorant/v4/matches//pc/{name}/{tag}"
    response = requests.get(url, headers=HEADERS)
    return response.json()
