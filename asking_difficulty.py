from send_mess import *
from get_chat_id import *


def asking_difficulty(incoming, url):
    send_mess(get_chat_id(incoming), 'А заморачиваться сильно?', url)
    send_mess(get_chat_id(incoming), '/yes - Да\n'
                                     '/no - Нет\n'
                                     '/exit - Вернуться в начало', url)
    return 'asking difficulty'
