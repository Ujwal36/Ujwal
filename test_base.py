import json
from unittest.mock import MagicMock

from test_framework.common.web_server.base import APIBaseHandler


class TestJsonErrorRequestMock:
    def __init__(self, method, body):
        self.body = body
        self.method = method
        self.options = None
        self.environ = {
            'CONTENT_LENGTH': 0,
            'route_args': {},
            'headers': MagicMock()
        }

    @property
    def form(self):
        return (json.loads(self.body), None)


def test_json_decoding_error_handling():
    """Test APIBaseHandler for json decode error handling."""

    request_body = '{"a":"b}'
    request = TestJsonErrorRequestMock(method="GET", body=request_body)

    expected = {
        'reason': '`Unterminated string starting at` at 5 in `{"a":"b}`'
    }

    response = APIBaseHandler(request)
    assert response.status_code == 400
    assert response.buffer[0].decode() == json.dumps(expected, separators=(',', ':'))
