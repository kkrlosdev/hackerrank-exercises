# Enunciado
"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports.
For example, "alison heck" should be capitalised correctly as "Alison Heck".
"""

# Solución

def solve(s):
    partes = s.split(' ')
    frase_capitalizada = [palabra.capitalize() for palabra in partes]
    return ' '.join(frase_capitalizada)
print(solve("hello world"))