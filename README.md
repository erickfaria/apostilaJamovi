# Apostila de jamovi em português

Uma apostila para aprender a organizar dados, escolher análises e interpretar resultados no jamovi. O material combina explicações, exemplos guiados e exercícios comentados, com escrita voltada ao estudo e referências oficiais verificáveis.

**[Ler o PDF](https://github.com/erickfaria/apostilaJamovi/blob/main/apostila_jamovi.pdf)** · **[Baixar o PDF](https://raw.githubusercontent.com/erickfaria/apostilaJamovi/main/apostila_jamovi.pdf)** · **[Versões da apostila](https://github.com/erickfaria/apostilaJamovi/tags)** · **[Histórico de alterações](CHANGELOG.md)** · **[Usar e adaptar](docs/LICENCIAMENTO.md)** · **[Contribuir](CONTRIBUTING.md)**

O jamovi é um software estatístico livre e de código aberto. Consulte o [site oficial](https://www.jamovi.org/) para instalação e acesso e a [documentação oficial](https://docs.jamovi.org/) para os recursos da versão utilizada.

## Feita para ajudar e ser usada

Criei esta apostila para ajudar as pessoas a aprender estatística e análise de dados com o jamovi. Quero que ela seja útil em sala de aula, em cursos, em grupos de estudo e para quem aprende por conta própria.

**Professoras e professores podem adotar a apostila inteira ou selecionar apenas o que fizer sentido para suas turmas.** Você pode imprimir, distribuir, retirar capítulos, mudar a ordem, reescrever explicações, traduzir, acrescentar atividades e publicar uma adaptação. Pode também usar e alterar os fontes LaTeX/TikZ e os scripts. Não precisa pedir autorização prévia nem contribuir de volta para usar o material.

O conteúdo e os fontes da apostila usam **CC BY 4.0**, com crédito e indicação das mudanças; os scripts e workflows usam **MIT**, preservando os avisos dessa licença. Ambas permitem uso comercial. Veja os exemplos de créditos e o escopo de cada licença no [guia de uso e adaptação](docs/LICENCIAMENTO.md).

## Conteúdo

| Capítulo | O que vamos estudar |
| --- | --- |
| 1. Introdução | Instalação, primeiros passos, módulos, Rj, acessibilidade e organização de projetos |
| 2. Manipulação de dados | Tipos de variáveis, organização, transformações, filtros, valores ausentes e exportação |
| 3. Estatística descritiva | Frequências, posição e dispersão, quantis, acumulada empírica, boxplot, Q–Q e densidade |
| 4. Testes de hipóteses | Valor de p, intervalos, testes t, efeitos padronizados, equivalência, não paramétricos e planejamento |
| 5. ANOVA | Um fator, contrastes, interação fatorial, medidas repetidas, desenho misto, ANCOVA, Kruskal–Wallis e Friedman |
| 6. Regressão linear | Modelos simples e múltiplos, fatores, interações, diagnósticos e intervalos de média e predição |
| 7. Dados categóricos | Tabelas, proporções, aderência, McNemar e regressão logística binária |
| 8. Probabilidade, amostragem e estimação | Probabilidades condicionais, binomial, normal, distribuição amostral, viés, intervalos e bootstrap no Rj |
| 9. Escores e confiabilidade | Itens invertidos, pontuação, alfa, item–resto, fundamentos do ômega e erro de medida |
| 10. Dimensões | PCA e AFE, matriz de correlações, autovalores, retenção, rotação, cargas, comunalidades, KMO e Bartlett |
| 11. Regressões multinomial e ordinal | Categoria de referência, logits, probabilidades, limiares, chances proporcionais e interpretação |
| 12. Projetos integradores | Notas e modelos, escores e dimensões, descrição documentada do CNES e entregáveis |

A intenção é ampliar continuamente o material em língua portuguesa. Modelos lineares mistos, análise fatorial confirmatória e modelos para amostragem complexa seguem como possibilidades de aprofundamento; os capítulos atuais explicam os limites dos procedimentos apresentados.

## Como acompanhar os exemplos

1. Baixe o PDF e abra o jamovi.
2. Escolha um dos arquivos da pasta [`dados`](dados/README.md), seguindo o capítulo.
3. Consulte o dicionário para conferir o que cada linha representa, os tipos das variáveis e as opções da análise.
4. Salve seu trabalho em `.omv` e escreva sua interpretação antes de consultar os comentários dos exercícios.

Há **12 CSVs fictícios**. Eles distinguem pessoas independentes, medidas repetidas e contagens agregadas; não representam resultados de pesquisas reais.

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
| [`exemplo_escalas.csv`](dados/exemplo_escalas.csv) | Recodificação de itens, escores e consistência interna |
| [`exemplo_dimensoes.csv`](dados/exemplo_dimensoes.csv) | Oito indicadores contínuos, PCA e atividade de AFE |
| [`exemplo_multinomial.csv`](dados/exemplo_multinomial.csv) | Resposta nominal de três categorias e probabilidades |
| [`exemplo_ordinal.csv`](dados/exemplo_ordinal.csv) | Resposta ordenada e chances proporcionais |

Os 12 capítulos incluem **68 exercícios comentados** e **45 figuras em TikZ/PGFPlots**, com fórmulas e explicações. A revisão 1.3.0 acrescenta 26 dessas figuras e 40 exercícios, além de aprofundar os capítulos anteriores. Os cálculos dos exemplos podem ser reproduzidos com Python 3, NumPy e SciPy:

```bash
python scripts/calcular_exemplos.py
python scripts/calcular_dimensoes.py
python scripts/calcular_categoricos.py
```

Esses scripts são calculadores didáticos: leem os CSVs e exibem os resultados, sem modificar os dados nem acessar a rede. O [dicionário](dados/README.md) registra as opções, a construção dos bancos e os valores esperados. O repositório não mantém suíte de testes automatizados.

## Referências e materiais complementares

As referências estão em [`bibliografia.bib`](bibliografia.bib), com URLs e datas de consulta para fontes da web. O texto utiliza documentação oficial do jamovi, do R e do pacote psych, o manual NIST/SEMATECH e a declaração da American Statistical Association sobre valores de p. O capítulo de questionários também remete aos Standards de AERA, APA e NCME e ao artigo original de Cronbach. A discussão de calibração remete à documentação oficial do scikit-learn.

As figuras explicativas novas são de elaboração própria em TikZ/PGFPlots. As capturas anteriores foram preservadas com indicação de que a interface pode ter mudado.

- [Página da apostila no Balaio Científico](https://www.balaiocientifico.com/2022/11/apostila-de-jamovi.html).
- [Sobre o Balaio Científico](https://www.balaiocientifico.com/p/sobre-o-balaio-cientifico.html).
- [Videoaulas no YouTube](https://www.youtube.com/channel/UCzHAqwm3RSDM-YKdxd4XYTg).
- [Playlist de jamovi](https://www.youtube.com/playlist?list=PL9yRFhroUHDAC_XfMQH7mRiHshp63qI1B).
- [Trilhas por capítulo: blog, vídeo e prática](docs/trilhas-balaio.md).

Cada capítulo conecta a leitura a posts e vídeos do Balaio Científico, com atividades próprias da apostila. Os links e metadados selecionados foram conferidos em 25/10/2026. Posts e videoaulas podem usar outros bancos ou versões do programa; consulte as fontes oficiais para os métodos e as opções da versão utilizada. A edição web e o PDF podem receber revisões em momentos diferentes.

## Versões da apostila

O arquivo [`VERSION`](VERSION) identifica a edição em preparação; [`CHANGELOG.md`](CHANGELOG.md) registra suas alterações. As tags são anotadas e seguem `vMAIOR.MENOR.CORREÇÃO`:

- **MAIOR:** reorganizações amplas da estrutura e do percurso de estudo.
- **MENOR:** novos temas ou ampliações de conteúdo.
- **CORREÇÃO:** ajustes de texto, cálculos, referências ou links.

As edições de `v1.0.0` a `v1.3.0` estão publicadas. A edição em preparação, `v1.3.1`, explicita as licenças, as liberdades de adoção e adaptação e as orientações para contribuir. Sua tag será criada automaticamente quando o novo PDF for publicado pelo Actions.

Para consultar uma edição fixa, abra a [lista de tags](https://github.com/erickfaria/apostilaJamovi/tags), selecione a versão e acesse `apostila_jamovi.pdf`. Cada tag inclui os fontes e o PDF daquela edição. A versão da `main` continua sendo atualizada no mesmo endereço público.

## Como contribuir

Correções de texto ou cálculo, sugestões, novos exemplos e relatos de uso em cursos são bem-vindos. Você pode abrir uma [issue](https://github.com/erickfaria/apostilaJamovi/issues/new/choose) mesmo sem conhecer LaTeX ou Git.

O [guia de contribuição](CONTRIBUTING.md) explica onde editar, como enviar um PR e os cuidados didáticos com fórmulas, figuras, dados e referências. O projeto trabalha com branches descritivas, commits pequenos e remoção das branches incorporadas. O template é preservado e o PDF é publicado pela automação.

Para adotar ou adaptar a apostila, consulte o [guia de uso e licenças](docs/LICENCIAMENTO.md). Para referenciar uma edição em aulas e trabalhos, veja [como citar](CITATION.md).

## Compilação e publicação automática

O [workflow da apostila](.github/workflows/compilar-apostila.yml) usa pdfLaTeX e Biber com TeX Live 2026. Ele compila os fontes em PRs para `main` e disponibiliza o PDF como artefato `apostila-jamovi` por sete dias.

Após a integração à `main`, o Actions compila novamente e atualiza apenas `apostila_jamovi.pdf` na raiz. Se a versão de `VERSION` ainda não tiver tag, publica uma tag anotada **no commit que contém o PDF compilado**. Tags existentes são preservadas; novas edições devem receber novos números.

Assim, os links de leitura e download continuam os mesmos. Se a compilação falhar, o PDF anteriormente publicado permanece disponível e a nova tag não é criada. PRs e branches de trabalho não publicam na `main`.

Também é possível recompilar em **Actions → Compilar apostila → Run workflow**, selecionando `main`. Alterações apenas em Markdown ou no próprio PDF não disparam compilação automática; alterar `VERSION` dispara. O workflow usa o `GITHUB_TOKEN` do repositório.

## Autoria e licença

Material de **Erick Faria — Balaio Científico**, criado para ajudar as pessoas a aprender e compartilhar conhecimento.

| Parte do repositório | Licença |
| --- | --- |
| Conteúdo e PDF; fontes LaTeX/TikZ; documentação, dados fictícios e figuras originais | [CC BY 4.0](LICENSE) |
| Scripts Python/shell e workflows de automação | [MIT](scripts/LICENSE) |

Você pode compartilhar e adaptar o conteúdo, inclusive para uso comercial, com os créditos e avisos aplicáveis, um link para a licença e indicação das mudanças. A CC BY não exige que a adaptação use a mesma licença. Para os scripts, mantenha o aviso de copyright e o texto da MIT ao redistribuir cópias ou partes substanciais.

O [guia de licenciamento](docs/LICENCIAMENTO.md) detalha as permissões e oferece um modelo de crédito. Materiais de terceiros identificados no projeto conservam seus próprios direitos e condições.
