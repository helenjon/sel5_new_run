import pytest
from tests.parser_options import get_config


@pytest.fixture
def driver(selenium):
    selenium.implicitly_wait(300)
    selenium.maximize_window()
    return selenium


@pytest.fixture(scope="session", autouse=True)
def variables():
    vari = get_config()
    return vari


