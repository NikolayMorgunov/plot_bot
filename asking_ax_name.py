from send_mess import *
from get_chat_id import *


def asking_ax_name(incoming, url):
    send_mess(get_chat_id(incoming), 'Как оси назвать?\n'
                                     'Введи названия для y и x на разных строках', url)
    send_mess(get_chat_id(incoming), '/exit - Вернуться в начало', url)
    return 'asking axes names'
