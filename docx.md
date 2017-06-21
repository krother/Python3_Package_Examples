
# python-docx

### What it is good for?

Create, read and write Word documents.

A straightforward library to access documents in MS Word format. Available features include text, labeled sections, pictures and tables.

### Installed with Python by default

no

### Installed with Anaconda

no

### How to install it?

    pip install python-docx

### Example

Create a Word document:

    from docx import Document

    d = Document()

    d.add_heading('Hamlet')
    d.add_heading('dramatis personae', 2)
    d.add_paragraph('Hamlet, the Prince of Denmark')

    d.save('hamlet.docx')

Read a Word document:

    document = Document('hamlet.docx')
    for para in document.paragraphs:
        print(para.text)

### Where to learn more?

[https://python-docx.readthedocs.org](https://python-docx.readthedocs.org)
