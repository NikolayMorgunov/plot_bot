def ax_typing(incoming, stage, ax):
    if incoming['message']['text'] == '/linear' or incoming['message']['text'] == '/log':
        return f'ax {ax} typed', incoming['message']['text'][1:]
    return stage, ''
