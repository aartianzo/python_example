import pytest

def pytest_addoption(parser):
  parser.addoption("--num1", action="store", default=5, help="test num1")
  parser.addoption("--num2", action="store", default=0, help="test num2 ")
  
  
@pytest.fixture
def num1(request):
  return int(request.config.getoption("--num1"))

@pytest.fixture
def num2(request):
  return int(request.config.getoption("--num2"))
