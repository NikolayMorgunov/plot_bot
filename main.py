from setup import *
from time import sleep
from get_updates_json import *
from last_update import *
from download_file import *
from starting import *
from wrong_chat import *
from scatter_plot_choise import *
from asking_difficulty import *
from choising_difficulty import *
from asking_file import *
from asking_ax_name import *
from ax_naming import *
from asking_ax_type import *
from ax_typing import *
from asking_legend import *
from getting_legend import *
from plot_drawing import *
from send_result import *


def main():
    update_id = last_update(get_updates_json(url, 0))['update_id']
    update_id = last_update(get_updates_json(url, update_id))['update_id'] + 1

    scatter = False
    stage = ''
    chat_id = ''
    hard_type = False
    message_id = ''
    ax_y_name = ''
    ax_x_name = ''
    ax_y_scale = 'linear'
    ax_x_scale = 'linear'
    legend = []

    while True:
        incoming = last_update(get_updates_json(url, update_id - 1))
        if update_id == incoming['update_id']:
            if stage and chat_id != get_chat_id(incoming):
                wrong_chat(incoming, url)
                update_id += 1
                sleep(1)
                continue

            print(incoming['message'])
            if stage == '' and 'text' in incoming['message'].keys():
                if incoming['message']['text'] == '/start':
                    stage, chat_id = starting(incoming, url)

            if 'text' in incoming['message'].keys():
                if incoming['message']['text'] == '/exit':
                    stage, chat_id = starting(incoming, url)

            if stage == 'started' and 'text' in incoming['message'].keys():
                stage, scatter = scatter_plot_choise(incoming, stage)

            if stage == 'chosen type':
                stage = asking_difficulty(incoming, url)

            if stage == 'asking difficulty' and 'text' in incoming['message'].keys():
                stage, hard_type = choising_difficulty(incoming, stage)

            if stage == 'chosen difficulty':
                stage = asking_file(incoming, url)

            if stage == 'asked file' and 'document' in incoming['message'].keys():
                download_file(token, incoming['message']['document']['file_id'])
                if hard_type:
                    stage = 'file downloaded'
                else:
                    stage = 'drawing'
                    ax_y_name = ''
                    ax_x_name = ''
                    ax_y_scale = 'linear'
                    ax_x_scale = 'linear'
                    legend = []

            if stage == 'file downloaded':
                stage = asking_ax_name(incoming, url)

            if stage == 'asking axes names' and 'text' in incoming['message'].keys():
                stage, ax_y_name, ax_x_name = ax_naming(incoming, stage)

            if stage == 'axes named':
                stage = asking_ax_type(incoming, url, 'y')

            if stage == 'asking ax y type' and 'text' in incoming['message'].keys():
                stage, ax_y_scale = ax_typing(incoming, stage, 'y')
                message_id = incoming['message']['message_id']

            if stage == 'ax y typed':
                stage = asking_ax_type(incoming, url, 'x')

            if stage == 'asking ax x type' and 'text' in incoming['message'].keys() and message_id != \
                    incoming['message']['message_id']:
                stage, ax_x_scale = ax_typing(incoming, stage, 'x')
                message_id = incoming['message']['message_id']

            if stage == 'ax x typed':
                stage = asking_legend(incoming, url)

            if stage == 'asking legend' and 'text' in incoming['message'].keys() and message_id != \
                    incoming['message']['message_id']:
                stage, legend = getting_legend(incoming, stage)

            if stage == 'drawing':
                stage = plot_drawing(ax_x_name, ax_y_name, ax_x_scale, ax_y_scale, scatter, legend)

            if stage == 'plot drawn':
                stage = send_result(incoming, url)
                chat_id = ''

            print(stage)
            update_id += 1
        sleep(1)


if __name__ == '__main__':
    main()
