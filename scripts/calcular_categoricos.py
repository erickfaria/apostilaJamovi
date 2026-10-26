"""Cálculos didáticos dos modelos multinomial e ordinal do capítulo 11.

Requer NumPy e SciPy. Lê os CSVs, ajusta por máxima verossimilhança e
exibe coeficientes e probabilidades. Não modifica arquivos nem acessa a rede.
"""
import csv
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit, logsumexp

PASTA = Path(__file__).resolve().parents[1] / 'dados'


def ler(nome, resposta, niveis):
    with (PASTA / nome).open(encoding='utf-8', newline='') as arquivo:
        linhas = list(csv.DictReader(arquivo))
    horas = np.array([float(r['horas_preparo']) for r in linhas])
    y = np.array([niveis.index(r[resposta]) for r in linhas])
    return horas, y


# Multinomial, referência Texto; dois coeficientes por comparação.
horas, y = ler('exemplo_multinomial.csv', 'recurso', ['Texto', 'Video', 'Oficina'])
x = np.column_stack([np.ones(len(horas)), horas])
indicadores = np.eye(3)[y]


def objetivo_multinomial(b):
    betas = b.reshape(2, 2)
    eta = np.column_stack([np.zeros(len(x)), x @ betas.T])
    logp = eta-logsumexp(eta, axis=1, keepdims=True)
    p = np.exp(logp)
    gradiente = ((p[:, 1:]-indicadores[:, 1:]).T @ x).ravel()
    return -np.sum(logp[np.arange(len(y)), y]), gradiente


ajuste = minimize(objetivo_multinomial, np.zeros(4), jac=True,
                  method='BFGS', options={'gtol': 1e-8})
b = ajuste.x.reshape(2, 2)
print('Multinomial: Video/Texto e Oficina/Texto; colunas intercepto e horas')
print(b)
print('Fatores multiplicativos das razões de probabilidades:', np.exp(b[:, 1]))
print('Log-verossimilhança:', -ajuste.fun, 'AIC:', 2*ajuste.fun+8)
print('Norma do gradiente:', np.linalg.norm(ajuste.jac))
novos = np.column_stack([np.ones(5), np.arange(1, 6)])
eta = np.column_stack([np.zeros(5), novos @ b.T])
p = np.exp(eta-logsumexp(eta, axis=1, keepdims=True))
print('Probabilidades de Texto, Video, Oficina em 1 a 5 horas:')
print(p)

# Ordinal: logit P(Y<=j | x) = theta_j - beta*x.
horas, y = ler('exemplo_ordinal.csv', 'avaliacao', ['Baixa', 'Media', 'Alta'])


def objetivo_ordinal(v):
    beta, theta1, logdistancia = v
    theta2 = theta1+np.exp(logdistancia)
    f1 = expit(theta1-beta*horas)
    f2 = expit(theta2-beta*horas)
    p = np.column_stack([f1, f2-f1, 1-f2])
    selecionada = np.maximum(p[np.arange(len(y)), y], np.finfo(float).tiny)
    s1, s2 = f1*(1-f1), f2*(1-f2)
    d_beta = np.where(y == 0, -horas*s1,
                      np.where(y == 1, -horas*(s2-s1), horas*s2))
    d_theta = np.where(y == 0, s1, np.where(y == 1, s2-s1, -s2))
    d_dist = np.where(y == 0, 0, np.where(y == 1, np.exp(logdistancia)*s2,
                                        -np.exp(logdistancia)*s2))
    gradiente = -np.array([np.sum(d/selecionada) for d in [d_beta, d_theta, d_dist]])
    return -np.log(selecionada).sum(), gradiente


ajuste_ord = minimize(objetivo_ordinal, [0.6, 1.0, np.log(2)], jac=True,
                      method='BFGS', options={'gtol': 1e-6})
beta, theta1, distancia = ajuste_ord.x
theta2 = theta1+np.exp(distancia)
xnovo = np.arange(1, 6)
f1 = expit(theta1-beta*xnovo)
f2 = expit(theta2-beta*xnovo)
print('Ordinal: beta, theta1, theta2:', beta, theta1, theta2)
print('OR comum para categorias superiores:', np.exp(beta))
print('Log-verossimilhança:', -ajuste_ord.fun, 'AIC:', 2*ajuste_ord.fun+6)
print('Norma do gradiente:', np.linalg.norm(ajuste_ord.jac))
print('Probabilidades de Baixa, Media, Alta em 1 a 5 horas:')
print(np.column_stack([f1, f2-f1, 1-f2]))
