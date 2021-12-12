from send_mess import *
from get_chat_id import *


def send_result(incoming, url):
    send_photo(get_chat_id(incoming), 'plot.png', url)
    send_mess(get_chat_id(incoming), '/start - Сделать еще один график', url)
    return ''
