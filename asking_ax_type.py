from send_mess import *
from get_chat_id import *

def asking_ax_type(incoming, url, ax):
    send_mess(get_chat_id(incoming), f'Какой масштаб оси {ax} сделать?', url)
    send_mess(get_chat_id(incoming), '/linear - Линейный\n'
                                     '/log - Логарифмический по основанию 10\n'
                                     '/exit - Вернуться в начало', url)
    return f'asking ax {ax} type'
