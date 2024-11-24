import pytest


@pytest.fixture
def json_content() -> str:
    return '''{
                "devices": [
                    {
                        "id": 123,
                        "alias": "Device123",
                        "status": "on",
                        "ip": "123.123.123.123"
                    },
                    {
                        "id": 321,
                        "alias": "Device321",
                        "status": "off",
                        "ip": "321.32.15.179"
                    }
                ]
            }'''
