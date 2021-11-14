import os
import sys
import json
import requests
import eth_abi

SOUND_CHARTS = "https://sandbox.api.soundcharts.com/api/v2/artist/11e81bcc-9c1c-ce38-b96b-a0369fe50396/streaming/spotify/listeners/2020/10"


def call_api(url):
    s = requests.Session()
    s.headers.update({"x-app-id": "soundcharts"})
    s.headers.update({"x-api-key": "soundcharts"})
    s.headers.update({"Host": "sandbox.api.soundcharts.com"})

    response = s.get(url)
    print(response.json())

    if response.ok:
        return response.text


if __name__ == "__main__":
    call_api(SOUND_CHARTS)
