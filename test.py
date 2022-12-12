def test_arguments(num1):
    response = request.get({num1})
    print(response.request.num1)
def test_arguments(num2):
    response = request.get({num2})
    print(response.request.num2)
    
    
