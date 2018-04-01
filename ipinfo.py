import requests
import json


def fetch_html(url):
    print(url)
    res = requests.get(url)
    if res.status_code == 200:
        return res.content
    else:
        return '<html></html>'


def fetch_info(ip):
    base_uri = 'https://ipinfo.io'
    endpoint = base_uri + '/' + ip
    html = fetch_html(endpoint)
    return json.loads(html)