import requests

parameters = {"firstname": "Maria", "lastname": "Hassan", "Age": 23}
response = requests.get("https://httpbin.org/get", params=parameters)
print(response.url)
