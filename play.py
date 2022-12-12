# test/play.py

def test_params(params):
    print(params)
    assert params['username'] == 'test@gmail.com'
    assert params['password'] == '12345'
