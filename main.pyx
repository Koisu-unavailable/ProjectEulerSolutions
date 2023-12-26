import sympy
import math
import sys

sys.setrecursionlimit(2147483647)
ret : int = 0
def cool_func(num:int) -> None:
    for i in range(math.floor(num/4)):
        i += math.floor(num/4)
        print(i)
        if i % 2 == 0: print("skip"); continue
        if sympy.isprime(i):
            if num % i == 0:
                print("FOUND")
                ret = i
cool_func(600851475143)
print(ret)
input("Input enter to exit: ")

