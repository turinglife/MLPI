
CMD=pandoc -t beamer --template=slide_template.tex

PRE = slide_template.tex

all: slides

slides: \
	lec0_overview.pdf \
	lec1_metrics.pdf

lec0_overview.pdf: $(PRE) lec0_overview.md
	$(CMD) lec0_overview.md -o $@

lec1_metrics.pdf: $(PRE) lec1_metrics.md
	$(CMD) lec1_metrics.md -o $@
