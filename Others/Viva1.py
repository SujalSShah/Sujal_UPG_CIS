# P1 to P4 Viva

# --------------------------------------------------------------------

# P1 

import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

img = Image.open("sample.jpg")
text = pytesseract.image_to_string(img, lang="hin")
print(text)



# --------------------------------------------------------------------

# P2

import cv2

image = cv2.imread('sample_faded.jpg')


blur = cv2.GaussianBlur(image, (5,5), 0)

cv2.imwrite('output.jpg', blur)

cv2.imshow('Original Color Image', image)
cv2.imshow('Processed Color Image', blur)

cv2.waitKey(0)

cv2.destroyAllWindows()


# --------------------------------------------------------------------

# P3

def detect_script(word):
    for char in word:

        # English (A-Z, a-z)
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):
            continue

        # Devanagari (Hindi, Marathi, Sanskrit)
        elif '\u0900' <= char <= '\u097F':
            return "Devanagari"

        # Gujarati
        elif '\u0A80' <= char <= '\u0AFF':
            return "Gujarati"

        # Arabic
        elif '\u0600' <= char <= '\u06FF':
            return "Arabic"

        # Any other language/script
        else:
            return "Other language"

    return "English"

#print(detect_script("Hello"))
#print(detect_script("भारत"))
#print(detect_script("ગુજરાત"))
#print(detect_script("தமிழ்"))
#print(detect_script("السلام عليكم"))




# --------------------------------------------------------------------

# P4


from jiwer import cer
ground_truth = "नमस्ते दुनिया"
ocr_output = "नमस्त दुनिया" # Simulating an error
error = cer(ground_truth, ocr_output)
print(f"Character Error Rate: {error * 100}%")


# --------------------------------------------------------------------


# End




