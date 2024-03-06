import pytest

sever_url = None


@pytest.fixture(autouse=True)
def server_url():
    global server_url
    server_url = 'http://localhost:8282/sensorhub'
