
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

lectures: lec0 lec1 lec2

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

$(lec1_note): $(NOTE_PRE) $(lec1_src)
	cat $(lec1_src) | $(MKNOTE) -o $@

$(lec1_slide): $(SLIDE_PRE) $(lec1_src)
	cat $(lec1_src) | $(MKSLIDE) -o $@

## lec2

lec2_src = \
	lec2/lec2_montecarlo.md

lec2_note=notes/lec2_montecarlo.pdf
lec2_slide=slides/lec2_montecarlo_slides.pdf

lec2: $(lec2_slide) $(lec2_note)

$(lec2_slide): $(NOTE_PRE) $(lec2_src)
	cat $(lec2_src) | $(MKSLIDE) -o $@

$(lec2_note): $(SLIDE_PRE) $(lec2_src)
	cat $(lec2_src) | $(MKNOTE) -o $@


#### Clean

clean:
	rm -r notes slides

