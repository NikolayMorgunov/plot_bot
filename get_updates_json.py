import requests


def get_updates_json(request, offset):
    if not offset:
        response = requests.get(request + 'getUpdates')
    else:
        response = requests.get(request + 'getUpdates' + '?offset=' + str(offset))
    return response.json()
