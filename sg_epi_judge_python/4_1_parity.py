from test_framework import generic_test

# Parity is 1 if 1 bits are odd else partity is 0
def parity1(x):
    # TODO - you fill in here.
    count1 = 0
    while x > 0:
        count1 ^= x & 1
        x = x >> 1
    return count1 % 2

def parity2(x):
    count = 0
    while x > 0:
        x = x & (x - 1)
        count += 1
    return count % 2

def parity(x):
    #print("Computing parity", bin(x))
    y = x >> 32
    #print("After shift with 32: ", bin(y))
    x = x ^ y 
    #print("After XOR with y: ", bin(x))
    
    y = x >> 16
    #print("After shift with 16: ", bin(y))
    x = x ^ y 
    #print("After XOR with y: ", bin(x))

    y = x >> 8
    #print("After shift with 8: ", bin(y))
    x = x ^ y 
    #print("After XOR with y: ", bin(x))

    y = x >> 4
    #print("After shift with 4: ", bin(y))
    x = x ^ y 
    #print("After XOR with y: ", bin(x))

    y = x >> 2
    #print("After shift with 2: ", bin(y))
    x = x ^ y 
    #print("After XOR with y: ", bin(x))

    y = x >> 1
    #print("After shift with 2: ", bin(y))
    x = x ^ y 
    #print("After XOR with y: ", bin(x))

    return x & 0x1

if __name__ == '__main__':
    # parity(10000)
    generic_test.generic_test_main("parity.py", 'parity.tsv', parity)
    generic_test.generic_test_main("parity1.py", 'parity.tsv', parity1)
    exit(generic_test.generic_test_main("parity2.py", 'parity.tsv', parity2))
