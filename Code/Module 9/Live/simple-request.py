import requests
response = r = requests.get('http://learn.python.ru')
print(response.status_code)
print(response.text)
