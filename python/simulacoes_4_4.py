"""Simulacoes da Secao 4.4: contagem de chamadas, limite pratico
e verificacao das formulas fechadas da Funcao de Ackermann."""
import math
import sys
from functools import lru_cache

# 4.4.1 Implementacao direta e contagem de chamadas
chamadas = 0


def ack(m, n):
    global chamadas
    chamadas += 1
    if m == 0: return n + 1
    if n == 0: return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


for (m, n) in [(1, 1), (2, 2), (3, 3)]:
    chamadas = 0
    v = ack(m, n)
    print(f"A({m},{n}) = {v}  -  {chamadas} chamadas")   # 4, 27 e 2432 chamadas

# 4.4.2 O limite pratico: profundidade de recursao
print(sys.getrecursionlimit())   # 1000, valor padrao
try:
    print(ack(3, 7))
except RecursionError:
    print("RecursionError: profundidade maxima excedida")


# 4.4.3 Tabela de valores e verificacao das formulas fechadas
@lru_cache(maxsize=None)
def A(m, n):
    if m == 0: return n + 1
    if n == 0: return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))


for n in range(5):
    assert A(1, n) == n + 2
    assert A(2, n) == 2*n + 3
    assert A(3, n) == 2**(n + 3) - 3
print("formulas fechadas verificadas para n = 0..4")

digitos = math.floor(65536 * math.log10(2)) + 1
print(digitos)   # 19729
