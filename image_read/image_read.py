from pytesseract import pytesseract
from PIL import Image

def extract_text(path):
    return pytesseract.image_to_string(Image.open(path),lang='ben+eng')



if __name__ == '__main__':
    with open('temp/t.txt','a') as f:
        f.write(extract_text('images/k.png'))