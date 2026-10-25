# Dados dos exemplos da apostila

Estes arquivos contêm **dados fictícios**, elaborados para ensino. Não representam participantes reais nem evidências sobre a eficácia de métodos de estudo. Os resultados numéricos ilustram a configuração e a leitura das análises; amostras pequenas exigem cuidado especial com pressupostos e incerteza.

Abra os CSVs no jamovi por **Arquivo → Abrir → Este PC**. O separador é vírgula e a primeira linha contém os nomes das variáveis. Verifique os tipos após importar e salve as análises em `.omv`.

## `exemplo_notas.csv`

Cada linha representa uma pessoa, com notas antes e depois de uma atividade. Cada pessoa pertence a apenas um dos três grupos; há seis pessoas por grupo e 18 no total.

| Variável | Significado | Tipo de medida no jamovi |
| --- | --- | --- |
| `id` | Identificador da pessoa | ID |
| `grupo` | Leitura, Video ou Oficina | Nominal |
| `horas` | Horas de estudo no período | Contínua |
| `antes` | Nota anterior, em pontos | Contínua |
| `depois` | Nota posterior, em pontos | Contínua |

O nível `Video` foi escrito sem acento no arquivo; na narrativa, corresponde a “Vídeo”. Não ordene as colunas `antes` e `depois` separadamente: isso desfaz os pares.

Resultados de conferência, calculados sem filtros e sem valores ausentes:

| Análise | Resultado aproximado |
| --- | --- |
| Descritiva de `depois` | n = 18; média = 64,556; DP amostral = 8,597 |
| Média de `depois` por grupo | Leitura = 59,167; Video = 64,667; Oficina = 69,833 |
| t de uma amostra de `depois`, referência 60, bilateral | t(17) = 2,248; p = 0,0381; IC95% da média [60,280; 68,831] |
| Welch de `depois`, Leitura menos Video | t(9,902) = −1,287; p = 0,2275; IC95% da diferença [−15,037; 4,037] |
| t pareado, `depois` menos `antes` | diferença média = 12,889; t(17) = 9,598; p < 0,001; IC95% [10,056; 15,722] |
| ANOVA clássica de `depois` por `grupo` | F(2, 15) = 2,799; p = 0,0927 |
| ANOVA de Welch de `depois` por `grupo` | F ≈ 2,652; p ≈ 0,1194 |
| Regressão simples de `depois` em `horas`, com intercepto | intercepto = 49,764; inclinação = 5,221; R² = 0,705 |

O sentido da diferença e do t depende da ordem dos níveis ou das medidas escolhida no jamovi. O IC exibido pelo teste de uma amostra refere-se à **diferença em relação a 60**: [0,280; 8,831]; some 60 aos limites para obter o IC da média listado acima. Welch usa graus de liberdade aproximados.

## `exemplo_frequencias.csv`

São quatro combinações de categorias que resumem **100 observações fictícias independentes**. As quatro linhas são contagens agregadas, não quatro pessoas.

Configure `grupo` e `resultado` como nominais. Na tabela de contingência, atribua `grupo` a **Linhas**, `resultado` a **Colunas** e `frequencia` a **Contagens (Counts)**. Confirme que o total é 100.

- Percentual de “Sim”: grupo A = 60%; grupo B = 30%.
- Qui-quadrado de Pearson **sem correção de continuidade**: χ²(1) = 9,091; p = 0,00257.
- Frequências esperadas: 22,5 e 27,5 em cada linha.
- V de Cramér = 0,302.
- Fisher bilateral: p ≈ 0,00464.
- Odds ratio de “Sim”, A em relação a B: 3,5. A ordem das categorias pode inverter essa razão na saída do software.

Os números foram conferidos com NumPy e SciPy, independentemente da composição do PDF. Arredondamentos e opções diferentes, como correção de continuidade, podem alterar o que aparece na saída. Os CSVs e os cálculos são de elaboração própria; as referências metodológicas estão na bibliografia da apostila.

## `exemplo_fatorial.csv`

Há 24 pessoas fictícias independentes, seis em cada combinação de dois fatores.

| Variável | Significado | Tipo |
| --- | --- | --- |
| `id` | Pessoa | ID |
| `formato` | Texto ou Video | Nominal |
| `pratica` | Nao ou Sim | Nominal |
| `pontos` | Nota, em pontos | Contínua |

As médias Texto/Nao, Texto/Sim, Video/Nao e Video/Sim são, respectivamente, 60, 64, 65 e 79. No modelo com intercepto, dois efeitos principais e interação, as somas de quadrados são 600 (formato), 486 (prática), 150 (interação) e 280 (resíduo). Como o desenho é balanceado, as decomposições usuais de tipos I, II e III coincidem para esses termos, usando uma parametrização apropriada. A interação apresenta F(1,20) = 10,714; p = 0,00380; η² parcial = 0,349. Não confunda esse modelo com duas ANOVAs separadas.

## `exemplo_medidas_repetidas.csv`

