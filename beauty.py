import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Users\LOGISTICSSYSTEM28\AppData\Local\Tesseract-OCR\tesseract.exe'
from PIL import Image

img = Image.open('beauty.png')
text = tess.image_to_string(img)

print(text)
