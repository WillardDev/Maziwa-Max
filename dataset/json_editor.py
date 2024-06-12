import PyPDF2
import json

def pdf_to_json(pdf_path, json_path, chunk_size=1):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        chunks = []

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader._get_page(page_num)
            text = page.extract_text()

            text_chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
            print(text_chunks)

            chunks.append(text_chunks)

    json_data = json.dumps(chunks, indent=4)

    with open(json_path, 'w') as json_file:
        json_file.write(json_data)

pdf_to_json('./dairy3.pdf', 'dairy3.json', chunk_size=500)