Há 12 pessoas, cada uma medida três vezes. O banco está no formato largo: **uma linha por pessoa**, sem ausentes.

| Variável | Significado | Tipo |
| --- | --- | --- |
| `id` | Pessoa | ID |
| `grupo` | Leitura ou Pratica, seis pessoas em cada | Nominal |
| `inicial`, `final`, `seguimento` | Três notas da mesma pessoa | Contínuas |

Primeiro use somente o fator intrassujeitos `Tempo`, com os três níveis nessa ordem. As médias são 53,667; 59,833; 62,333. **Sem fator entre pessoas e sem correção de esfericidade**, F(2,22) = 37,052; p < 0,001. Esse é um valor de conferência do cálculo não corrigido: a escolha do resultado a relatar depende dos diagnósticos. Acrescentar `grupo` produz outra análise, a ANOVA mista, com outro termo de erro e outros graus de liberdade. Para Friedman de um fator, χ²(2) = 20,667; p ≈ 0,0000325, pela aproximação qui-quadrado.

## `exemplo_logistica.csv`

São 60 pessoas independentes. Configure `id` como ID, `horas` como contínua e `concluiu` como nominal com dois níveis: **0 = não concluiu; 1 = concluiu**. Use 0 como referência da resposta. Cada duração de uma a cinco horas tem 12 pessoas; os totais de conclusões são 2, 4, 6, 8 e 10.

Na regressão logística com intercepto e apenas `horas`, o logit estimado é −2,320861 + 0,773620 × horas. A OR por hora é 2,168, com IC95% de Wald [1,384; 3,395]. As probabilidades ajustadas para uma a cinco horas são 0,175; 0,316; 0,500; 0,684; 0,825. São cálculos por máxima verossimilhança; não constituem validação de um modelo preditivo para uso real.

## `exemplo_binomial.csv`

Cada uma das 80 linhas corresponde a uma pessoa; 52 responderam Sim e 28, Nao. Configure `resposta` como nominal. O total amostral é 80; `id` não é peso. Para o evento Sim, a proporção é 0,65; o teste binomial exato bilateral contra 0,50 produz p ≈ 0,00968. O IC95% exato de Clopper–Pearson é aproximadamente [0,535; 0,753].

## `exemplo_aderencia.csv`

Três linhas agregam 60 observações independentes: categorias A, B e C com contagens 30, 15 e 15. Use `categoria` como nominal e `frequencia` como contagens. Contra proporções esperadas iguais a 1/3, os esperados são 20, 20 e 20: χ²(2) = 7,5; p ≈ 0,02352. Há uma variável categórica, não duas variáveis cruzadas.

## `exemplo_mcnemar.csv`

Quatro linhas agregam **60 pares antes/depois**, com as combinações Sim/Sim = 28; Sim/Nao = 4; Nao/Sim = 16; Nao/Nao = 12. Configure `antes` e `depois` como nominais e `frequencia` como contagens na tabela **pareada**. Os 20 pares discordantes informam o teste de McNemar.

- Sem correção: χ²(1) = 7,2; p ≈ 0,00729.
- Com correção de continuidade: χ²(1) = 6,05; p ≈ 0,01391.
- Binomial exato bilateral nos discordantes: p ≈ 0,01182.

Os percentuais de Sim são 32/60 = 53,33% antes e 44/60 = 73,33% depois, diferença de 20 **pontos percentuais**. O total de pessoas continua sendo 60, não 120.

## Conferência dos cálculos novos

O script [`scripts/conferir_exemplos.py`](../scripts/conferir_exemplos.py) lê os arquivos, confere a estrutura dos exemplos e recalcula regressão múltipla, ANOVA fatorial, medidas repetidas, Friedman, logística, proporção binomial, aderência e McNemar. Requer Python 3, NumPy e SciPy; execute `python scripts/conferir_exemplos.py` na raiz do repositório. Não altera arquivos nem acessa a rede.

Para `exemplo_notas.csv`, o modelo múltiplo `depois ~ horas + antes`, com intercepto e 18 casos, produz coeficientes 20,502916; 3,443600; 0,663789. R² = 0,736212 e R² ajustado = 0,701040; o acréscimo de `antes` ao modelo com `horas` apresenta F(1,15) = 1,776921 e p = 0,202422. O IC95% da inclinação de `horas` é [0,102747; 6,784453].

No modelo **simples** de nota posterior em horas, a média ajustada em três horas é 65,425641. O IC95% da média é [63,002128; 67,849154], e o intervalo de predição individual de 95% é [54,937885; 75,913397], usando a variância residual e t com 16 graus de liberdade. Para a OR da tabela independente A versus B, o IC95% de Wald na escala logarítmica é [1,528844; 8,012591]. O planejamento ilustrativo de teste t independente bilateral, diferença de 5 pontos, DP comum de 10, α = 0,05 e 64 pessoas por grupo fornece poder aproximado de 0,80146 sob esse modelo.
