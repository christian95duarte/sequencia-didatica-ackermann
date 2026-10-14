"""Algoritmo de Euclides (Secao 3.6): pior caso (Tabela 3.2),
custo efetivo (Tabela 3.3) e amostra aleatoria (Secao 3.6.4)."""
import random


def euclides(m, n):
    """Devolve (mdc, numero de divisoes efetuadas)."""
    k = 0
    while n != 0:
        m, n = n, m % n
        k += 1
    return m, k


# Tabela 3.2: pares de Fibonacci consecutivos
for par in [(8, 5), (21, 13), (55, 34), (144, 89), (377, 233), (610, 377)]:
    print(par, euclides(*par))

# Tabela 3.3
for par in [(1071, 462), (144, 89), (10**9 + 7, 10**8 + 3)]:
    print(par, euclides(*par))

# Secao 3.6.4: 200 mil pares aleatorios ate 10^12 (semente 2026)
random.seed(2026)
razao_max = 0
for _ in range(200_000):
    a, b = random.randint(1, 10**12), random.randint(1, 10**12)
    m, n = max(a, b), min(a, b)
    _, k = euclides(m, n)
    razao_max = max(razao_max, k / len(str(n)))
print(f"razao maxima divisoes/algarismos: {razao_max:.2f}")   # 3.45 no Python 3.13
