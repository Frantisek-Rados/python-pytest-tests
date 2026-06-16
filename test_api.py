import requests

def test_api_vrati_200():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200


def test_api_vrati_spravny_title():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    expected_title = "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert data ["title"] == expected_title