import pytest
def pytest_addoption(parser):
    parser.addoption(
        '--num1', action='store'
    )
    parser.addoption(
        '--num2',action='store'
    )

def test_arguments(num1):
    response = request.get(num1)
    print(response.request.num1)
def test_arguments(num2):
    response = request.get(num2)
    print(response.request.num2)
    
