import requests

url = 'https://api64.ipify.org?format=json'

r = requests.get(url)
print(r.json())