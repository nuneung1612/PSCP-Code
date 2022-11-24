"""GCD_N"""
import math
from functools import reduce

def gcd_n(numlist):
    """to find gcd"""
    numa = reduce(math.gcd, numlist)
    return numa

def main():
    """input"""
    count = int(input())
    array = []
    for _ in range(count):
        num = int(input())
        array.append(num)
    print(gcd_n(array))
main()
