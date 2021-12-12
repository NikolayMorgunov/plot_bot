from send_mess import *
from get_chat_id import *


def starting(incoming, url):
    send_mess(get_chat_id(incoming),
              'Привет! Я бот, который может построить график по твоим данным. Давай решим сначала, что тебе нужно',
              url)
    send_mess(get_chat_id(incoming), '/scatter - Точки на плоскости\n'
                                     '/plot - График по точкам', url)
    chat_id = incoming['message']['chat']['id']
    return 'started', get_chat_id(incoming)
