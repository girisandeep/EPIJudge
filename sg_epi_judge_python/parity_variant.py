
>>> bin(x)
'0b1010000'
>>> bin(x-1)
'0b1001111'
>>> bin(x |x-1)
'0b1011111'

>>> x = 77
>>> y = 64
>>> x & (y -1)
13

for x in range(1, 100):
...     if x & ~(x -1) == x:
...             print(x)
...

>>> for x in range(1, 100):
...     if x & x - 1 == 0:
...             print(x)
...
1
2
4
8
16
32
64