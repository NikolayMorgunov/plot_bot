from send_mess import *
from get_chat_id import *

def asking_legend(incoming, url):
    send_mess(get_chat_id(incoming), 'Как назвать графики?\n'
                                     'Введи названия для графиков по одному на строчку\n'
                                     '/exit - Вернуться в начало', url)

    return 'asking legend'
