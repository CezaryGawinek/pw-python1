import re
text = "Dopasowuje pozycję, która nie jest granicą słowa."

x=re.search("^Dopasowuje.*słowa.$",text)
print(x)

# findall - zwraca liste zawierajaca wszystkie wystapienia
# search - zwraca obiekt match, jesli w dowolnym miejscu zajdzie dopasowanie 
# split - zraca liste, w ktorej ciagu znakow zostal podzielony
# sub - zastepuje jedno lub wiecej wystapien
# [a-z] - zwraca dopasowania pasujace do wzoru od a-z, male litery
# [michal] - m, i, c, h, a, l (znaki literowe) 
# [^michal] - wszystkie poza tymi
# [0-6][8-9] - 56, nie 72
# [+] - kazdy znak

text2="Dopasowuje nie pozycję, nie która nie jest granicą nie słowa"
x=re.findall("nie",text2)
print(x)

x=re.split("\s",text2,1)
print(x)

x=re.sub("nie","WOW",text2,1)
print(x)

x=re.findall(r"\bnie\b",text2)
print(x)

x=re.findall(r"[\w]+",text2)
print(x)

mail="imie.nazwisko@pw.edu.pl"
x=re.split("@",mail)
print(x)

x=re.match("^[\w\.]+@[\w\.]+",mail)
print(bool(x))

text3="rok 2023 będzie na pewno lepszy."

x=re.sub("\d",'X',text3)
print(x)

x=re.findall(r"\b[n]\w+",text3)
print(x)

kot="Nasz kot ma 60 lat i waży 4kg"
x=re.findall(r"\d+",kot)
print(x)

x=re.search(r"kg$",kot)
print(x) 

x=re.search(r"nasz",kot,re.IGNORECASE)
print(x)

text="Mój numer to 123-456-7890."
x=re.findall(r"\d+",text)
print(x)