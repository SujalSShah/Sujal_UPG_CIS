print("\nExample 1")
text = "शक्ति" # Sh-a-k-virama-t-i
print("A Hindi Word is शक्ति")
for char in text:
    if char == '\u094D': # Unicode for Virama
        print("Virama found!")
 #   else:
 #       print(" No Virama found")



#print("\nExample 2")
#text = "कमल"
#print("A Hindi Word is कमल")
#for char in text:
#    if char == '\u094D':
#        print("Virama found")
#    else:
#        print(" No Virama found")



#print("\nExample 3")
#text = "શબ્દ"
#print("A Gujarati Word is શબ્દ")
#for char in text:
#    if char == '\u0ACD':
#        print("Virama found!")
#    else:
#        print(" No Virama found")
