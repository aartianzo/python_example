import pytest
def pytest_addoption(parser):
    parser.addoption(
        "--a","--b",
        action="store"
    )

# a = sys.argv[1]
# b = sys.argv[2]
@pytest.fixture
@fixture()
def sum(request):
    return request.config.getoptions("--a","--b")
# def sum("--a","--b"):
#     return a + b

# def test_add():
#     assert sum("--a","--b") > 10, ("sum less than 10")
#     assert sum(13, 4) == 17
    
