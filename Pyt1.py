import sys

a = sys.argv[1]
b = sys.argv[2]

def sum(a, b):
    return a + b

def test_add(a, b):
    assert sum(a, b) > 10, ("sum less than 10")
