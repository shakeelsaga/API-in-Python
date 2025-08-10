import requests

# url = "https://api.github.com/users/shakeelsaga"

# r = requests.get(url)
# r = r.json()

# username = r['login']

req = requests.post("https://httpbin.org/post", params = {"this": "that"}, data = {"shakeel": "saga"})

print(req.text)

# with open("index.html", 'w') as file:
#     file.write(req.text)