# ENUNCIADO

"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

# SOLUCIÓN

def swap_case(sentence):
    nueva_cadena = ''

    for char in sentence:
        if char.isupper():
            nueva_cadena += char.lower()
        elif char.islower():
            nueva_cadena += char.upper()
        else:
            nueva_cadena += char
    return nueva_cadena

sentence = input("Sentence -> ")
print(swap_case(sentence))