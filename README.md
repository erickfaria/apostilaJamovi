# Introdução ao Jamovi

## Sobre o Jamovi

O Jamovi é um software livre e de código aberto que oferece uma ampla gama de recursos estatísticos e de análise de dados. Ele foi projetado para ser intuitivo, acessível e eficiente, permitindo que usuários de diferentes níveis de experiência possam realizar análises estatísticas de forma eficaz.

## Sobre a Apostila

Esta apostila foi criada com o objetivo de fornecer um guia prático e abrangente para aqueles que desejam aprender a utilizar o Jamovi para análise estatística. Ela abrange desde conceitos básicos até técnicas mais avançadas, tudo apresentado de forma clara e concisa.

### Conteúdo

A apostila está organizada em capítulos, abordando os seguintes tópicos:

1. Introdução ao Jamovi
2. Manipulação de Dados no Jamovi
3. Estatística Descritiva
4. Testes de hipóteses: testes t, Mann–Whitney, Wilcoxon, planejamento amostral e multiplicidade
5. ANOVA: um fator, contrastes, interação fatorial, medidas repetidas, desenho misto, ANCOVA, Kruskal–Wallis e Friedman
6. Regressão linear: modelos simples e múltiplos, fatores, interações, diagnósticos e intervalos
7. Dados categóricos: tabelas, proporções, aderência, McNemar e regressão logística binária

Cada capítulo apresenta uma combinação de explicações teóricas e exemplos práticos, com a demonstração passo a passo de como realizar as análises estatísticas utilizando o Jamovi.

### Exemplos e referências

A pasta [`dados`](dados/README.md) contém oito CSVs fictícios, o dicionário das variáveis e resultados de conferência. Os exemplos distinguem pessoas independentes, medidas repetidas e contagens agregadas. Há exercícios com comentários nos capítulos 4 a 7 e um roteiro de estudo no capítulo inicial. As bases não representam resultados de pesquisas reais.

Os capítulos usam documentação oficial do jamovi e do R, o manual NIST/SEMATECH e a declaração da American Statistical Association sobre valores de p. A discussão de calibração remete à documentação oficial do scikit-learn. As referências da web incluem URLs e datas de consulta em `bibliografia.bib`; as figuras novas usam TikZ/PGFPlots e são identificadas como elaboração própria. As capturas anteriores foram preservadas como ilustrações, com indicação de que a interface pode ter mudado.

O script [`scripts/conferir_exemplos.py`](scripts/conferir_exemplos.py), com NumPy e SciPy, recalcula os novos exemplos diretamente dos CSVs, incluindo coeficientes, intervalos e estatísticas de teste. Ele não depende de uma compilação do PDF. Veja o dicionário para o comando e as opções que definem cada resultado.

A expansão atual desenvolve os capítulos de inferência e modelos. Modelos lineares mistos, regressões ordinal e multinomial, análise fatorial e confiabilidade de escalas ainda precisam de tratamento próprio; as menções a esses caminhos não equivalem a capítulos completos sobre eles.

### Balaio Científico

A [página atual da apostila](https://www.balaiocientifico.com/2022/11/apostila-de-jamovi.html) reúne o acesso à edição web e aos materiais complementares. A [página sobre o Balaio](https://www.balaiocientifico.com/p/sobre-o-balaio-cientifico.html) substitui o endereço antigo de autor nos links da apostila. O PDF e a edição web podem ser revisados em momentos diferentes; confira a data de cada edição.

### Como Utilizar

- Faça o download do repositório ou clone-o em sua máquina local.
- Caso prefira, você também pode fazer o download da apostila completa em formato PDF para estudar offline.
- Você também pode acessar a [versão atualizada da apostila no GitHub](https://github.com/erickfaria/apostilaJamovi/blob/main/apostila_jamovi.pdf).

### Contribuições

Este repositório está aberto a contribuições. Se você encontrar erros, tiver sugestões de melhoria ou desejar adicionar mais conteúdo relevante, sinta-se à vontade para enviar uma solicitação de pull. Seu feedback é valioso e ajudará a aprimorar ainda mais esta apostila.

### Compilação e atualização automática do PDF

As alterações na apostila devem ser feitas em uma branch e enviadas por pull request para `main`. O GitHub Actions compila `apostila_jamovi.tex` com pdfLaTeX e Biber, usando TeX Live 2026, para verificar os fontes antes da integração. O PDF de cada compilação fica disponível como artefato `apostila-jamovi` na execução do workflow por sete dias.

Ao integrar as alterações à `main`, o workflow compila novamente e faz um commit automático apenas de `apostila_jamovi.pdf`, na raiz do repositório. Assim, o PDF continua no mesmo caminho e os links que apontam para esse arquivo na `main` continuam válidos:

- [Visualizar o PDF no GitHub](https://github.com/erickfaria/apostilaJamovi/blob/main/apostila_jamovi.pdf)
- [Baixar o PDF diretamente](https://raw.githubusercontent.com/erickfaria/apostilaJamovi/main/apostila_jamovi.pdf)

Também é possível recompilar manualmente em **Actions → Compilar apostila → Run workflow**, selecionando `main`. Alterações apenas em arquivos Markdown ou no próprio PDF não disparam a compilação automática. Se a compilação falhar, o PDF publicado anteriormente permanece disponível. Execuções de pull requests ou de outras branches nunca publicam na `main`.

O workflow usa o `GITHUB_TOKEN` do próprio repositório, sem necessidade de cadastrar tokens adicionais. A etapa de publicação precisa de permissão de escrita em `contents`; se futuramente forem criadas regras de proteção para `main`, elas precisarão permitir o commit automático do PDF.



