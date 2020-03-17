from functions import salary, hello_who

def test_hello_who_max():
    assert hello_who('Max') == 'Hello, Max'
def test_hello_who_other():
    assert hello_who('Leo') == 'Hello, Leo'
    assert hello_who('Nik') == 'Hello, Nik'
    assert hello_who('Max') == 'Hello, Max'