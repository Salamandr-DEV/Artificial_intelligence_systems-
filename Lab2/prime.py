import itertools as it
from kanren import *
from kanren.core import *
from sympy.ntheory.generate import prime, isprime

def check_prime(x):
    if isvar(x):
        return condeseq([(eq, x, p)] for p in map(prime, it.count(1)))
    else:
        return success if isprime(x) else fail

x = var()

list_nums = (23, 4, 27, 17, 13, 10, 21, 29, 3, 32, 11, 19)
print('\nList of primes in the list:')
print(set(run(0, x, (membero, x, list_nums), (check_prime, x))))

print('\nList of first 7 prime numbers:')
print(run(7, x, check_prime(x)))