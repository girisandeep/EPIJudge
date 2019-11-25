def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def even_first(a):
    i = 0
    j = 1
    while i < len(a) - 1 and j < len(a):
        if a[i] % 2 == 1:
            while j <= i:
                j += 1
            while j < len(a):
                if a[j] % 2 == 0:
                    swap(a, i, j)
                    i += 1
                    j += 1
                    break
                j += 1
        else:
            i += 1
    return a

import random
def main():
    l = list(range(1, 100))
    random.shuffle(l)
    # l = [30, 48, 69, 71, 36, 76, 4, 98, 92, 26, 8, 58, 47, 13, 35, 38, 51, 67, 73, 32, 15, 50, 53, 31, 84, 10, 66, 21, 41, 24, 78, 95, 3, 85, 88, 99, 17, 86, 9, 96, 49, 2, 87, 68, 23, 34, 56, 61, 16, 45, 55, 64, 12, 25, 54, 39, 79, 70, 83, 94, 81, 46, 90, 59, 37, 62, 77, 97, 6, 72, 27, 44, 22, 42, 60, 80, 93, 43, 29, 33, 74, 40, 82, 18, 5, 91, 28, 19, 14, 1, 20, 52, 75, 63, 11, 65, 7, 89, 57]
    print(l)
    even_first(l)
    print("POST")
    print(l)
    print(check(l))

def check(a):
    if len(a) > 0:
        prev = a[0] %2

        for e in a[1:]:
            curr = e % 2
            if prev == 1 and curr == 0:
                return False
            prev = curr
    return True

if __name__ == "__main__":
    main()