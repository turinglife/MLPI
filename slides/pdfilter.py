# This filter adds extra support to pandoc format
#
# 1. Multi-column support
#
#   [columns]
#
#   [column=0.6]
#   ...
#
#
#   [column=0.4]
#   ...
#
#   [/columns]
#


import pandocfilters as pf

def latex(s):
    return pf.RawBlock('latex', s)

def do_filter(k, v, f, m):
    if k == "Para":
        value = pf.stringify(v)
        if value.startswith('[') and value.endswith(']'):
            content = value[1:-1]
            if content == "columns":
                return latex(r'\begin{columns}')
            elif content == "/columns":
                return latex(r'\end{columns}')
            elif content.startswith("column="):
                return latex(r'\column{%s\textwidth}' % content[7:])

if __name__ == "__main__":
    pf.toJSONFilter(do_filter)


    