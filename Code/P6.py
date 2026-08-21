# Practical 6: Devanagari to Gujarati Transliteration

mapping = {
    # Independent vowels
    'अ': 'અ', 'आ': 'આ', 'इ': 'ઇ', 'ई': 'ઈ',
    'उ': 'ઉ', 'ऊ': 'ઊ', 'ए': 'એ', 'ऐ': 'ઐ',
    'ओ': 'ઓ', 'औ': 'ઔ',

    # Consonants
    'क': 'ક', 'ख': 'ખ', 'ग': 'ગ', 'घ': 'ઘ', 'ङ': 'ઙ',
    'च': 'ચ', 'छ': 'છ', 'ज': 'જ', 'झ': 'ઝ', 'ञ': 'ઞ',
    'ट': 'ટ', 'ठ': 'ઠ', 'ड': 'ડ', 'ढ': 'ઢ', 'ण': 'ણ',
    'त': 'ત', 'थ': 'થ', 'द': 'દ', 'ध': 'ધ', 'न': 'ન',
    'प': 'પ', 'फ': 'ફ', 'ब': 'બ', 'भ': 'ભ', 'म': 'મ',
    'य': 'ય', 'र': 'ર', 'ल': 'લ', 'व': 'વ',
    'श': 'શ', 'ष': 'ષ', 'स': 'સ', 'ह': 'હ',

    # Vowel signs
    'ा': 'ા',
    'ि': 'િ',
    'ी': 'ી',
    'ु': 'ુ',
    'ू': 'ૂ',
    'े': 'ે',
    'ै': 'ૈ',
    'ो': 'ો',
    'ौ': 'ૌ',

    # Other signs
    'ं': 'ં',
    'ः': 'ઃ',
    'ँ': 'ઁ',
    '्': '્',

    # Space and punctuation
    ' ': ' ',
    '।': '।'
}

#text = input("Enter Devanagari text: ")

t1="भारत"
r1 = ""

for char in t1:
    if char in mapping:
        r1 += mapping[char]
    else:
        r1 += char

print("\n\nSample 1:")
print("Devnagari text:",t1)
print("Gujarati text:", r1)


t2="भरत"
r2 = ""

for char in t2:
    if char in mapping:
        r2 += mapping[char]
    else:
        r2 += char

print("\n\nSample 2:")
print("Devnagari text:",t2)
print("Gujarati text:", r2)

