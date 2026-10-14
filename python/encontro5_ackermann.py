"""Encontro 5: o horizonte, a Funcao de Ackermann (Secao 4.3.5).

Versao sem memoizacao, de proposito: com ela, A(3, 7) e o primeiro valor
cujo calculo excede o limite padrao de 1000 chamadas aninhadas do Python.
O erro e um limite da ferramenta, nao da funcao.
"""
import sys


def ack(m, n):
    if m == 0: return n + 1
    if n == 0: return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


print(ack(2, 2))   # 7
print(ack(3, 3))   # 61
print(ack(3, 6))   # 509

try:
    print(ack(3, 7))
except RecursionError:
    print("A(3, 7): RecursionError (limite padrao de 1000 chamadas aninhadas)")

# Elevando o limite, o mesmo calculo termina em uma fracao de segundo:
sys.setrecursionlimit(5000)
print("A(3, 7) =", ack(3, 7))   # 1021
# ack(4, 2) tem 19 729 digitos e exigiria pelo menos A(4, 2) - 2 chamadas.
