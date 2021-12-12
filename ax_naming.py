def ax_naming(incoming, stage):
    if incoming['message']['text'] != '/exit':
        s = incoming['message']['text'].split('\n')
        if not s:
            return 'axes named', '', ''
        if len(s) == 1:
            return 'axes named', s[0], ''
        if len(s) >= 2:
            return 'axes named', s[0], s[1]
    return stage, '', ''
