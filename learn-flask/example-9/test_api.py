"""
To run this test do -
pytest
"""

import api
import pytest


@pytest.fixture()
def client():
    return api.app.test_client(use_cookies=False)


def test_me(client):
    resp = client.get("/me")
    user = resp.get_json()
    assert user["username"] == "quantum_random"
    assert not user["is_admin"]
    assert user["num_posts"] == 10
