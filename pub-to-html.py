import json
import re

data = json.loads(open("publications.json").read())

out = open("publications.php", "w")

out.write("<?php include 'header.html'; ?>\n")
out.write("<div class=\"row col-lg-6 col-lg-offset-3\">\n\n")
out.write("<div style=\"text-align:right;\">Download as: <a href=\"publications.bib\">BibTeX</a>&nbsp;&nbsp;<a href=\"publications.json\">JSON-LD</a></div>")
out.write("""<div style="text-align:right;padding-bottom:10px;">By Type:&nbsp;&nbsp;
<a href="#" class="arttype all" onclick="showall()">All</a>&nbsp;&nbsp;
<a href="#" class="arttype selArticle" onclick="showonly('Article')">Journal Articles</a>&nbsp;&nbsp;
<a href="#" class="arttype selBook" onclick="showonly('Book')">Books</a>&nbsp;&nbsp;
<a href="#" class="arttype selInCollection" onclick="showonly('InCollection')">Book Chapters</a>&nbsp;&nbsp;
<a href="#" class="arttype selProceedings" onclick="showonly('Proceedings')">Proceedings Volumes</a>&nbsp;&nbsp;
<a href="#" class="arttype selInProceedings" onclick="showonly('InProceedings')">Conference/Workshops Articles</a>&nbsp;&nbsp;
<a href="#" class="arttype selPhDThesis" onclick="showonly('PhDThesis')">Thesis</a>&nbsp;&nbsp;
<a href="#" class="arttype selMisc" onclick="showonly('Misc')">Reports</a>
</div>""")
out.write("""<div style="text-align:right;padding-bottom:10px;">By Year:&nbsp;&nbsp;
<a href="#" class="year all" onclick="showall()">All</a>&nbsp;&nbsp;
<a href="#" class="year sely2018" onclick="showonly('y2018')">2018</a>&nbsp;&nbsp;
<a href="#" class="year sely2017" onclick="showonly('y2017')">2017</a>&nbsp;&nbsp;
<a href="#" class="year sely2016" onclick="showonly('y2016')">2016</a>&nbsp;&nbsp;
<a href="#" class="year sely2015" onclick="showonly('y2015')">2015</a>&nbsp;&nbsp;
<a href="#" class="year sely2014" onclick="showonly('y2014')">2014</a>&nbsp;&nbsp;
<a href="#" class="year sely2013" onclick="showonly('y2013')">2013</a>&nbsp;&nbsp;
<a href="#" class="year sely2012" onclick="showonly('y2012')">2012</a>&nbsp;&nbsp;
<a href="#" class="year sely2011" onclick="showonly('y2011')">2011</a>&nbsp;&nbsp;
<a href="#" class="year sely2010" onclick="showonly('y2010')">2010</a>&nbsp;&nbsp;
<a href="#" class="year sely2009" onclick="showonly('y2009')">2009</a>&nbsp;&nbsp;
<a href="#" class="year sely2000" onclick="showonly('y2008')">2008</a>
</div>""")

def mkclasses(paper):
    year = "y" + re.sub('\W+', '', str(paper["year"]))[:4]
    arttype = paper["@type"][5:]
    if "author" in paper:
        coauthors = ' '.join([re.sub('\W+', '', a) for a in paper["author"]])
        return "pub " + year + " " + arttype + " " + coauthors
    else:
        return "pub " + year + " " + arttype

for paper in data["@graph"]:
    if "ccepted" in str(paper["year"]):
        out.write("<p class=\"" + mkclasses(paper) + "\"><b>")
    else:
        out.write("<p class=\"" + mkclasses(paper) + "\"><b><a class=\"publication\"")
        if "url" in paper:
            out.write(" href=\"" + paper["url"] + "\">")
        else:
            out.write(" href=\"papers/" + paper["@id"] + ".pdf\">")
    out.write(paper["title"])
    if "ccepted" in str(paper["year"]):
        out.write("</a></b>. ")
    else:
        out.write("</a></b>. ")

    if "author" in paper:
        if len(paper["author"]) == 1:
            out.write(paper["author"][0])
        else:
            out.write(", ".join(paper["author"][:-1]))
            out.write(" and ")
            out.write(paper["author"][-1])
        out.write(", ")
    if "editor" in paper:
        out.write("<i>")
        if len(paper["editor"]) == 1:
            out.write(paper["editor"][0])
        else:
            out.write(", ".join(paper["editor"][:-1]))
            out.write(" and ")
            out.write(paper["editor"][-1])
        out.write(" (eds)</i>, ")
    if paper["@type"] == "swrc:InProceedings":
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
    elif paper["@type"] == "swrc:Proceedings":
        out.write("<i>")
        out.write(paper["publisher"])
        out.write(" - ")
        out.write(paper["series"])
        out.write("</i>, ")
    elif paper["@type"] == "swrc:PhDThesis":
        out.write("PhD Thesis for Graduate University of Advanced Studies (SoKenDai), ")
    elif paper["@type"] == "swrc:Misc":
        out.write("Technical Report: " + paper["organization"])
    else:
        sys.stderr.write("unknown type" + paper["@type"])

         
    out.write("(" + str(paper["year"]) + ").")
 


    out.write("</p>\n\n")

out.write("</div></div>")
out.write("""<script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>""")
out.write("""<script>
        function showonly(p) {
            $('.pub:not(.' + p + ')').slideUp();
            $('.' + p).slideDown();
            $('.all').css('color','#00bdff');
            $('.arttyp').css('color', '#00bdff');
            $('.year').css('color', '#00bdff');
            $('.sel' + p).css('color', 'black');
            }
        function showall(p) {
            $('.pub').slideDown();
            $('.all').css('color','black');
            $('.arttyp').css('color', '#00bdff');
            $('.year').css('color', '#00bdff');
            }
            </script>""")

out.write("<?php include 'footer.html'; ?>")

out.flush
out.close

