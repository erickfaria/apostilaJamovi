"""Recalcula os exemplos a partir dos CSVs; requer NumPy e SciPy.

Execute na raiz: python scripts/calcular_exemplos.py
Não depende do PDF nem de tabelas copiadas da interface do jamovi.
"""
import csv
from pathlib import Path
import numpy as np
from scipy import stats
from scipy.special import expit

DADOS = Path(__file__).resolve().parents[1] / 'dados'

def ler(nome):
    with (DADOS / nome).open(encoding='utf-8', newline='') as arquivo:
        return list(csv.DictReader(arquivo))

def coluna(linhas, nome):
    return np.array([float(linha[nome]) for linha in linhas])

def mostrar(titulo, **valores):
    print(titulo)
    for nome, valor in valores.items():
        print(f'  {nome}: {np.asarray(valor)}')

# Regressão múltipla: intercepto + horas + nota anterior.
notas = ler('exemplo_notas.csv')
y = coluna(notas, 'depois')
x = np.column_stack([np.ones(len(y)), coluna(notas, 'horas'), coluna(notas, 'antes')])
b = np.linalg.lstsq(x, y, rcond=None)[0]
sse = np.sum((y - x @ b)**2)
sst = np.sum((y - np.mean(y))**2)
gl = len(y) - x.shape[1]
s2 = sse / gl
se = np.sqrt(np.diag(s2 * np.linalg.inv(x.T @ x)))
ic = b[:, None] + np.outer(se, [-1, 1]) * stats.t.ppf(.975, gl)
r2 = 1 - sse / sst
x_simples = x[:, :2]
b_simples = np.linalg.lstsq(x_simples, y, rcond=None)[0]
sse_simples = np.sum((y - x_simples @ b_simples)**2)
f_mudanca = (sse_simples - sse) / s2
mostrar('Regressão múltipla', coeficientes=b, erros_padrao=se, IC95=ic,
        R2=r2, R2_ajustado=1-(1-r2)*(len(y)-1)/gl,
        F_acrescimo_antes=f_mudanca, p_acrescimo=stats.f.sf(f_mudanca, 1, gl),
        previsao_3h_antes52=np.array([1, 3, 52]) @ b,
        VIF=1/(1-np.corrcoef(x[:, 1], x[:, 2])[0, 1]**2))
# Intervalos do modelo simples, em três horas.
s2_simples = sse_simples / (len(y)-2)
x0 = np.array([1., 3.])
h0 = x0 @ np.linalg.inv(x_simples.T @ x_simples) @ x0
critico = stats.t.ppf(.975, len(y)-2)
previsao = x0 @ b_simples
mostrar('Regressão simples: três horas', media=previsao,
        IC95_media=previsao + np.array([-1, 1])*critico*np.sqrt(s2_simples*h0),
        IP95_individual=previsao + np.array([-1, 1])*critico*np.sqrt(s2_simples*(1+h0)))
critico = stats.t.ppf(.975, 126)
ncp = .5*np.sqrt(64/2)
poder = stats.nct.sf(critico, 126, ncp) + stats.nct.cdf(-critico, 126, ncp)
mostrar('Planejamento: t bilateral, d=0,5, n=64 por grupo', poder=poder)

# Decomposição da ANOVA fatorial balanceada 2 x 2.
fatorial = ler('exemplo_fatorial.csv')
media = np.mean(coluna(fatorial, 'pontos'))
medias_celulas = {}
ss_erro = 0.
for formato in ['Texto', 'Video']:
    for pratica in ['Nao', 'Sim']:
        celula = [r for r in fatorial if r['formato'] == formato and r['pratica'] == pratica]
        valores = coluna(celula, 'pontos')
        medias_celulas[formato, pratica] = valores.mean()
        ss_erro += np.sum((valores-valores.mean())**2)
ss_efeitos = []
for fator in ['formato', 'pratica']:
    ss = 0.
    for nivel in sorted({r[fator] for r in fatorial}):
        valores = coluna([r for r in fatorial if r[fator] == nivel], 'pontos')
        ss += len(valores) * (valores.mean()-media)**2
    ss_efeitos.append(ss)
ss_entre = sum(6*(m-media)**2 for m in medias_celulas.values())
ss_interacao = ss_entre - sum(ss_efeitos)
fs = np.array([*ss_efeitos, ss_interacao]) / (ss_erro/20)
mostrar('ANOVA fatorial: formato, prática, interação', medias=list(medias_celulas.values()),
        SQ=[*ss_efeitos, ss_interacao, ss_erro], F=fs, p=stats.f.sf(fs, 1, 20),
        eta_parcial_interacao=ss_interacao/(ss_interacao+ss_erro))

