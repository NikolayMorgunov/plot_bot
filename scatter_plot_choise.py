def scatter_plot_choise(incoming, stage):
    scatter = False
    if incoming['message']['text'] == '/scatter':
        scatter = True
        stage = 'chosen type'
    elif incoming['message']['text'] == '/plot':
        scatter = False
        stage = 'chosen type'
    return stage, scatter
