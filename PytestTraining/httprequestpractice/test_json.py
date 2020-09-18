import requests
from httprequestpractice.httppost import login_user

def test_login_user(base_url):
    uri = base_url + '/login'
    status_code, token = login_user(uri)
    assert status_code==200 and token == 'QpwL5tke4Pnpja7X4'

def test_list_users(base_url):
    url = base_url + '/users?page=2'
    response = requests.get(url)
    assert response.status_code == 200
    payload = response.json()
    assert payload['total'] == payload['page'] * payload['per_page']


