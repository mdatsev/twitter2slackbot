import requests
import json
import time
import os

headers = {
    'Content-type': 'application/json',
}

def get_secret(name):
    locations = ["/run/secrets/", "/var/openfaas/secrets/"]
    for loc in locations:
        if os.path.isfile(loc + name):
            with open(loc + name, "r") as f:
                return f.read()
    raise "Secret not found: " + name

def handle(req):
    url = get_secret("slack-webhook")
    tweet = json.loads(req)
    message = json.dumps({
        "text": "<{}| >".format(tweet["link"]),
        "unfurl_links": True
    })
    requests.post(url, 
        headers=headers, 
        data=message)
