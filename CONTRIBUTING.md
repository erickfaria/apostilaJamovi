# Vamos melhorar a apostila juntos

Esta apostila foi criada por Erick Faria, do Balaio Científico, para ajudar pessoas a aprender estatística e análise de dados com o jamovi. Professores, estudantes e demais leitores são bem-vindos para corrigir, sugerir, ampliar e adaptar o material.

Você não precisa saber LaTeX ou Git para ajudar. Uma explicação que ficou confusa, um link quebrado ou uma conta que merece conferência já são boas contribuições.

## Quero usar a apostila na minha turma

Pode usar a apostila inteira ou selecionar partes, retirar capítulos, reorganizar o conteúdo e acrescentar exemplos. Consulte o [guia de uso e licenças](docs/LICENCIAMENTO.md) para os créditos e as permissões. Adotar ou adaptar a apostila não depende de abrir uma issue, enviar suas mudanças ou obter aprovação do projeto.

## Quero sugerir ou apontar uma correção

Abra uma [issue](https://github.com/erickfaria/apostilaJamovi/issues/new/choose). Há modelos para correções e sugestões de conteúdo; você também pode escrever livremente.

Conte qual capítulo ou seção está discutindo e, se possível, a versão da apostila. Para um erro, indique o trecho, o problema e sua proposta de correção. Para uma sugestão, descreva a pergunta que o novo conteúdo ajudaria a responder. Inclua fontes oficiais ou publicações originais quando a questão envolver método, interpretação ou uma opção do jamovi.

Se o problema estiver na interface ou no resultado de uma análise, informe a versão do jamovi, as opções selecionadas e um exemplo pequeno que permita compreender a situação. Use dados fictícios ou compartilháveis, sem informações pessoais.

## Quero enviar uma alteração nos arquivos

1. Faça um fork, atualize sua cópia a partir da `main` e crie uma branch com nome descritivo, como `docs/correcao-mediana` ou `conteudo/exemplo-regressao`.
2. Faça alterações focadas e commits pequenos, com mensagens que expliquem a mudança.
3. Confira texto, contas, links e referências afetados. Descreva no PR como fez essa conferência.
4. Abra um pull request para a `main`, explicando a contribuição e sua finalidade. Uma issue anterior é útil para propostas amplas, mas não é exigida para uma correção pequena.

Depois da integração, a branch incorporada pode ser apagada. A publicação do PDF é automática pelo Actions; preserve esse fluxo.

## Onde editar

| Arquivo ou pasta | Conteúdo |
| --- | --- |
| `capitulos/` | Texto LaTeX e figuras TikZ dos capítulos |
| `apostila_jamovi.tex` | Documento principal e inclusão dos capítulos |
| `bibliografia.bib` | Referências e endereços das fontes |
| `dados/` e `dados/README.md` | Bases didáticas, dicionários e valores de referência |
| `imagens/` | Imagens utilizadas no documento |
| `scripts/` | Cálculos didáticos e publicação da apostila |
| `docs/` | Trilhas do Balaio Científico e orientações de uso |
| `README.md`, `VERSION`, `CHANGELOG.md` | Guia do repositório e histórico das edições |

## Como escrever para esta apostila

- Mantenha o português claro, o tom de apostila e a abordagem colaborativa. Apresente a pergunta antes do procedimento e interprete os resultados nas unidades do exemplo.
- Preserve o template. Use TikZ/PGFPlots para diagramas e figuras explicativas quando ajudarem a compreender a ideia; identifique o que é esquema e o que foi calculado de um banco.
- Defina símbolos, denominadores e condições das fórmulas. Diferencie associação, previsão e causalidade; explicite os limites do exemplo.
- Priorize documentação oficial do jamovi, R e pacotes usados, além de fontes metodológicas originais. Registre URL, autoria e data de consulta na bibliografia quando cabível.
- Use os posts e vídeos do Balaio Científico como material complementar pertinente ao tema, conferindo os endereços e o assunto efetivo de cada recurso.
- Identifique dados fictícios, explique o significado de cada linha e atualize o dicionário quando alterar um exemplo. Confira as contas e mantenha as opções necessárias para reproduzi-las.
- Respeite as licenças de imagens, trechos e dados de terceiros; indique fonte e condições de reutilização.

## Conferência e compilação

Uma correção textual pode ser conferida por leitura e pelo diff. Quando mudar números, fórmulas ou análises, confira os cálculos e registre dados e opções. Os scripts de `scripts/` são calculadores didáticos, não uma suíte de testes. Este repositório não mantém testes automatizados; não acrescente uma suíte como requisito para uma contribuição editorial.

Para compilar localmente, use uma instalação de TeX Live com pdfLaTeX, Biber e os pacotes do documento. A partir da raiz:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error apostila_jamovi.tex
```

O Actions também compila os fontes dos PRs. Depois da integração à `main`, ele publica o PDF no endereço existente e cria a tag de uma edição ainda não publicada. Envie os fontes; deixe a atualização do PDF publicado a cargo da automação. Ajustes de `VERSION` e do histórico são combinados na revisão da edição.

## Licenças das contribuições

Ao enviar uma contribuição, você concorda em disponibilizar o material que criou sob a licença aplicável à parte alterada: **CC BY 4.0 para conteúdo e fontes da apostila; MIT para scripts e workflows**, conforme o [guia de licenciamento](docs/LICENCIAMENTO.md). Você mantém sua autoria; não há cessão de direitos autorais ao mantenedor. Se incorporar material de outra origem, informe a licença e a fonte para avaliar a compatibilidade antes de integrá-lo.

As orientações editoriais desta página servem para colaborar neste repositório. As liberdades para usar sua própria cópia ou publicar uma adaptação são as das licenças, sem obrigação de contribuir de volta.

Nas discussões, trate as pessoas com respeito, explique as divergências com clareza e concentre as críticas no conteúdo. Toda contribuição pode ajudar alguém a aprender melhor.
