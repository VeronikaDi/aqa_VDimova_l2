import pytest
import requests
from requests.auth import HTTPBasicAuth


@pytest.fixture(scope='class')
def authenticated_session():

    session = requests.Session()

    auth_url = 'http://127.0.0.1:8080/auth'
    credentials = {"username": "test_user", "password": "test_pass"}
    response = session.post(auth_url, auth=HTTPBasicAuth(credentials["username"], credentials["password"]))

    assert response.status_code == 200, "Authentication failed"

    access_token = response.json().get("access_token")
    assert access_token, "No access token found"

    session.headers.update({'Authorization': f'Bearer {access_token}'})

    return session
