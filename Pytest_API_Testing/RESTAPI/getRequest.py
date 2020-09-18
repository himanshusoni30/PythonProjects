import requests
import json


def baseURL():
    return 'https://reqres.in'


def fullURI(relURI):
    baseURI = baseURL()
    print("Base URL: " + baseURI)
    return baseURI + relURI


def test_my_first_get_request():
    url = fullURI('/api/users?page=2')
    print("Full URL: " + url)
    resp = requests.get(url)
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['total_pages'] == 2
    print("Response: " + str(resp_body))
