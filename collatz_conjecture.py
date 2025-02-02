
import math

def collatz(n):
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            print(math.floor(n))
        else:
            n = n * 3 + 1
            print(math.floor(n))

n = int(input("Enter a number: "))
collatz(n)