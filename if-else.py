# ENUNCIADO
"""
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
"""

# Solución

n = int(input("Value of n:"))

if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print('Not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    else:
        print('Not Weird')