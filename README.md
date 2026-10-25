# Apostila de jamovi em português

Uma apostila para aprender a organizar dados, escolher análises e interpretar resultados no jamovi. O material combina explicações, exemplos guiados e exercícios comentados, com escrita voltada ao estudo e referências oficiais verificáveis.

**[Ler o PDF](https://github.com/erickfaria/apostilaJamovi/blob/main/apostila_jamovi.pdf)** · **[Baixar o PDF](https://raw.githubusercontent.com/erickfaria/apostilaJamovi/main/apostila_jamovi.pdf)** · **[Versões da apostila](https://github.com/erickfaria/apostilaJamovi/tags)** · **[Histórico de alterações](CHANGELOG.md)**

O jamovi é um software estatístico livre e de código aberto. Consulte o [site oficial](https://www.jamovi.org/) para instalação e acesso e a [documentação oficial](https://docs.jamovi.org/) para os recursos da versão utilizada.

## Conteúdo

| Capítulo | O que vamos estudar |
| --- | --- |
| 1. Introdução | Instalação, primeiros passos, módulos, Rj e roteiro de estudo |
| 2. Manipulação de dados | Tipos de variáveis, organização, transformações, filtros, valores ausentes e exportação |
| 3. Estatística descritiva | Frequências, medidas de posição e dispersão, gráficos e interpretação |
| 4. Testes de hipóteses | Valor de p, intervalos, testes t, Mann–Whitney, Wilcoxon, planejamento amostral e multiplicidade |
| 5. ANOVA | Um fator, contrastes, interação fatorial, medidas repetidas, desenho misto, ANCOVA, Kruskal–Wallis e Friedman |
| 6. Regressão linear | Modelos simples e múltiplos, fatores, interações, diagnósticos e intervalos de média e predição |
| 7. Dados categóricos | Tabelas, proporções, aderência, McNemar e regressão logística binária |

A intenção é ampliar continuamente o material em língua portuguesa. Modelos lineares mistos, regressões ordinal e multinomial, análise fatorial e confiabilidade de escalas ainda precisam de tratamento próprio.

## Como acompanhar os exemplos

1. Baixe o PDF e abra o jamovi.
2. Escolha um dos arquivos da pasta [`dados`](dados/README.md), seguindo o capítulo.
3. Consulte o dicionário para conferir o que cada linha representa, os tipos das variáveis e as opções da análise.
4. Salve seu trabalho em `.omv` e escreva sua interpretação antes de consultar os comentários dos exercícios.

Há **oito CSVs fictícios**. Eles distinguem pessoas independentes, medidas repetidas e contagens agregadas; não representam resultados de pesquisas reais.

| Arquivo | Uso principal |
| --- | --- |
| [`exemplo_notas.csv`](dados/exemplo_notas.csv) | Descritivas, testes t, ANOVA de um fator e regressão linear |
| [`exemplo_frequencias.csv`](dados/exemplo_frequencias.csv) | Associação em tabela de contingência |
| [`exemplo_fatorial.csv`](dados/exemplo_fatorial.csv) | Dois fatores e interação |
| [`exemplo_medidas_repetidas.csv`](dados/exemplo_medidas_repetidas.csv) | Tempo, medidas repetidas e desenho misto |
| [`exemplo_logistica.csv`](dados/exemplo_logistica.csv) | Regressão logística binária |
| [`exemplo_binomial.csv`](dados/exemplo_binomial.csv) | Uma proporção |
| [`exemplo_aderencia.csv`](dados/exemplo_aderencia.csv) | Proporções de várias categorias |
| [`exemplo_mcnemar.csv`](dados/exemplo_mcnemar.csv) | Respostas binárias pareadas |

Os capítulos 4 a 7 incluem **16 exercícios comentados**. Os cálculos novos podem ser reproduzidos com Python 3, NumPy e SciPy:

```bash
python scripts/calcular_exemplos.py
```

O script lê os CSVs e exibe os resultados, sem modificar os dados nem acessar a rede. O [dicionário](dados/README.md) registra as opções e os valores esperados.

## Referências e materiais complementares

As referências estão em [`bibliografia.bib`](bibliografia.bib), com URLs e datas de consulta para fontes da web. O texto utiliza documentação oficial do jamovi e do R, o manual NIST/SEMATECH e a declaração da American Statistical Association sobre valores de p. A discussão de calibração remete à documentação oficial do scikit-learn.

As figuras explicativas novas são de elaboração própria em TikZ/PGFPlots. As capturas anteriores foram preservadas com indicação de que a interface pode ter mudado.

- [Página da apostila no Balaio Científico](https://www.balaiocientifico.com/2022/11/apostila-de-jamovi.html).
- [Sobre o Balaio Científico](https://www.balaiocientifico.com/p/sobre-o-balaio-cientifico.html).
- [Videoaulas no YouTube](https://www.youtube.com/@BalaioCientifico).

A edição web e o PDF podem receber revisões em momentos diferentes. Confira a data de atualização de cada material.

## Versões da apostila

O arquivo [`VERSION`](VERSION) identifica a edição em preparação; [`CHANGELOG.md`](CHANGELOG.md) registra suas alterações. As tags são anotadas e seguem `vMAIOR.MENOR.CORREÇÃO`:

- **MAIOR:** reorganizações amplas da estrutura e do percurso de estudo.
- **MENOR:** novos temas ou ampliações de conteúdo.
- **CORREÇÃO:** ajustes de texto, cálculos, referências ou links.

A `v1.0.0` identifica a revisão anterior já compilada. A `v1.1.0` identifica a ampliação dos capítulos finais e será marcada automaticamente quando seu PDF for publicado pelo Actions.

Para consultar uma edição fixa, abra a [lista de tags](https://github.com/erickfaria/apostilaJamovi/tags), selecione a versão e acesse `apostila_jamovi.pdf`. Cada tag inclui os fontes e o PDF daquela edição. A versão da `main` continua sendo atualizada no mesmo endereço público.

## Como contribuir

Correções, sugestões e novos exemplos são bem-vindos. Abra uma issue ou um pull request e indique o capítulo, a pergunta e as fontes usadas.

O fluxo de trabalho é:

1. Atualizar a `main` e criar uma branch com nome descritivo, como `conteudo/novo-tema` ou `docs/corrigir-referencia`.
2. Fazer commits pequenos e manter o tom didático e colaborativo. Preservar o template e citar fontes oficiais quando cabível.
3. Conferir os exemplos, atualizar o README quando o conteúdo mudar e registrar a edição em `VERSION` e `CHANGELOG.md` quando houver uma nova versão.
4. Abrir um PR para `main`. Depois da integração, sincronizar a cópia local e apagar as branches incorporadas.

## Compilação e publicação automática

O [workflow da apostila](.github/workflows/compilar-apostila.yml) usa pdfLaTeX e Biber com TeX Live 2026. Ele compila os fontes em PRs para `main` e disponibiliza o PDF como artefato `apostila-jamovi` por sete dias.

Após a integração à `main`, o Actions compila novamente e atualiza apenas `apostila_jamovi.pdf` na raiz. Se a versão de `VERSION` ainda não tiver tag, publica uma tag anotada **no commit que contém o PDF compilado**. Tags existentes são preservadas; novas edições devem receber novos números.

Assim, os links de leitura e download continuam os mesmos. Se a compilação falhar, o PDF anteriormente publicado permanece disponível e a nova tag não é criada. PRs e branches de trabalho não publicam na `main`.

Também é possível recompilar em **Actions → Compilar apostila → Run workflow**, selecionando `main`. Alterações apenas em Markdown ou no próprio PDF não disparam compilação automática; alterar `VERSION` dispara. O workflow usa o `GITHUB_TOKEN` do repositório.

## Autoria e licença

Material de **Erick Faria**, do Balaio Científico, sob a licença [Creative Commons Atribuição 4.0 Internacional — CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt_BR). Ao compartilhar ou adaptar, atribua a autoria e indique as modificações.
