# test/conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--num1", action="store", help="input num1")
    parser.addoption("--num2", action="store", help="input num2")

@pytest.fixture
def params(request):
    params = {}
    params['num1'] = request.config.getoption('--num1')
    params['num2'] = request.config.getoption('--num2')
    if params['num1'] or params['num2'] is greater than 10:
        pytest.skip()
    return params
