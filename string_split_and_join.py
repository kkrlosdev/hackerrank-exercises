# ENUNCIADO
"""
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
"""


# SOLUCIÓN
def split_and_join(line):
    newLine = line.replace(' ', '-')

    return newLine

line = input('Line -> ')
result = split_and_join(line)
print(result)