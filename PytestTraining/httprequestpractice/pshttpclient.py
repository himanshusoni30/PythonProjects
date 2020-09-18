import requests
from pprint import pprint as pp

url = 'https://reqres.in/api/users?page=2'
response = requests.get(url)
print(response.status_code)
print()
print(response.headers)
print()
output = response.json()
pp(output)
page = output.get('page')
per_page = output.get('per_page')
total = output.get('total')

assert page*per_page==total
