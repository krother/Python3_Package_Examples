
from docx import Document

document = Document('hamlet.docx')

print(document)

for para in document.paragraphs:
    print(para.text)
