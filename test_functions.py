from functions import salary, hello_who

def test_hello_who_max():
    assert hello_who("Max") == "Hello Max"


def test_hello_who_other():
    assert hello_who("Tom") == "Hello, Tom"
    assert hello_who("Bob") == "Hello, Bo"