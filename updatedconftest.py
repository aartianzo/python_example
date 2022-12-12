import pytest
def pytest_addoption(parser):
    parser.addoption(
        '--num1', action='store'
    )
    parser.addoption(
        '--num2',action='store'
    )

