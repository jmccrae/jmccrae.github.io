import json
from urllib.request import urlopen
from urllib.parse import quote
import sys

data = json.load(open("publications.json"))

def make_name(a):
    name = ""
    if "given" in a:
        name = a["given"] + " "
    if "family" in a:
        name = name + a["family"]
    return name

for pub in data["@graph"]:
    print(pub["title"])
    with urlopen("https://api.crossref.org/works?mailto=johnmccrae@gmail.com&query=" + quote(pub["title"])) as crossref:
            result = json.load(crossref)
            for item in result["message"]["items"]:
                if "title" in item:
                    sys.stdout.write("  " + item["title"][0] + " - ")
                if "author" in item:
                    print(", ".join(make_name(a) for a in item["author"]))
                else:
                    print()
                if "DOI" in item:
                    print("    " + item["DOI"])
