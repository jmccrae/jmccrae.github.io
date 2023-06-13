#import json
import yaml
import sys
import re
from pylatexenc.latexencode import unicode_to_latex

def fix(string):
    return unicode_to_latex(string)


#data = json.loads(open("publications.json").read())
data = yaml.safe_load(open("publications.yaml"))

#out = open("test/test.tex", "w")
#
#out.write("\\documentclass[a4paper]{article}\n")
#out.write("\\begin{document}\n")

for paper in data:
    #out.write("\\cite{%s}\n" % paper["@id"])
    if paper["@type"] == "InProceedings" or paper["@type"] == "Conference" or paper["@type"] == "Workshop":
        print("@inproceedings{%s," % paper["@id"])
    elif paper["@type"] == "Proceedings":
        print("@proceedings{%s," % paper["@id"])
    elif paper["@type"] == "Book":
        print("@book{%s," % paper["@id"])
    elif paper["@type"] == "Article":
        print("@article{%s," % paper["@id"])
    elif paper["@type"] == "InCollection":
        print("@incollection{%s," % paper["@id"])
    elif paper["@type"] == "PhDThesis":
        print("@phdthesis{%s," % paper["@id"])
    elif paper["@type"] == "Misc":
        print("@misc{%s," % paper["@id"])
    elif paper["@type"] == "Patent":
        print("@misc{%s," % paper["@id"])
    first = True
    for key, value in paper.items():
        if key.startswith("@") or key == "grants" or key == "open" or key == "license":
            pass
        else:
            if not first:
                sys.stdout.write(",\n")
            else:
                first = False
            if key == "author":
                sys.stdout.write("author=\"%s\"" % " and ".join([unicode_to_latex(v) for v in value]))
            elif key == "editor":
                sys.stdout.write("editor=\"%s\"" % " and ".join(value))
            elif key == "title":
                sys.stdout.write("title={{%s}}" % fix(value))
            else:
                sys.stdout.write("%s=\"%s\"" % (key, fix(str(value))))
    print("")
    print("}")
    print("")

#out.write("\\bibliographystyle{ieeetr}\n")
#out.write("\\bibliography{../publications}\n")
#out.write("\\end{document}\n")
