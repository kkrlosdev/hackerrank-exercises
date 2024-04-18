def split_and_join(line):
    newLine = line.replace(' ', '-')

    return newLine

line = input('Line -> ')
result = split_and_join(line)
print(result)