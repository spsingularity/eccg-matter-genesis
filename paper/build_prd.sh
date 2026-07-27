#!/usr/bin/env bash
# Build the Physical Review D PDF (revtex4-2) for Paper VII from ECCG_matter_genesis.md.
#   makedoc (title/abstract/keywords -> YAML, fold figures, number sections)
#   -> pandoc --natbib with template_prd.tex -> xelatex + bibtex.
set -e
cd "$(dirname "$0")"
mkdir -p tex
BASE=ECCG_matter_genesis

python3 tools/makedoc.py $BASE.md .build.md
trap 'rm -f .build.md' EXIT
# (a) drop the citeproc "## References / ::: {#refs}" placeholder if present
# (b) protect native inline $...$ math as raw-LaTeX spans so pandoc's "$5" heuristic
#     does not swallow notation like $\sim$30 / $3\to2$
python3 - <<'PY_INNER'
import re
t=open('.build.md',encoding='utf-8').read()
t=re.sub(r'\n##\s+References\s*\n+:::\s*\{#refs\}\s*\n:::\s*\n','\n',t)
t=re.sub(r'(?<!\\)(?<!\$)\$(?!\$)((?:\\.|[^$\\\n]|\\\n)+?)\$(?!\$)',
         lambda m: '`\\('+m.group(1)+'\\)`{=latex}', t)
open('.build.md','w',encoding='utf-8').write(t)
PY_INNER

pandoc -f markdown-superscript-subscript .build.md -o tex/$BASE.tex \
  --standalone --shift-heading-level-by=-1 --natbib \
  --template=tools/template_prd.tex

# numeric journal: no author-prominent form — normalise \citet -> \citep
perl -0pi -e 's#\\citet\{#\\citep{#g' tex/$BASE.tex

# number display equations: pandoc emits \[ ... \]; convert to a numbered environment
# make long monospace paths breakable (prevents right-margin overflow)
perl -0pi -e 's{\\texttt\{([^{}]*)\}}{"\\texttt{".($1=~s#([/._])#$1\\allowbreak #gr)."}"}ge' tex/$BASE.tex
perl -0pi -e 's/\\\[/\\begin{equation}/g; s/\\\]/\\end{equation}/g' tex/$BASE.tex

( cd tex && \
  pdflatex -interaction=nonstopmode $BASE.tex >$BASE.build.log 2>&1 ; \
  BIBINPUTS="..:$BIBINPUTS" bibtex $BASE      >>$BASE.build.log 2>&1 ; \
  pdflatex -interaction=nonstopmode $BASE.tex >>$BASE.build.log 2>&1 ; \
  pdflatex -interaction=nonstopmode $BASE.tex >>$BASE.build.log 2>&1 ) || true

if [ -f tex/$BASE.pdf ]; then
  cp tex/$BASE.pdf $BASE.pdf
  echo "built paper/$BASE.pdf  (Physical Review D)"
  grep -c "^!" tex/$BASE.build.log | awk '{print $1" LaTeX errors (see tex/'$BASE'.build.log)"}'
  grep -c "Warning--" tex/$BASE.build.log 2>/dev/null | awk '{print $1" bibtex warnings"}'
  grep -c "Citation.*undefined" tex/$BASE.build.log 2>/dev/null | awk '{print $1" undefined citations"}'
else
  echo "BUILD FAILED — see tex/$BASE.build.log"; grep -A2 '^!' tex/$BASE.build.log | head -20
fi
