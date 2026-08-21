import unicodedata
a="क"
b="क़"
c="क़"

print(unicodedata.name(a))
print(unicodedata.name(b))
#print(unicodedata.name(c))

for x in c:
    print(x, unicodedata.name(x))

print(len("क"))
print(len("क़"))
print(len("क़"))
print(len(c))
