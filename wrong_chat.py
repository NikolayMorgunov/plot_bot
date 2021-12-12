from send_mess import *
from get_chat_id import *


def wrong_chat(incoming, url):
    send_mess(get_chat_id(incoming),
              'Подожди, я сейчас занят',
              url)
