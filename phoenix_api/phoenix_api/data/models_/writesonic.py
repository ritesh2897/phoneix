import requests


def writesonic(data="The options and the answer to the question - In Kabhi Khushi Kabhie Gham", tone_of_voice="funny",
               **kwargs):
    url = "https://api.writesonic.com/v1/business/content/content-rephrase?engine=economy&language=en"
    payload = {
        "content_to_rephrase": data,
        "tone_of_voice": tone_of_voice
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "X-API-KEY": "e0be6560-6b90-4963-b5bf-ee2299be41d5"
    }
    response = requests.post(url, json=payload, headers=headers)
    res = list(map(lambda x: x['text'], response.json()))
    return res
