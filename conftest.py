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
#     if params['username'] is None or params['password'] is None:
#         pytest.skip()
    return params
