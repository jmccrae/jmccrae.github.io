import json

data = json.loads(open("publications.json").read())

out = open("publications.php", "w")

out.write("<?php include 'header.html'; ?>\n")
out.write("<div class=\"row col-lg-6 col-lg-offset-3\">\n\n")
out.write("<div style=\"text-align:right;padding-bottom:10px;\">Download as: <a href=\"publications.bib\">BibTeX</a>&nbsp;&nbsp;<a href=\"publications.json\">JSON-LD</a></div>")

for paper in data["@graph"]:
    if "ccepted" in str(paper["year"]):
        out.write("<p><b>")
    else:
        out.write("<p><b><a class=\"publication\"")
        if "url" in paper:
            out.write(" href=\"" + paper["url"] + "\">")
        else:
            out.write(" href=\"papers/" + paper["@id"] + ".pdf\">")
    out.write(paper["title"])
    if "ccepted" in str(paper["year"]):
        out.write("</a></b>. ")
    else:
        out.write("</a></b>. ")

    if len(paper["author"]) == 1:
        out.write(paper["author"][0])
    else:
        out.write(", ".join(paper["author"][:-1]))
        out.write(" and ")
        out.write(paper["author"][-1])
    out.write(", ")
    if paper["@type"] == "swrc:Proceedings" or paper["@type"] == "swrc:InProceedings":
        out.write("<i>")
        out.write(paper["booktitle"])
        out.write("</i>, ")
        if "pages" in paper:
            out.write("pp " + paper["pages"] + ", ")
    elif paper["@type"] == "swrc:Article":
        out.write("<i>")
        out.write(paper["journal"])
        out.write("</i>, ")
        if "volume" in paper:
            out.write(str(paper["volume"]))
            if "number" in paper:
                out.write("(" + str(paper["number"]) + "), ")
        if "pages" in paper:
            out.write("pp " + paper["pages"] + ", ")
    elif paper["@type"] == "swrc:InCollection":
        out.write("In: <i>")
        out.write(paper["booktitle"])
        if "editor" in paper:
            out.write(", eds. ")
            out.write(", ".join(paper["editor"]))
        out.write("</i>, ")
        if "pages" in paper:
            out.write("pp " + paper["pages"] + ", ")
    elif paper["@type"] == "swrc:Book":
        out.write("<i>")
        out.write(paper["publisher"])
        out.write("</i>, ")
    elif paper["@type"] == "swrc:PhDThesis":
        out.write("PhD Thesis for Graduate University of Advanced Studies (SoKenDai), ")
    else:
        sys.stderr.write("unknown type" + paper["@type"])

         
    out.write("(" + str(paper["year"]) + ").")
 


    out.write("</p>\n\n")


out.flush
out.close

