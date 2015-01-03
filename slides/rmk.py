# make slide HTML using remark template

import sys
from jinja2 import Template


if __name__ == '__main__':

	if len(sys.argv) != 2:
		print """
Usage:

    python rmk.py <lecture_name>

"""
		sys.exit(1)

	lec = sys.argv[1]

	tmplfile = "remark_template.html"
	srcfile = lec + ".md"
	dstfile = lec + ".html"
	title = "MLPI " + lec

	with open(tmplfile, 'r') as f:
		jtempl = f.read()

	with open(srcfile, 'r') as f:
		md_content = f.read()

	tmpl = Template(jtempl)
	html_content = tmpl.render(title=title, markdown_content=md_content)

	with open(dstfile, 'w') as f:
		f.write(html_content)


