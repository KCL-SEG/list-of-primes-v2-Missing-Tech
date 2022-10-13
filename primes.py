"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    validate_input(number_of_primes)

    index = 2;
    while len(list) < number_of_primes:
        if is_prime(index):
            list.append(index)
        index+=1

    return list

def validate_input(num):
    if num < 1:
        raise ValueError('Works with numbers greater than 0 only')

def is_prime(num):
    for i in range(2, num):
        if is_factor(num, i):
            return False
    return True

def is_factor(a, b):
    if (a % b == 0):
        return True
    return False