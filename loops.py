# Enunciado

"""
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2.
"""

# Solución

n = int(input("Value of n -> "))
i = 0
    
while i < n:
    print(i**2)
    i += 1