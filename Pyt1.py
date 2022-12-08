def sum(a, b):
    return a + b


def test_add():
    assert sum((${{ secrets.env1 }}) + (${{ secrets.env2 }})) < 10
#     assert sum(5,7) > 10, ("sum less than 10")
   
