# test/conftest.py
import pytest

def pytest_addoption(parser):
    parser.addoption("--num1", action="store")
    parser.addoption("--num2", action="store")

@pytest.fixture
def add(request):
    add_value1 = request.config.getoption.num1
    add_value2 = request.config.getoption.num2
    if add_value1 or add_value2 is less than 10:
        pytest.skip()
    return add
