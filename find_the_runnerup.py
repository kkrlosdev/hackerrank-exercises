# Enunciado

"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given n scores. Store them in a list and find the score of the runner-up.
"""

# Solución

n = int(input())
arr = map(int, input().split())

lista = list(arr)
puntuaciones_unicas = set(lista)
puntuaciones_ordenadas = sorted(puntuaciones_unicas, reverse=True)
segundo_lugar = puntuaciones_ordenadas[1]
print(segundo_lugar)