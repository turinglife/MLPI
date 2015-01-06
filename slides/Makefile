
CMD=pandoc -t beamer --template=slide_template.tex --filter=pdfilter.py 

PRE = slide_template.tex

all: slides

slides: \
	lec0_overview.pdf \
	lec1_math.pdf

lec0_overview.pdf: $(PRE) lec0_overview.md
	$(CMD) lec0_overview.md -o $@

LEC1_SRC = \
	lec1_math.md \
	lec1_topology.md \
	lec1_functional.md \
	lec1_prob.md


lec1_math.pdf: $(PRE) $(LEC1_SRC)
	$(CMD) lec1_functional.md -o $@
