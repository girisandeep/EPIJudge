def plus_one(A):
    carry_over = 1
    i = len(A) - 1
    while carry_over != 0 and i > -1:
        v = A[i] + carry_over
        carry_over = v // 10
        A[i] = v % 10
        i -= 1
    if carry_over != 0:
        return [1] + A
    return A
    
if __name__ == '__main__':
    A = [1,2,3]
    print(A)
    print(plus_one(A))