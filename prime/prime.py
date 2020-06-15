from math import sqrt
import sys

file_path = sys.argv[1]

def is_prime(number):
    if number % 2 == 0 and number != 2:
        return 0

    for i in range(3,int(sqrt(number)) + 1, 2):
        if number % i == 0:
            return 0
    return 1

with open(file_path, 'r') as inputs:
    for number in inputs.readlines():
        print(is_prime(int(number)))