# ANOVA de tempo, SEM fator entre pessoas e SEM correção de esfericidade.
repetidas = ler('exemplo_medidas_repetidas.csv')
a = np.column_stack([coluna(repetidas, v) for v in ['inicial', 'final', 'seguimento']])
n, k = a.shape
ss_tempo = n * np.sum((a.mean(axis=0)-a.mean())**2)
ss_pessoas = k * np.sum((a.mean(axis=1)-a.mean())**2)
ss_total = np.sum((a-a.mean())**2)
ss_residuo = ss_total-ss_tempo-ss_pessoas
f_tempo = (ss_tempo/(k-1))/(ss_residuo/((n-1)*(k-1)))
friedman = stats.friedmanchisquare(*a.T)
mostrar('Medidas repetidas: um fator tempo', medias=a.mean(axis=0),
        SQ=[ss_tempo, ss_pessoas, ss_residuo], F_nao_corrigido=f_tempo,
        p_nao_corrigido=stats.f.sf(f_tempo, k-1, (n-1)*(k-1)),
        Friedman=friedman.statistic, p_Friedman=friedman.pvalue)

# Logística binária por máxima verossimilhança (Newton/IRLS).
logistica = ler('exemplo_logistica.csv')
y = coluna(logistica, 'concluiu')
x = np.column_stack([np.ones(len(y)), coluna(logistica, 'horas')])
b = np.zeros(x.shape[1])
for _ in range(100):
    p = expit(x @ b)
    informacao = x.T @ ((p*(1-p))[:, None]*x)
    passo = np.linalg.solve(informacao, x.T @ (y-p))
    b += passo
    if np.max(np.abs(passo)) < 1e-12:
        break
else:
    raise RuntimeError('O ajuste logístico não convergiu')
p = expit(x @ b)
informacao = x.T @ ((p*(1-p))[:, None]*x)
se = np.sqrt(np.diag(np.linalg.inv(informacao)))
ic_or = np.exp(b[1] + np.array([-1, 1])*stats.norm.ppf(.975)*se[1])
mostrar('Logística: evento 1, referência 0', coeficientes=b, erros_padrao=se,
        OR_horas=np.exp(b[1]), IC95_OR_Wald=ic_or,
        probabilidades_1a5=expit(b[0]+b[1]*np.arange(1, 6)))

# Uma proporção e aderência multinomial.
binomial = ler('exemplo_binomial.csv')
sucessos = sum(r['resposta'] == 'Sim' for r in binomial)
teste = stats.binomtest(sucessos, len(binomial), p=.5)
mostrar('Proporção binomial: Sim', n=len(binomial), sucessos=sucessos,
        proporcao=teste.statistic, p=teste.pvalue,
        IC95_exato=tuple(teste.proportion_ci(method='exact')))
aderencia = ler('exemplo_aderencia.csv')
chi = stats.chisquare(coluna(aderencia, 'frequencia'))
mostrar('Aderência: três proporções iguais', qui_quadrado=chi.statistic, p=chi.pvalue)

# McNemar: só os pares discordantes entram na estatística.
pares = ler('exemplo_mcnemar.csv')
tabela = {(r['antes'], r['depois']): int(r['frequencia']) for r in pares}
b, c = tabela['Sim', 'Nao'], tabela['Nao', 'Sim']
chi = (b-c)**2/(b+c)
chi_corr = (abs(b-c)-1)**2/(b+c)
mostrar('McNemar', n=sum(tabela.values()), discordantes=b+c,
        qui_quadrado=chi, p=stats.chi2.sf(chi, 1),
        qui_quadrado_corrigido=chi_corr, p_corrigido=stats.chi2.sf(chi_corr, 1),
        p_exato=stats.binomtest(b, b+c, p=.5).pvalue)
# OR da tabela independente, IC de Wald na escala logarítmica.
frequencias = ler('exemplo_frequencias.csv')
tabela = {(r['grupo'], r['resultado']): int(r['frequencia']) for r in frequencias}
a, b, c, d = (tabela[chave] for chave in [('A', 'Sim'), ('A', 'Nao'), ('B', 'Sim'), ('B', 'Nao')])
or_tabela = a*d/(b*c)
se_log_or = np.sqrt(1/a+1/b+1/c+1/d)
mostrar('OR: Sim, A versus B', OR=or_tabela,
        IC95_Wald=np.exp(np.log(or_tabela)+np.array([-1, 1])*1.96*se_log_or))
print('Cálculos concluídos. Os valores são cálculos sobre dados fictícios.')
