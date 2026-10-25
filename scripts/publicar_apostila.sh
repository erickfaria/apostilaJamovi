#!/usr/bin/env bash
# Executado pelo job de publicação, depois de baixar o PDF compilado.
set -euo pipefail

: "${SOURCE_SHA:?Informe o commit dos fontes que geraram o PDF.}"

# Uma execução antiga nunca publica sobre fontes mais novos.
if [ "$(git rev-parse HEAD)" != "$SOURCE_SHA" ]; then
  echo 'A main recebeu outro commit; a execução mais recente fará a publicação.'
  exit 0
fi

versao_apostila="$(< VERSION)"
if [[ ! "$versao_apostila" =~ ^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$ ]]; then
  echo 'VERSION deve conter MAIOR.MENOR.CORREÇÃO, por exemplo 1.1.0.' >&2
  exit 1
fi
tag_apostila="v${versao_apostila}"

# O checkout do job traz o histórico e as tags para esta conferência.
if git show-ref --verify --quiet "refs/tags/$tag_apostila"; then
  if ! git merge-base --is-ancestor "$tag_apostila^{commit}" HEAD; then
    echo "A tag $tag_apostila pertence a outro histórico; use uma nova versão." >&2
    exit 1
  fi
fi

git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git add -- apostila_jamovi.pdf
if git diff --cached --quiet; then
  echo 'O PDF já está atualizado.'
else
  git commit -m 'docs: atualiza o PDF da apostila automaticamente'
fi

# Uma edição já publicada nunca recebe outra posição de tag.
if git show-ref --verify --quiet "refs/tags/$tag_apostila"; then
  echo "A tag $tag_apostila já existe e será preservada."
  git push origin HEAD:main
else
  git tag --annotate "$tag_apostila" --message "Apostila de jamovi $tag_apostila: fontes e PDF compilado."
  # Sem force, e tudo ou nada: PDF e tag precisam ser publicados juntos.
  git push --atomic origin HEAD:main "refs/tags/$tag_apostila"
fi
