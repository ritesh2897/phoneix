import json

import openai


def open_ai(data="Say this is a test", model="text-davinci-002", max_tokens=6, temperature=0):
    openai.organization = "org-rYZGFk6DpgU2xw45KwnFrwXV"
    openai.api_key = "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"
    res = openai.Completion.create(
        model=model,
        prompt=data,
        max_tokens=max_tokens,
        temperature=temperature
    )
    return json.dumps([res.get('choices', [{}])[0].get("text")])
