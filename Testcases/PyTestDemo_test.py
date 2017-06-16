def add(a,b):
    z = a+b
    return z


def mul(a,b):
    c = a*b
    return c


def sub(a,b):
    c = a-b
    return c


def test_add():
    add(1,2) == 3,"Add rest success"


def test_mul():
    mul(2,3) == 7,"Mul test failed.."


def test_sub():
    sub(3,2) == 1,"Sub test pass.."


