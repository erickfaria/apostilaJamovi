# SPDX-License-Identifier: MIT
# SPDX-FileCopyrightText: 2026 Erick Faria
"""Recalcula PCA e resumos de dimensões a partir do CSV; requer NumPy e SciPy.

Execute: python scripts/calcular_dimensoes.py
Lê o arquivo publicado sem modificá-lo. Exibe os cálculos na saída padrão,
sem acessar a rede, criar arquivos ou gerar uma nova base de dados.
A análise paralela ilustrativa usa simulação própria, independente do jamovi.
"""
import csv
from pathlib import Path

import numpy as np
from scipy import stats

DADOS = Path(__file__).resolve().parents[1] / 'dados'
INDICADORES = ([f'planejamento_{j}' for j in range(1, 5)]
               + [f'monitoramento_{j}' for j in range(1, 5)])

with (DADOS / 'exemplo_dimensoes.csv').open(encoding='utf-8', newline='') as arquivo:
    linhas = list(csv.DictReader(arquivo))
x = np.array([[float(linha[nome]) for nome in INDICADORES] for linha in linhas])
n, p = x.shape
r = np.corrcoef(x, rowvar=False)

# PCA da matriz de correlações, sem rotação.
autovalores, vetores = np.linalg.eigh(r)
autovalores = autovalores[::-1]
vetores = vetores[:, ::-1]
for k in range(2):
    if vetores[0, k] < 0:
        vetores[:, k] *= -1
cargas = vetores[:, :2] * np.sqrt(autovalores[:2])
porcentagens = 100 * autovalores / p
representacao = np.sum(cargas**2, axis=1)

# KMO global, usando correlações simples e parciais fora da diagonal.
inversa = np.linalg.inv(r)
parciais = -inversa / np.sqrt(np.outer(np.diag(inversa), np.diag(inversa)))
np.fill_diagonal(parciais, 0)
sem_diagonal = r.copy()
np.fill_diagonal(sem_diagonal, 0)
soma_r2 = np.sum(sem_diagonal**2)
soma_parciais2 = np.sum(parciais**2)
kmo = soma_r2 / (soma_r2 + soma_parciais2)

# Aproximação de Bartlett para a hipótese de matriz identidade.
bartlett = -(n - 1 - (2*p + 5)/6) * np.linalg.slogdet(r)[1]
gl_bartlett = p * (p - 1) // 2
p_bartlett = stats.chi2.sf(bartlett, gl_bartlett)

# Simulação paralela de PCA: percentil 95 por posição, não uma saída do jamovi.
semente_paralela = 20261026
repeticoes = 2000
rng = np.random.Generator(np.random.PCG64(semente_paralela))
replicas = np.empty((repeticoes, p))
for k in range(repeticoes):
    aleatorio = rng.standard_normal((n, p))
    r_aleatoria = np.corrcoef(aleatorio, rowvar=False)
    replicas[k] = np.linalg.eigvalsh(r_aleatoria)[::-1]
q95 = np.quantile(replicas, .95, axis=0, method='linear')

np.set_printoptions(precision=8, suppress=True)
print(f'Indicadores contínuos fictícios: n={n}, p={p}')
print('Ordem das colunas:', ', '.join(INDICADORES))
print('Correlações de Pearson:\n', r)
print('Autovalores iniciais da PCA:', autovalores)
print('Porcentagens da variância padronizada:', porcentagens)
print('Porcentagens acumuladas:', np.cumsum(porcentagens))
print('Cargas PCA sem rotação, dois componentes:\n', cargas)
print('Variância de cada indicador representada pelos dois componentes:', representacao)
print('Pesos do primeiro componente:', vetores[:, 0])
print(f'KMO global: {kmo:.10f}')
print(f'Bartlett aproximado: qui-quadrado={bartlett:.10f}, gl={gl_bartlett}, p={p_bartlett:.8g}')
print(f'Paralela PCA própria: {repeticoes} matrizes normais, semente={semente_paralela}')
print('Percentil 95 dos autovalores por posição:', q95)
print('Posições em que o observado supera o percentil 95:',
      np.flatnonzero(autovalores > q95) + 1)
print('As contas acima não estimam cargas ou correlações fatoriais de AFE.')
