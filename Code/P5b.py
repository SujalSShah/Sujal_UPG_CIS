import unicodedata

a = "क"
b = "क़"
c = "क़"
d = "कमल"

print(unicodedata.name(a))
print(unicodedata.name(b))

try:
    print(unicodedata.name(c))
except TypeError as e:
    print("Error:", e)

print(c[0], c[1])
