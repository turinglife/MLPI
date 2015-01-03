# make slide HTML using remark template

from jinja2 import Template


if __name__ == '__main__':

	tmplfile = "remark_template.html"
	srcfile = "lec1.md"
	dstfile = "lec1.html"
	title = "Lecture 1"

	with open(tmplfile, 'r') as f:
		jtempl = f.read()

	with open(srcfile, 'r') as f:
		md_content = f.read()

	tmpl = Template(jtempl)
	html_content = tmpl.render(title=title, markdown_content=md_content)

	with open(dstfile, 'w') as f:
		f.write(html_content)


