import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from PIL import Image

text = pytesseract.image_to_string(Image.open("Receipts/rec_6.jpg"))
print(text)
