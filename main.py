#1-misol
matn = "ALGORITM VA DASTURLASH"
n = matn.lower()
b = n.lstrip()
print(f"Bu matnda {len(b)} ta harf bor")

#2-misol
matn = "  java vs python  "
n = matn.title()
b = n.rstrip()
print(b)

#3-misol
matn = "o'quvchi talaba"
n = matn.capitalize()
print(len(n) // 3)

#4-misol
matn = "  DATA SCIENCE  "
n = matn.strip()
b = n.upper(), n.lower()
print(b)

#5-misol
matn = "web dasturchi"
n = matn.title()
b = n.lstrip()
print(len(b) // 2)
