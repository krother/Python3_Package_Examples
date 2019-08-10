from PIL import Image
import pytesseract

im = Image.open('myimage.jpg')
print(pytesseract.image_to_string(im))

