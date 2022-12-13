from pytest_easy_addoption import AddOption

class FooBarAddOption(AddOption):
    foo: str
    bar: str = 'BAR'

def pytest_addoption(parser):
    FooBarAddOption.register(parser)
