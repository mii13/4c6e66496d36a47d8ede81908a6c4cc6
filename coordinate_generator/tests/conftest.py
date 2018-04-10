import os
import pytest
from app.factory import create_app


@pytest.fixture(scope="session")
def app():
    os.environ["FLASK_CONFIGURATION"] = "testing"
    ap = create_app()
    return ap
