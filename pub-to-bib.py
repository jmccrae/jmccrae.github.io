import json
import sys
import re


def fix(string):
    return re.sub("&", "\\&", string)


data = json.loads(open("publications.json").read())

#out = open("test/test.tex", "w")
#
#out.write("\\documentclass[a4paper]{article}\n")
#out.write("\\begin{document}\n")

for paper in data["@graph"]:
    #out.write("\\cite{%s}\n" % paper["@id"])
    if paper["@type"] == "swrc:InProceedings" or paper["@type"] == "Conference" or paper["@type"] == "Workshop":
        print("@inproceedings{%s," % paper["@id"])
    elif paper["@type"] == "swrc:Proceedings":
        print("@proceedings{%s," % paper["@id"])
    elif paper["@type"] == "swrc:Book":
        print("@book{%s," % paper["@id"])
    elif paper["@type"] == "swrc:Article":
        print("@article{%s," % paper["@id"])
    elif paper["@type"] == "swrc:InCollection":
        print("@incollection{%s," % paper["@id"])
    elif paper["@type"] == "swrc:PhDThesis":
        print("@phdthesis{%s," % paper["@id"])
    elif paper["@type"] == "swrc:Misc":
        print("@misc{%s," % paper["@id"])
    first = True
    for key, value in paper.items():
        if key.startswith("@"):
            pass
        else:
            if not first:
                sys.stdout.write(",\n")
            else:
                first = False
            if key == "author":
                sys.stdout.write("author=\"%s\"" % " and ".join(value))
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
