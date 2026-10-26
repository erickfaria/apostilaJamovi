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

O script [`scripts/calcular_exemplos.py`](../scripts/calcular_exemplos.py) lê os arquivos e calcula regressão múltipla, ANOVA fatorial, medidas repetidas, Friedman, logística, proporção binomial, aderência e McNemar. Requer Python 3, NumPy e SciPy; execute `python scripts/calcular_exemplos.py` na raiz do repositório. Não altera arquivos nem acessa a rede.

Para `exemplo_notas.csv`, o modelo múltiplo `depois ~ horas + antes`, com intercepto e 18 casos, produz coeficientes 20,502916; 3,443600; 0,663789. R² = 0,736212 e R² ajustado = 0,701040; o acréscimo de `antes` ao modelo com `horas` apresenta F(1,15) = 1,776921 e p = 0,202422. O IC95% da inclinação de `horas` é [0,102747; 6,784453].

No modelo **simples** de nota posterior em horas, a média ajustada em três horas é 65,425641. O IC95% da média é [63,002128; 67,849154], e o intervalo de predição individual de 95% é [54,937885; 75,913397], usando a variância residual e t com 16 graus de liberdade. Para a OR da tabela independente A versus B, o IC95% de Wald na escala logarítmica é [1,528844; 8,012591]. O planejamento ilustrativo de teste t independente bilateral, diferença de 5 pontos, DP comum de 10, α = 0,05 e 64 pessoas por grupo fornece poder aproximado de 0,80146 sob esse modelo.

## `exemplo_escalas.csv`

São 30 pessoas fictícias com cinco respostas de concordância, de 1 (Discordo totalmente) a 5 (Concordo totalmente). As frases sobre hábitos de estudo foram criadas somente para ensino e estão descritas no capítulo 9; não se trata de um instrumento validado.

- `id`: identificador, sem participação na pontuação.
- `item1`, `item2`, `item4`, `item5`: itens em direção favorável ao escore proposto, inteiros ordinais de 1 a 5.
- `item3_neg`: item em direção oposta; crie `item3_corr = 6 - item3_neg` antes da pontuação e da confiabilidade.

Há cinco respostas completas por pessoa. Na análise de confiabilidade, use `item1`, `item2`, `item3_corr`, `item4` e `item5`; não inclua o total ou o identificador e não inverta novamente o item já corrigido.

| Resultado | Valor aproximado |
| --- | --- |
| Primeiro registro após a correção | 4, 4, 4, 3, 4; total 19; média 3,8 |
| Média e DP amostral do total | 14,766667 e 6,229426 |
| Média e DP do escore médio | 2,953333 e 1,245885 |
| Soma das variâncias amostrais dos itens | 10,736782 |
| Variância amostral do total | 38,805747 |
| Alfa não padronizado, com item corrigido | 0,904150 |
| Alfa não padronizado sem corrigir o item invertido | 0,293636 |
| Correlação média entre pares e alfa padronizado | 0,652081 e 0,903579 |
| Correlações item–resto, itens 1 a 5 | 0,773650; 0,734611; 0,843045; 0,642355; 0,815066 |
| Alfa ao excluir cada item, 1 a 5 | 0,880797; 0,888465; 0,864474; 0,906203; 0,870681 |

A exclusão do item 4 aumenta pouco o alfa e não constitui recomendação de excluir conteúdo. As contas usam covariâncias/correlações de Pearson e os códigos numéricos dos itens; não são coeficientes baseados em correlações policóricas. O script didático `scripts/calcular_exemplos.py` também calcula esses resumos diretamente do CSV.


### `exemplo_dimensoes.csv`: componentes principais e análise fatorial

Base **inteiramente fictícia**, produzida para as atividades do capítulo 10. São 180 registros independentes construídos por simulação, sem ausentes, com oito indicadores contínuos. Os nomes planejamento e monitoramento são rótulos de ensino. Os indicadores não constituem um instrumento validado, não resultam de questionário real e não possuem interpretação diagnóstica.

| Coluna | Tipo/medida no jamovi | Descrição |
| --- | --- | --- |
| `id` | Inteiro/ID | Identificador único de 1 a 180; não incluir nas análises |
| `planejamento_1` a `planejamento_4` | Decimal/contínua | Quatro indicadores fictícios associados ao primeiro componente de geração |
| `monitoramento_1` a `monitoramento_4` | Decimal/contínua | Quatro indicadores fictícios associados ao segundo componente de geração |

**Geração reproduzível.** Utilizou-se NumPy `Generator(PCG64(20261025))`. Primeiro, foi sorteada uma matriz normal padrão 180 × 2, `B`, linha a linha. Os componentes de geração são `F1 = B[:, 0]` e `F2 = 0.35*B[:, 0] + sqrt(1 - 0.35²)*B[:, 1]`. Depois foi sorteada outra matriz normal padrão independente, `E`, 180 × 8. Para planejamento 1–4, usou-se F1; para monitoramento 1–4, F2. Os coeficientes `a` são `[.85, .80, .75, .70, .85, .80, .75, .70]`. Cada indicador é `50 + 10*(a*F + sqrt(1 - a²)*E)`, arredondado e gravado com três casas decimais. Não foram feitos recortes ou substituições para forçar resultados. O CSV foi relido antes dos cálculos.

A correlação `.35` é parâmetro de geração; ela **não** é correlação fatorial estimada. Os parâmetros de geração não devem ser apresentados como resultado de AFE do arquivo.

**Memória de cálculos do CSV** (PCA da matriz de correlações, sem rotação):

