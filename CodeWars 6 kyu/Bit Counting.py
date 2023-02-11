'''
Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.

Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
'''

#Решение
from collections import Counter
def count_bits(n):
    t = Counter(format(n, "b"))
    for k, v in t.items():
        if k == "1":
            return v
        else:
            return 0