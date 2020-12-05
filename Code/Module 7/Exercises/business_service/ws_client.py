import requests
import DemoBot.config as config


def get_course(message):
    response = requests.get(config.ws)
    if response.status_code == 200:
        answer = response.json()
        result = "Один рубль равен {} тенге" .format(answer[0]['Rate'])
    else:
        result = "Ошибка {} получения курса валюты ".format(response.status_code)
    return result
    