- Correlação planejamento 1 × planejamento 2: `0.64981789`.
- Correlação planejamento 1 × monitoramento 1: `0.30353337`.
- Autovalores: `3.78156122, 1.91150724, 0.52213127, 0.46763579, 0.38163977, 0.35685947, 0.30545980, 0.27320545`.
- Porcentagem nos componentes 1 e 2: `47.26951520%` e `23.89384055%`; acumulada: `71.16335575%`.
- Cargas dos dois componentes sem rotação, na ordem das colunas: `(0.72955744, 0.46288875); (0.65955941, 0.52120368); (0.67078931, 0.46752117); (0.58289972, 0.57553121); (0.73900068, -0.46831757); (0.72158247, -0.47103236); (0.69364893, -0.48647861); (0.69036661, -0.44488369)`. Os sinais foram orientados para tornar a primeira carga positiva em cada componente; inversões de sinais das colunas não alteram a solução.
- Variância do primeiro indicador representada pelos dois componentes: `0.74652006`. Não é comunalidade de uma AFE ajustada.
- KMO global da matriz: `0.8382559951`.
- Bartlett pela aproximação `-(n - 1 - (2*p+5)/6) * log(det(R))`: `686.0351899776`, gl 28, `p < .001`.

**Simulação paralela ilustrativa da figura.** Gerador independente `Generator(PCG64(20261026))`, 2.000 matrizes normais padrão de tamanho 180 × 8. Em cada uma, calcula-se a matriz de correlações e os oito autovalores ordenados do maior para o menor. Compara-se cada autovalor observado ao percentil 95 dos autovalores na mesma posição, com interpolação linear (`np.quantile(..., method='linear')`). Limites: `1.43635315, 1.27669200, 1.16945759, 1.08153755, 1.00358333, 0.93256078, 0.85988733, 0.78024100`. Apenas os dois primeiros observados excedem esses limites. Esta simulação é própria e **não** reproduz exatamente o algoritmo ou uma saída do jamovi. A análise paralela de fatores comuns pede o procedimento correspondente, não apenas esta comparação de PCA.

A AFE no jamovi é proposta como atividade com extração por resíduos mínimos e rotação oblimin. O capítulo **não apresenta valores de cargas, correlações entre fatores ou ajuste de AFE que não foram estimados**. Conservar no arquivo `.omv` as escolhas e a versão utilizada ao realizar essa atividade.

O calculador [`scripts/calcular_dimensoes.py`](../scripts/calcular_dimensoes.py) lê este CSV e refaz os números de PCA, KMO, Bartlett e a simulação paralela ilustrativa. Requer Python 3, NumPy e SciPy. Execute `python scripts/calcular_dimensoes.py`; o script apenas exibe resultados, sem alterar dados ou gerar arquivos.


## `exemplo_multinomial.csv`

São 120 registros fictícios independentes, com 24 pessoas em cada duração de uma a cinco horas. `id` é identificador, `horas_preparo` é contínua e `recurso` é nominal, com níveis Texto, Video e Oficina. Os totais são 39, 36 e 45. Não há pesos nem contagens agregadas nesse arquivo. O nível Video aparece sem acento somente no CSV.

As contagens Texto/Video/Oficina em cada duração são, respectivamente: 1 hora = 14/7/3; 2 = 10/8/6; 3 = 7/8/9; 4 = 5/7/12; 5 = 3/6/15. Os registros foram construídos a partir dessas contagens; não vieram de uma pesquisa nem de amostragem de uma população real.

Com Texto como referência e somente horas como preditor, o modelo multinomial possui quatro parâmetros:

| Comparação | Intercepto | Inclinação de horas | Multiplicador da razão por hora |
| --- | --- | --- | --- |
| Video/Texto | −0,98274825 | 0,34668051 | 1,41436478 |
| Oficina/Texto | −2,14540596 | 0,76647838 | 2,15217375 |

A log-verossimilhança é −120,99487984 e o AIC é 249,98975967. Em três horas, as probabilidades ajustadas de Texto, Video e Oficina são 0,31003029; 0,32831165; 0,36165806. A inclinação positiva de Video/Texto não obriga a probabilidade absoluta de Video a aumentar em todo o intervalo: a de Oficina também participa do denominador comum.

## `exemplo_ordinal.csv`

São outros 120 registros fictícios independentes, com `id`, `horas_preparo` e `avaliacao`. Configure `avaliacao` como **ordinal e ordene explicitamente Baixa, Media, Alta**; os totais são 37, 42 e 41. A ordem alfabética não corresponde à ordem substantiva. Cada duração tem 24 registros e as contagens Baixa/Media/Alta são: 1 hora = 14/7/3; 2 = 10/9/5; 3 = 7/10/7; 4 = 4/9/11; 5 = 2/7/15.

No modelo logístico ordinal de chances proporcionais, adotamos `logit P(Y <= j | x) = theta_j - beta*x`. Com somente horas, beta = 0,63782252, theta1 = 0,96292747 e theta2 = 2,70115220. O multiplicador comum das **chances cumulativas superiores** é exp(beta) = 1,89235583. A log-verossimilhança é −119,15968823 e o AIC é 244,31937646 (três parâmetros). Em três horas, as probabilidades de Baixa, Media e Alta são 0,27877622; 0,40855774; 0,31266604.

Não compare o AIC deste ajuste com o do arquivo multinomial: são bancos e respostas diferentes. Os IDs desses arquivos não estabelecem correspondência com os demais bancos.

O calculador didático [`scripts/calcular_categoricos.py`](../scripts/calcular_categoricos.py) lê os dois CSVs e reproduz coeficientes, probabilidades, log-verossimilhanças e AIC por máxima verossimilhança com NumPy/SciPy. Execute `python scripts/calcular_categoricos.py`; ele somente imprime resultados. Intervalos não são apresentados como valores esperados porque os métodos usados pela interface e por aproximações alternativas podem diferir.
