
from PyPDF2 import PdfFileMerger

merger = PdfFileMerger()
     
merger.append(open("01_title_grants.pdf", "rb"))
merger.append(open("02_GettingGrants.pdf", "rb"))
merger.append(open("ebooks.pdf", "rb"))

# Write to an output PDF document
output = open("Academis_GettingGrants_1.0.pdf", "wb")
merger.write(output)
