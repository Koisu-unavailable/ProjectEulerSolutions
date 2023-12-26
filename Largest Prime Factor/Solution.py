import sympy
import math 

ret : int = 0
skips = 0
def cool_func(num:int, skips) -> None:
    for i in range(math.floor(num/4)):
        i += math.floor(num/4)
        if i % 2 == 0 or i%3 == 0 or i%5 ==0 or i%7 == 0 or i%11 == 0 or i%13 == 0 or i%17 == 0 or i%19:
            print("skip")
            continue
        skips += 1
        print(i)
        if sympy.isprime(i):
            if num % i == 0:
                print("FOUND")
                ret = i
cool_func(600851475143, 0)
print(ret)
input("Input enter to exit: ")

