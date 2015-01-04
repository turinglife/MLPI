
CMD=pandoc -t beamer --template=slide_template.tex

PRE = slide_template.tex

all: slides

slides: lec1_overview.pdf

lec1_overview.pdf: $(PRE) lec1_overview.md
	$(CMD) lec1_overview.md -o $@
