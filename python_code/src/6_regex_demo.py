import re

pattern = r"eggs"
if re.match(pattern, "eggseggsqweasd"):
    print("Match found")
else:
    print("Match not found")

if re.match(pattern, "qweeggseggsqweasd"):
    print("Match found")
else:
    print("Match not found")

## FindAll
if re.search(pattern, "qweeggseggsqweasd"):
    print("Match found", re.findall(pattern, "qweeggseggsqweasd"))
else:
    print("Match not found")

## Replace
string = "His name is John. John is a good boy"
pattern = r"John"
newstring = re.sub(pattern, "Joel", string)
print(newstring)
