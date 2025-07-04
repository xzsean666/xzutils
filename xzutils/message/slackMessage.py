import requests


def sendMessage(webhook, msg):

    headers = {
        "Content-type": "application/json",
    }

    json_data = {
        "text": msg,
    }

    response = requests.post(
        webhook,
        headers=headers,
        json=json_data,
    )
    return response
