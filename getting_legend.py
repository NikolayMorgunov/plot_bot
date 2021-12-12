def getting_legend(incoming, stage):
    if incoming['message']['text'] != '/exit':
        s = incoming['message']['text'].split('\n')
        return 'drawing', s
    return stage, []
