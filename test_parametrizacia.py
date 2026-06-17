import pytest
import requests

@pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
def test_api_vrati_200_pre_vsetky(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200
