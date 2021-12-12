def choising_difficulty(incoming, stage):
    hard_type = False
    if incoming['message']['text'] == '/yes':
        hard_type = True
        stage = 'chosen difficulty'
    elif incoming['message']['text'] == '/no':
        hard_type = False
        stage = 'chosen difficulty'
    return stage, hard_type
