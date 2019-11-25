
def divide(x, y):
    num = 0
    while x >= y:
        x = x - y
        num += 1 
    return num

print(divide(10, 2))
