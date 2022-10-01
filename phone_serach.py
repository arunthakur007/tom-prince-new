import requests
import json


def main(phone):
    """    repr :     
    """
    url = "https://devapi.endato.com/PersonSearch"

    payload = json.dumps({
    "Phone": phone
    })
    headers = {
    'galaxy-ap-name': 'f5778850-ab32-401e-bca1-377606919ae0',
    'galaxy-ap-password': '54e01deb091c4df2bef74481b5093453',
    'galaxy-search-type': 'Person',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text),response.status_code

