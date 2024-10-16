import PyPDF2
import json

def pdf_to_json(pdf_file_path, json_file_path):
    # Create a PDF file reader object
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        pdf_data = {}
        # Extract text from each page and add it to a dictionary
        for i, page in enumerate(reader.pages):
            page_text = page.extract_text()
            pdf_data[f'Page_{i + 1}'] = page_text

    # Write the dictionary to a JSON file
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(pdf_data, json_file, indent=4)


pdf_file_path = 'C:/Users/keabe/Desktop/Antive Internal Projects/LLM Reader/Model/Term Of Service Data/E-Commerce/Terms and Conditions « Takealot.com.pdf'
json_file_path = 'Takealot.json'
pdf_to_json(pdf_file_path, json_file_path)
print(f'PDF data saved to {json_file_path}')


