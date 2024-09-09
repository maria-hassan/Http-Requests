import requests

response = requests.get('https://randomuser.me/api')
print(response.status_code)
print(response.json())

gender = response.json()['results'][0]['gender']
print(gender)

title = response.json()['results'][0]['name']['title']

firstname = response.json()['results'][0]['name']['first']

lastname = response.json()['results'][0]['name']['last']

age = response.json()['results'][0]['dob']['age']

print(f'{title}.{firstname} {lastname}')
print(f'Age:{age}')
