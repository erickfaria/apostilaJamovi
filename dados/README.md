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
