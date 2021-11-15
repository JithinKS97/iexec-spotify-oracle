import os
import sys
import json
import requests
import eth_abi


def get_api_url(id, month, year):
    return (
        "https://sandbox.api.soundcharts.com/api/v2/artist/"
        + id
        + "/streaming/spotify/listeners/"
        + year
        + "/"
        + month
    )


def get_monthly_count(url):
    s = requests.Session()

    s.headers.update({"x-app-id": "soundcharts"})
    s.headers.update({"x-api-key": "soundcharts"})
    s.headers.update({"Host": "sandbox.api.soundcharts.com"})

    response = s.get(url)
    data = response.json()
    dates = data["items"]
    total_count = 0
    for date in dates:
        cityPlots = date["cityPlots"]
        for item in cityPlots:
            total_count = total_count + item["value"]
            pass
        pass
    print(total_count)
    generate_callback({"count": total_count})

    if response.ok:
        return response.text


def generate_callback(data):
    iexec_out = os.environ["IEXEC_OUT"]

    with open(iexec_out + "/computed.json", "w+") as f:
        json.dump({"callback-data": data}, f)


if __name__ == "__main__":

    artist_id = "11e81bcc-9c1c-ce38-b96b-a0369fe50396"
    month = "10"
    year = "2020"

    url = get_api_url(artist_id, month, year)

    get_monthly_count(url)
