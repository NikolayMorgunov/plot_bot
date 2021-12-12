from send_mess import *
from get_chat_id import *


def asking_file(incoming, url):
    send_mess(get_chat_id(incoming),
              'Чтож, присылай файл в формате csv... Первый столбец по абсцисс, второй по ординат. Между двумя графиками пустая строка.',
              url)
    send_mess(get_chat_id(incoming),
              '/exit - Вернуться в начало.',
              url)
    return 'asked file'
