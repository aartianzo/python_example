def pytest_addoption(parser):
    parser.addoption(
        '--num1', action='store'
    )
    parser.addoption(
        '--num2',action='store'
    )
pytest.fixture
def num1(request):
    return request.config.getoption('--num1')
def num2(request):
    return request.config.getoption('--num2')
