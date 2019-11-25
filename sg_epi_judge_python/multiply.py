def add3bits(x, y, c):
    if x & y & c:
        return (1, 1)
    if x | y | c == 0:
        return (0, 0)
    xor = x ^ y ^ c
    if xor == 1: # number of 1 is 1
        return (0, 1)
    else:
        # There are two 1s
        return (1, 0)

def add(x, y):
    # print("Expected: %s, %s + %s"%(x+y, x, y))
    carryover = 0
    n = 0
    result = 0
    while x > 0 or y > 0:
        bx = x & 1
        by = y & 1
        (carryover, br) = add3bits(bx, by, carryover)
        result = result | br << n
        x = x >> 1
        y = y >> 1
        n += 1
    if carryover:
        result = result | (carryover << n)
    return result

def add1(x, y):
    print("Expected: %s, %s + %s"%(x+y, x, y))
    carryover = 0
    n = 0
    result = 0
    # print(x, ": ", bin(x))
    # print(y, ": ", bin(y))
    while x > 0 or y > 0:
        # print("--"*5)
        bx = x & 1
        by = y & 1
        # print("Adding bx: %s, by: %s, carryover: %s" 
        #     % (bin(bx), bin(by), bin(carryover)))
        newc = 0
        
        br = 0
        if bx & by:
            newc = 1 << 1
            br = 0
        else:
            br = (bx | by) & 1
        carryover = carryover | newc
        if (carryover & 1) & br:
            carryover = 1 << 1
            br = 0
        else:
            br = (br | (carryover & 1))&1
        # print("BR", bin(br))
        
        result = result | br << n
        # print("Result:", bin(result))
        # print("carryover:", bin(carryover))
        carryover = carryover >> 1
        x = x >> 1
        y = y >> 1
        n += 1
    if carryover:
        result = result | (carryover << n)

    return result

def multiply(x, y):
    print("Expected: %s, %s * %s"%(x*y, x, y))
    result = 0
    n = 0
    while x > 0 and y > 0:
        if y & 1:
            result = add(result, x << n)
        n += 1
        y = y >> 1
    return result

print(multiply(10, 15))
print(multiply(90, 35))
print(multiply(9, 30))

# print(add(201783, 31258))
# print(add(29819,298179721))
