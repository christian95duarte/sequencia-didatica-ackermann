# Sequência didática: da hierarquia das operações à Função de Ackermann

Animações em Manim e códigos em Python da sequência didática proposta na dissertação:

> DUARTE, Christian. **Iteração, crescimento e computabilidade no Ensino Médio: da hierarquia das operações à Função de Ackermann**. 2026. Dissertação (Mestrado Profissional em Matemática em Rede Nacional – PROFMAT) – Instituto de Ciências Ambientais, Químicas e Farmacêuticas, Universidade Federal de São Paulo, Diadema, 2026. Orientador: Prof. Dr. Anderson Augusto Ferreira.

A sequência tem cinco encontros de cerca de 50 minutos, para a 1ª ou a 2ª série do Ensino Médio. Os planos de aula estão no Apêndice B da dissertação, e os roteiros das animações, no Apêndice C.

## Conteúdo

| Encontro | Tema | Animação (código) | Vídeo | Habilidades da BNCC |
|---|---|---|---|---|
| 1 | A escada das operações | [`animacoes/b1_escada_das_operacoes.py`](animacoes/b1_escada_das_operacoes.py) | [`B1`](videos/B1_escada_das_operacoes.mp4) | EM13MAT405 |
| 2 | Progressão aritmética e função afim | [`animacoes/b2_pa_funcao_afim.py`](animacoes/b2_pa_funcao_afim.py) | [`B2`](videos/B2_pa_funcao_afim.mp4) | EM13MAT507, EM13MAT401 |
| 3 | Progressão geométrica e função exponencial | [`animacoes/b3_pg_funcao_exponencial.py`](animacoes/b3_pg_funcao_exponencial.py) | [`B3`](videos/B3_pg_funcao_exponencial.mp4) | EM13MAT508 |
| 4 | Linear contra exponencial | [`animacoes/b4_linear_vs_exponencial.py`](animacoes/b4_linear_vs_exponencial.py) | [`B4`](videos/B4_linear_vs_exponencial.mp4) | EM13MAT303, EM13MAT304 |
| 5 | O horizonte: a Função de Ackermann | [`animacoes/b5_horizonte_ackermann.py`](animacoes/b5_horizonte_ackermann.py) | [`B5`](videos/B5_horizonte_ackermann.mp4) | CG2, CE5 |

Códigos em Python puro, usados em sala e nas verificações do texto:

| Arquivo | Onde aparece na dissertação |
|---|---|
| [`python/encontro1_escada.py`](python/encontro1_escada.py) | Seção 4.3.1 e Apêndice C.1: soma, produto e potência, cada um chamando o anterior |
| [`python/encontro5_ackermann.py`](python/encontro5_ackermann.py) | Seção 4.3.5: investigação guiada com a Função de Ackermann (versão sem memoização) |
| [`python/simulacoes_4_4.py`](python/simulacoes_4_4.py) | Seção 4.4: contagem de chamadas, limite de recursão e fórmulas fechadas |
| [`python/euclides.py`](python/euclides.py) | Seção 3.6: Tabelas 3.2 e 3.3 e amostra aleatória (semente 2026) |

## Sem laboratório de informática

Os vídeos da pasta `videos/` podem ser projetados direto, sem instalar nada. Os scripts da pasta `python/` rodam em qualquer interpretador Python on-line, inclusive no celular.

## Como renderizar as animações

```bash
pip install -r requirements.txt
manim render -qm animacoes/b1_escada_das_operacoes.py
```

A opção `-ql` gera uma pré-visualização rápida em baixa resolução; `-qh` gera em 1080p. O Manim usado é a versão da comunidade (ManimCE), que exige LaTeX instalado para as fórmulas.

## Versões testadas

- Scripts da pasta `python/`: Python 3.13.
- Animações: Manim Community 0.22.0 com Python 3.12.

O limite de recursão do Python e o comportamento com inteiros muito grandes mudam entre versões. No Python 3.13, `ack(3, 7)` sem memoização interrompe com `RecursionError`, e com o limite elevado devolve 1021.

## Licença

Códigos sob a licença MIT (arquivo [`LICENSE`](LICENSE)). Os vídeos podem ser usados e adaptados livremente em sala de aula, com citação da dissertação.
