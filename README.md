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
4. Testes de Hipóteses
5. Análise de Variância (ANOVA)
6. Regressão Linear
7. Análise de Dados Categóricos

Cada capítulo apresenta uma combinação de explicações teóricas e exemplos práticos, com a demonstração passo a passo de como realizar as análises estatísticas utilizando o Jamovi.

### Exemplos e referências

A pasta [`dados`](dados/README.md) contém dois CSVs fictícios, o dicionário das variáveis e os resultados esperados dos exercícios. `exemplo_notas.csv` é usado nas descritivas, testes t, ANOVA e regressão; `exemplo_frequencias.csv` contém contagens agregadas para a análise de dados categóricos. Os exemplos são de elaboração própria e não representam resultados de pesquisas reais.

Os capítulos revisados usam a documentação oficial do jamovi, o manual NIST/SEMATECH e a declaração da American Statistical Association sobre valores de p. As referências da web incluem URLs e datas de consulta em `bibliografia.bib`; as figuras explicativas são feitas em TikZ/PGFPlots e identificadas como elaboração própria. As capturas anteriores foram preservadas como ilustrações, com indicação de que a interface pode ter mudado.

### Como Utilizar

- Faça o download do repositório ou clone-o em sua máquina local.
- Caso prefira, você também pode fazer o download da apostila completa em formato PDF para estudar offline.
- Você também pode acessar a apostila online no seguinte link: [Apostila do Jamovi](https://www.balaiocientifico.com/jamovi/apostila-de-jamovi/).

### Contribuições

Este repositório está aberto a contribuições. Se você encontrar erros, tiver sugestões de melhoria ou desejar adicionar mais conteúdo relevante, sinta-se à vontade para enviar uma solicitação de pull. Seu feedback é valioso e ajudará a aprimorar ainda mais esta apostila.

### Compilação e atualização automática do PDF

As alterações na apostila devem ser feitas em uma branch e enviadas por pull request para `main`. O GitHub Actions compila `apostila_jamovi.tex` com pdfLaTeX e Biber, usando TeX Live 2026, para verificar os fontes antes da integração. O PDF de cada compilação fica disponível como artefato `apostila-jamovi` na execução do workflow por sete dias.

Ao integrar as alterações à `main`, o workflow compila novamente e faz um commit automático apenas de `apostila_jamovi.pdf`, na raiz do repositório. Assim, o PDF continua no mesmo caminho e os links que apontam para esse arquivo na `main` continuam válidos:

- [Visualizar o PDF no GitHub](https://github.com/erickfaria/apostilaJamovi/blob/main/apostila_jamovi.pdf)
- [Baixar o PDF diretamente](https://raw.githubusercontent.com/erickfaria/apostilaJamovi/main/apostila_jamovi.pdf)

Também é possível recompilar manualmente em **Actions → Compilar apostila → Run workflow**, selecionando `main`. Alterações apenas em arquivos Markdown ou no próprio PDF não disparam a compilação automática. Se a compilação falhar, o PDF publicado anteriormente permanece disponível. Execuções de pull requests ou de outras branches nunca publicam na `main`.

O workflow usa o `GITHUB_TOKEN` do próprio repositório, sem necessidade de cadastrar tokens adicionais. A etapa de publicação precisa de permissão de escrita em `contents`; se futuramente forem criadas regras de proteção para `main`, elas precisarão permitir o commit automático do PDF.



