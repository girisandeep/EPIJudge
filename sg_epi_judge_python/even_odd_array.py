import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def swap(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def even_odd(a):
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

@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure("Even elements appear in odd part")
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure("Elements mismatch")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("even_odd_array.py",
                                       'even_odd_array.tsv', even_odd_wrapper))
