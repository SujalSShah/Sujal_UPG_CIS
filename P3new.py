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
