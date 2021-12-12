import requests


def last_update(data):
    results = data['result']
    #print(results)
    if results:
        return results[-1]
