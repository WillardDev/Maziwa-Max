import os
import fitz  # PyMuPDF

def pdf_to_text(pdf_path):
    text = ""

    # Construct absolute path
    pdf_path = os.path.abspath(pdf_path)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through each page
    for page_number in range(pdf_document.page_count):
        # Get the page
        page = pdf_document[page_number]

        # Extract text from the page
        text += page.get_text()

    # Close the PDF document
    pdf_document.close()

    return text

def save_to_txt(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(text)

# Replace 'your_pdf_file.pdf' with the actual path to your PDF file
pdf_path = './dataset/dairy3.pdf'
output_file = './dataset/dairy3.txt'

result_text = pdf_to_text(pdf_path)
save_to_txt(result_text, output_file)

print(f"Text extracted from PDF and saved to {output_file}.")
