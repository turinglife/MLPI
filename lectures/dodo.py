# A DoIt script for building the course materials

import yaml
import os
import os.path

from doit.task import clean_targets


with open("course.yaml", "r") as fcourse:
    course = yaml.safe_load(fcourse)

note_template = "note_template.tex"
slide_template = "slide_template.tex"


if not os.path.isdir("notes"):
    os.mkdir("notes")

if not os.path.isdir("slides"):
    os.mkdir("slides")


def task_lectures():
    """Build lecture materials"""

    lectures = course['lectures']

    for lec in lectures:
        pre = lec['pre']
        src = lec["src"]
        title = pre + '_' + lec['name']

        sourcefiles = [os.path.join(pre, "%s_%s.md" % (pre, s)) for s in src]
        srcseq = ' '.join(sourcefiles)

        for fmt in ["notes", "slides"]:
            outdir = fmt

            # format-specific options

            if fmt == "notes":
                outfname = "%s.pdf" % title
                tfmt = 'latex'
                templatefile = "notes_template.tex"

            elif fmt == "slides":
                outfname = "%s_slides.pdf" % title
                tfmt = 'beamer'
                templatefile = "slides_template.tex"

            # decide output file and command 

            outpath = os.path.join(outdir, outfname)

            cmd = "cat {srcs} | pandoc -t {tfmt} --template={templ} -o {output}".format(
                srcs=srcseq,
                tfmt=tfmt,
                templ=templatefile,
                output=outpath)

            # yield task

            yield {
                'name': "{title} [{fmt}]".format(title=title, fmt=fmt),
                'actions': [cmd],
                'file_dep': [templatefile] + sourcefiles,
                'targets' : [outpath],
                'clean': [clean_targets],
                'verbosity': 2
            }

