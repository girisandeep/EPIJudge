import math

def pow_(x, y):
    if y == 0:
        return 0
    if y == 1:
        return x
    r = pow_(x*x, y >> 1)
    if y &1:
        r = r * x
    return r

def test_pow(x, y):
    r = pow_(x, y)
    print("Pow(%s, %s), Exp: %s, Actual: %s" % (x, y, math.pow(x, y), r))

if __name__ == "__main__":
    test_pow(2.5, 2)
    test_pow(100, 4)