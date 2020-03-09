import requests
import sys
import os.path
import json
import urllib.request

def locate_file(name, pub):
    if os.path.exists("papers/%s.pdf" % name):
        return "papers/%s.pdf" % name
    elif "url" in pub:
        urllib.request.urlretrieve(pub["url"], "papers/%s.pdf" % name)
        return "papers/%s.pdf" % name
    else:
        return None

def map_affiliation(affil):
    return ["National University of Ireland Galway" if a == "NUIG" else a for a in affil]

def main():
    if len(sys.argv) < 3:
        sys.stderr.write("usage: add-to-zendo.py ACCESS_TOKEN paper1 paper2 ...")
        sys.exit(-1)

    pub_list = json.load(open("publications.json"))

    ACCESS_TOKEN = sys.argv[1]
    r = requests.get('https://zenodo.org/api/deposit/depositions',
                 params={'access_token': ACCESS_TOKEN})
    if r.status_code != 200:
        sys.stderr.write("Access token does not work\n")
        sys.exit(-1)


    for name in sys.argv[2:]:
        pub = [p for p in pub_list["@graph"] if p["@id"] == name]
        if not pub:
            sys.stderr.write("could not find publication %s\n" % name)
            sys.exit(-1)
        pub = pub[0]

        headers = {"Content-Type": "application/json"}
        r = requests.post('https://zenodo.org/api/deposit/depositions',
                params={'access_token': ACCESS_TOKEN}, json={},
                headers=headers)
        deposition_id = r.json()['id']
        print(r.status_code)
        print(r.json())
        data = {'filename': '%s.pdf' % name}
        location = locate_file(name, pub)
        if location:
            files = {'file': open(location, 'rb')}
            r = requests.post('https://zenodo.org/api/deposit/depositions/%s/files' % deposition_id,
                    params={'access_token': ACCESS_TOKEN}, data=data,
                                       files=files)
            print(r.status_code)
            print(r.json())
            data = {
                        'title': pub["title"],
                        'upload_type': "publication",
                        'publication_date': pub["date"],
                        'creators': [{'name': n[0], 'affiliation': n[1]} for n in zip(pub["author"], 
                            map_affiliation(pub["affiliation"]))],
                        'description': pub["description"],
                        'language': 'eng'
                        }
            if pub["open"]:
                data['access_right'] = "open"
                data['license'] = pub["license"]
            else:
                data['access_right'] = "closed"
            if "doi" in pub:
                data['doi'] = pub['doi']
            if pub["@type"] == "Conference" or pub["@type"] == "Workshop":
                data['publication_type'] = "conferencepaper"
                if pub["booktitle"].startswith("Proceedings of the "):
                    data['conference_title'] = pub["booktitle"][19:]
                elif pub["booktitle"].startswith("Proceedings of"):
                    data['conference_title'] = pub["booktitle"][15:]
                else:
                    data['conference_title'] = pub["booktitle"]
            elif pub["@type"] == "swrc:Article":
                data['publication_type'] = "article"
                if "journal" in pub:
                    data['journal_title'] = pub["journal"]
                if "number" in pub:
                    data['journal_issue'] = pub["number"]
                if "volume" in pub:
                    data['journal_volume'] = pub["volume"]
                if "pages" in pub:
                    data['journal_pages'] = pub["pages"]
            if "grants" in pub:
                data["grants"] = pub["grants"]

            print(data)
            r = requests.put('https://zenodo.org/api/deposit/depositions/%s' % deposition_id,
                    params={'access_token': ACCESS_TOKEN}, data=json.dumps({"metadata":data}),
                          headers=headers)
            print(r.status_code)
            print(r.json())
#            r = requests.post('https://zenodo.org/api/deposit/depositions/%s/actions/publish' % deposition_id,
#                      params={'access_token': ACCESS_TOKEN} )
#            print(r.status_code)
#            print(r.json())
            print("Created deposition at %s" % deposition_id)

if __name__ == "__main__":
    main()

