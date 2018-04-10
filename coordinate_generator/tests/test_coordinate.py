import json
import pytest
from flask import url_for


@pytest.mark.usefixtures('client_class')
class TestCoordinateGenerate:
    endpoint = "coordinates"

    def test_post(self):
        data = {
            "func": "t+2",
            "start": "2018-04-06T13:14:19",
            "end": "2018-04-06T14:15:44",
            "dt": 1,
        }
        resp = self.client.post(url_for(TestCoordinateGenerate.endpoint), data=json.dumps(data))
        assert resp.json.get("result") == [['2018-04-06T13:14:19', 1523020461],
                                           ['2018-04-06T14:14:19', 1523024061]]

    @pytest.mark.parametrize("func", ["t+2A", "DROP TABLE", "1"])
    def test_bad_func(self, func):
        data = {
            "func": func,
            "start": "2018-04-06T13:14:19",
            "end": "2018-04-06T14:15:44",
            "dt": 1,
        }
        resp = self.client.post(url_for(TestCoordinateGenerate.endpoint), data=json.dumps(data))
        print(resp.json)
        assert resp.json.get("error_code") == 400

    def test_without_parameters(self):
        resp = self.client.post(url_for(TestCoordinateGenerate.endpoint), data=json.dumps({}))
        assert resp.json.get("error_code") == 400
