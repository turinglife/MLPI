
CMD=pandoc -t beamer --template=slide_template.tex --filter=pdfilter.py 

PRE = slide_template.tex

all: slides

clean:
	rm -f *.pdf

slides: \
	lec0_overview.pdf \
	lec1_math.pdf

lec0_overview.pdf: $(PRE) lec0_overview.md
	$(CMD) lec0_overview.md -o $@

LEC1_SRC = \
	lec1_math.md \
	lec1_topology.md \
	lec1_functional.md \
	lec1_prob.md \
	lec1_convex.md

lec1.md: $(LEC1_SRC)
	cat $(LEC1_SRC) > lec1.md

lec1_math.pdf: $(PRE) lec1.md
	$(CMD) lec1.md -o $@
