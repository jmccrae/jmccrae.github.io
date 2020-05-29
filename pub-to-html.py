import json
import re
import sys
import os

data = json.loads(open("publications.json").read())

out = open("publications.php", "w")

out.write("<?php include 'header.html'; ?>\n")
out.write("<div class=\"row col-lg-6 col-lg-offset-3\">\n\n")
out.write("<div style=\"text-align:right;\">Download as: <a href=\"publications.bib\">BibTeX</a>&nbsp;&nbsp;<a href=\"publications.json\">JSON-LD</a></div>")
out.write("""<div style="text-align:right;">By Type:&nbsp;&nbsp;
<a href="#" class="arttype all" onclick="showall(event)" style="color:black;">All</a>&nbsp;&nbsp;
<a href="#" style="padding-left:5px;" class="arttype selArticle" onclick="showonly(event,'Article')">Journal Articles</a>
<a href="#" style="padding-left:5px;" class="arttype selBook" onclick="showonly(event,'Book')">Books</a>
<a href="#" style="padding-left:5px;" class="arttype selInCollection" onclick="showonly(event,'InCollection')">Book Chapters</a>
<a href="#" style="padding-left:5px;" class="arttype selProceedings" onclick="showonly(event,'Proceedings')">Proceedings</a>
<a href="#" style="padding-left:5px;" class="arttype selrence" onclick="showonly(event,'rence')">Conferences</a>
<a href="#" style="padding-left:5px;" class="arttype selhop" onclick="showonly(event,'hop')">Workshops</a>
<a href="#" style="padding-left:5px;" class="arttype selPhDThesis" onclick="showonly(event,'PhDThesis')">Thesis</a>
<a href="#" style="padding-left:5px;" class="arttype selMisc" onclick="showonly(event,'Misc')">Reports</a>
</div>""")
out.write("""<div style="text-align:right;padding-bottom:10px;">By Year:&nbsp;&nbsp;
<a href="#" class="year all" onclick="showall(event)" style="color:black;">All</a>
<a href="#" class="year sely2020" onclick="showonly(event,'y2020')" style="padding-left:5px;">2020</a>
<a href="#" class="year sely2019" onclick="showonly(event,'y2019')" style="padding-left:5px;">2019</a>
<a href="#" class="year sely2018" onclick="showonly(event,'y2018')" style="padding-left:5px;">2018</a>
<a href="#" class="year sely2017" onclick="showonly(event,'y2017')" style="padding-left:5px;">2017</a>
<a href="#" class="year sely2016" onclick="showonly(event,'y2016')" style="padding-left:5px;">2016</a>
<a href="#" class="year sely2015" onclick="showonly(event,'y2015')" style="padding-left:5px;">2015</a>
<a href="#" class="year sely2014" onclick="showonly(event,'y2014')" style="padding-left:5px;">2014</a>
<a href="#" class="year sely2013" onclick="showonly(event,'y2013')" style="padding-left:5px;">2013</a>
<a href="#" class="year sely2012" onclick="showonly(event,'y2012')" style="padding-left:5px;">2012</a>
<a href="#" class="year sely2011" onclick="showonly(event,'y2011')" style="padding-left:5px;">2011</a>
<a href="#" class="year sely2010" onclick="showonly(event,'y2010')" style="padding-left:5px;">2010</a>
<a href="#" class="year sely2009" onclick="showonly(event,'y2009')" style="padding-left:5px;">2009</a>
<a href="#" class="year sely2008" onclick="showonly(event,'y2008')" style="padding-left:5px;">2008</a>
</div>""")

def mkclasses(paper):
    year = "y" + re.sub('\W+', '', str(paper["year"]))[:4]
    arttype = paper["@type"][5:]
    if "author" in paper:
        coauthors = ' '.join([re.sub('\W+', '', a) for a in paper["author"]])
        return "pub " + year + " " + arttype + " " + coauthors
    else:
        return "pub " + year + " " + arttype


def year_as_number(year):
    if isinstance(year, str):
        return int(year[:4])
    else:
        return year

last_year = ""

for paper in data["@graph"]:
    if "year" not in paper:
        print(paper["@id"])

    if year_as_number(paper["year"]) != last_year:
        ystr = str(year_as_number(paper["year"]))
        out.write("<h3 class='y" + ystr + "'>" + ystr + "</h3><hr class='y" + ystr + "'/>")
        last_year = year_as_number(paper["year"])

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
    if paper["@type"] == "swrc:InProceedings" or paper["@type"] == "Conference" or paper["@type"] == "Workshop":
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
        if "publisher" not in paper:
            print(paper["@id"])
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
 
    if "url" in paper and os.path.exists("papers/%s.pdf" % paper["@id"]):
        out.write(" <a href='papers/%s.pdf'>PDF</a>" % paper["@id"])



    if "description" in paper:
        out.write(" <a onclick='$(\"#abstract-%s\").slideToggle()' class='abstract-link'>Abstract</a></p>\n\n" % paper["@id"])
        out.write("<p class='abstract' id='abstract-" + paper["@id"] + "'>" + paper["description"] + "</p>\n\n")
    else:
        out.write("</p>\n\n")

out.write("</div></div>")
out.write("""<script src="http://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>""")
out.write("""<script>
        function showonly(event,p) {
            event.preventDefault();
            $('.pub:not(.' + p + ')').slideUp();
            $('.' + p).slideDown();
            $('.all').css('color','#00bdff');
            $('.arttype').css('color', '#00bdff');
            $('.year').css('color', '#00bdff');
            $('.sel' + p).css('color', 'black');
            }
        function showall(event,p) {
            event.preventDefault();
            $('.pub').slideDown();
            $('.arttyp').css('color', '#00bdff');
            $('.year').css('color', '#00bdff');
            $('.all').css('color','black');
            }
            </script>""")

out.write("<?php include 'footer.html'; ?>")

out.flush
out.close

