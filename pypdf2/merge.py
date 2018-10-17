
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()

merger.append(open("doc1.pdf", "rb"))
merger.append(open("doc2.pdf", "rb"))

# Write to an output PDF document
output = open("result.pdf", "wb")
merger.write(output)
