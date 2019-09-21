"""
PyTesseract extracts text from images as a string
Optical Character Recognition (OCR)

To install Tesseract on your machine (Ubuntu):

    > sudo apt  install tesseract-ocr

then pip install the python package

    > pip install pytesseract
"""
from PIL import Image
import pytesseract

im = Image.open('myimage.jpg')
print(pytesseract.image_to_string(im))
