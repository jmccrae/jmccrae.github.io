import yaml
import os
import requests
from PyPDF2 import PdfReader
from io import BytesIO

publications = yaml.load(open('_data/publications.yaml'), Loader=yaml.FullLoader)

for publication in publications:
    pubid = publication['id']
    if 'url' not in publication:
        continue
    if os.path.exists(f'papers/{pubid}.pdf'):
        continue
    print(f"Downloading {pubid} from {publication['url']}")

    pdf_url = publication['url']
    try:
        # Attempt to download the PDF
        response = requests.get(pdf_url)
        
        # Raise an exception if the download failed (status code not 200)
        response.raise_for_status()
        

        if not response.headers['Content-Type'].startswith('application/pdf'):
            raise ValueError(f"Invalid MIME type: {response.headers['Content-Type']}. Expected 'application/pdf'.")

        # Open the PDF from the downloaded content
        pdf_file = BytesIO(response.content)
        pdf_reader = PdfReader(pdf_file)

        # Count the number of pages
        num_pages = len(pdf_reader.pages)

        if num_pages < 20:
            with open(f'papers/{pubid}.pdf', 'wb') as f:
                f.write(response.content)
        else:
            print(f"Skipping {pubid} because it has {num_pages} pages")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download the PDF: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")
        
