import json
from datetime import timedelta
from django.utils import timezone
from django.conf import settings
import requests


class GraphCreateException(Exception):
    pass


def get_coordinates(func: str, interval: int, dt: int)-> tuple:
    data = {
        "func": func,
        "start": (timezone.now() - timedelta(hours=interval)).isoformat(),
        "end": timezone.now().isoformat(),
        "dt": dt,
    }
    res = requests.post(settings.COORDINATE_GENERATE_API_URL,
                        headers={'Content-type': 'application/json', },
                        data=json.dumps(data),
                        timeout=5)

    if res.status_code != 200:
        raise GraphCreateException(res.text)

    if res.json().get("message"):
        raise GraphCreateException(res.json().get("message"))

    x, y = [], []
    for k in res.json().get("result"):
        x.append(k[0])
        y.append(k[1])
    return x, y


def get_graph(func: str, x: list, y: list, width: int=500)-> bytes:
    chart_structure = {
        "infile":
            {
                "title": {"text": func},
                "xAxis": {"categories": x},
                "series": [
                    {
                        "data": y,
                        "type": 'line',
                    }]
            },
        "type": "png",
        "width": width,
    }
    res = requests.post(url=settings.IMAGE_GENERATE_API_URL,
                        headers={'Content-type': 'application/json', },
                        data=json.dumps(chart_structure),
                        timeout=(5, 20))

    if res.status_code != 200:
        raise GraphCreateException(res.text)

    return res.content
