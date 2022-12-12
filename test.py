pytest.fixture
def num1(request):
    return request.config.getoption('--num1')
def num2(request):
    return request.config.getoption('--num2')

def test_arguments(num1):
    response = request.get(num1)
    print(response.request.num1)
def test_arguments(num2):
    response = request.get(num2)
    print(response.request.num2)
    
    
