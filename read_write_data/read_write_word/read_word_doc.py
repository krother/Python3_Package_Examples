
from docx import Document

document = Document('example.docx')

print(document)

for para in document.paragraphs:
    print(para.text)


