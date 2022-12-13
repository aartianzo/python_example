import sys

a = sys.argv[1]
b = sys.argv[2]

def sum(a, b):
    return a + b

def test_add():
    assert sum(12, 3) > 10, ("sum less than 10")
    assert sum(12,3) : 15
    
