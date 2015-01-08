
NOTE_TEMPLATE=note_template.tex
NOTE_PRE= $(NOTE_TEMPLATE) notes/.created

SLIDE_TEMPLATE=slide_template.tex
SLIDE_FILTER=pdfilter.py
SLIDE_PRE = $(SLIDE_TEMPLATE) $(SLIDE_FILTER) slides/.created

MKNOTE=pandoc -t latex --template=$(NOTE_TEMPLATE)
MKSLIDE=pandoc -t beamer --template=$(SLIDE_TEMPLATE) --filter=$(SLIDE_FILTER) 

.phony: all clean
all: lectures

#### Lectures

lectures: lec0 lec1

notes/.created:
	mkdir -p notes
	touch notes/.created

slides/.created:
	mkdir -p slides
	touch slides/.created

$(lectures): %: $(%_note)

## lec0

lec0_src=lec0/lec0_overview.md
lec0_note=notes/lec0_overview.pdf
lec0_slide=slides/lec0_overview_slides.pdf

lec0: $(lec0_note) $(lec0_slide)

$(lec0_note): $(NOTE_PRE) $(lec0_src)
	cat $(lec0_src) | $(MKNOTE) -o $@

$(lec0_slide): $(SLIDE_PRE) $(lec0_src)
	cat $(lec0_src) | $(MKSLIDE) -o $@

## lec1

lec1_src = \
	lec1/lec1_math.md \
	lec1/lec1_topology.md \
	lec1/lec1_functional.md \
	lec1/lec1_prob.md \
	lec1/lec1_convex.md

lec1_note=notes/lec1_math.pdf
lec1_slide=slides/lec1_math_slides.pdf

lec1: $(lec1_slide) $(lec1_note)

$(lec1_note): $(SLIDE_PRE) $(lec1_src)
	cat $(lec1_src) | $(MKNOTE) -o $@

$(lec1_slide): $(SLIDE_PRE) $(lec1_src)
	cat $(lec1_src) | $(MKSLIDE) -o $@


#### Clean

clean:
	rm -r notes slides

