import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img=Image.open('image.')
text=pytesseract.image_to_string(img)
print(text)
