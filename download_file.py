import requests
import os
import json


def download_file(token, file_id):
    path = os.getcwd()
    file = requests.post('https://api.telegram.org/bot' + token + '/getFile?file_id=' + file_id)
    path = json.loads(file.text)['result']['file_path']
    if path[-4:] == '.csv':
        response = requests.get('https://api.telegram.org/file/bot' + token + '/' + path)
        open('file.csv', 'wb').write(response.content)
    else:
        open('file.csv', 'wb').write(bytes('', encoding='utf-8'))
