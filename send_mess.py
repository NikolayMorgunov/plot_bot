import requests


def send_mess(chat, text, url):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def send_photo(chat, filename, url):
    result = open(filename, 'rb')
    response = requests.post(url + 'sendPhoto?chat_id=' + str(chat), files={'photo': result})
    return response
