import re

pattern = r"eggs"
if re.match(pattern, "eggseggsqweasd"):
    print("Match found")
else:
    print("Match found")

print(re.match(pattern, "qweeggs"))