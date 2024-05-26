from project_youtube import main


def test_function1():
    r = main.my_first_function()
    assert r == "Hello Hammad"    # assert works to check either it equal to both ends or not


def test_function2() :
    r= main.my_first_function()
    assert r != "Hello World"

def test_function3() :
    r= main.my_first_function()
    assert r == "Hello World"
