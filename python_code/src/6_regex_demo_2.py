import re

## metacharacter
pattern = r"gr.y"
string = "grwy"
if re.match(pattern, string):
    print("Match found")

if re.match(pattern, "gray"):
    print("Match found")

if re.match(pattern, "greey"):
    print("Match found")

## ^ and $ metacharacter
print("------^ and $ metacharacter--------")
pattern = r"^gr.y$"
if re.match(pattern, "grey"):
    print("match found")

if re.match(pattern, "arey"):
    print("match found")

if re.match(pattern, "grep"):
    print("match found")

## Character class
print("------Character Class--------")
pattern = r"[A-Za-z][A-Za-z][0-9]"
if re.match(pattern, "Js9"):
    print("Match found")

## * metacharacter
print("------* metacharacter--------")
pattern = r"jo*l"
if re.match(pattern, "joooool"):
    print("Match Found")
if re.match(r"jo.*l", "jowerwerwereasdl"):
    print("Match Found")
if re.match(r"egg(bacon)*", "eggsbaconbacon"):
    print("Match Found")
if re.match(r"egg(bacon)*", "eggs"):
    print("Match Found")
if re.match(r"egg(bacon)*", "bacon"):
    print("Match Found")

## *Group
print("------Group--------")
pattern = "bread(eggs)*bread"
if re.match(pattern,"breadeggseggsbread"):
    print("Match Found")

