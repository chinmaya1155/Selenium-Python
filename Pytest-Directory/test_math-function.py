import math_function

def test_add():
    assert math_function.add(7,3) == 10
    assert math_function.add(8) == 10
def test_multi():
    assert math_function.multi(2,2) == 4
    assert math_function.multi(5) ==10
def test_div():
    assert math_function.div(4,2) == 2
    assert math_function.div(8) == 4
def test_sub():
    assert math_function.sub(4,2) == 2
    assert math_function.sub(8) == 6