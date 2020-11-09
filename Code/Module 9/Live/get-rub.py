# (c) TICSIA
#
#
import requests
response = requests.get('http://cbu.uz/ru/arkhiv-kursov-valyut/json/RUB/')
if response.status_code == 200:
    result = response.json()
    print(result)
    print(result[0]["Rate"])
else:
    print(f'Ошибка:{response.status_code}')