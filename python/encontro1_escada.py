"""Encontro 1: a escada das operacoes (Secao 4.3.1 e Apendice C.1).

Cada operacao chama a anterior: soma itera o sucessor, prod itera a soma
e pot itera o produto.
"""


def soma(x, n): return x if n == 0 else soma(x, n-1) + 1
def prod(x, n): return 0 if n == 0 else soma(prod(x, n-1), x)
def pot(x, n):  return 1 if n == 0 else prod(pot(x, n-1), x)


print(prod(2, 4))   # 8  = 2+2+2+2
print(pot(2, 4))    # 16 = 2*2*2*2
