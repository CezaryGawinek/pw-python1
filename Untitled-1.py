def powitanie(imie):
    print(f"Witaj w świecie pythona, {imie}!")

powitanie("test")
#=============================================================
def max_min(a, b, c):
    return max(a, b, c), min(a, b, c)

print (max_min(10, 20, 30))
#=============================================================
def dlugosc_ciagu(ciag):
    return len(ciag)

print(dlugosc_ciagu("Python"))
#=============================================================
def silnia(n):
    if n==0:
        return 1
    else:
        return n*silnia(n-1)

t=silnia(5)
print(t)

def silnia2(n):
    wynik = n
    while n>1:
        n=n-1
        wynik=wynik*n
    return wynik

print(silnia(5))
#=============================================================
def dodawanie(a:int, b:int):
    return a+b

print(dodawanie(4,3))
#=============================================================
# import requests

# response = requests.get('https://www.google.com')
# print(response.text)
#=============================================================
# czy istnieje @: abc.abc@pw.edu.pl
#        username |     | |       | domena
# walidacja pustych znaków, user na od 6-30 znaków, domena to pw.edu.pl
def validate_email(email):
    if email.count('@')!=1:
        raise ValueError("To nie jest adres mailowy")
 #podzial adresu na username i domene
    param = email.split('@')

    if param[1] == 'pw.edu.pl':
        True
    else:
        raise ValueError("Domena jest spoza PW!")
    
    return True

          
try:
    validate_email("imie.nazwisko@pw.edu.pl")
except ValueError as e:
    print(f"Komunikat błędu:",{e})

#Funkcja validate_password, 8 znaków, jedna cyfra i jedna wielka litera

def validate_password(password):
    dlugosc = len(password)<8
    cyfra = any(char.isdigit() for char in password)
    wielka_litera = any(char.isupper() for char in password)
    if dlugosc != True:
        raise ValueError("To hasło jest za krótkie.")
    elif cyfra != True:
        raise ValueError("To hasło nie ma cyfry.")
    elif wielka_litera != True:
        raise ValueError("To hasło nie ma wielkiej litery")
    return dlugosc and cyfra and wielka_litera

if validate_password("Haslo1"):
    print("Masz silne hasło!")

# def validate_password(password):
#     dlugosc = len(password)<8
#     cyfra = any(char.isdigit() for char in password)
#     wielka_litera = any(char.isupper() for char in password)
#     return cyfra and wielka_litera and dlugosc

# haslo = input("Wprowadz haslo: ")

# if validate_password(haslo):
#     print("Mam silne haslo")

def validate_username(name):
    dlugosc = len(name)>2 and len(name)<17
    litery = any(char.isalpha() for char in name)
    if litery == False:
        return False
    cyfry = any(char.isdigit() for char in name)
    return dlugosc and litery or cyfry

if validate_username("aaaaa4"):
    print("tak")
else:
    print("nie")

#192.168.128.1
def validate_ip(ip):
    param = ip.split('.')
    pierwsza_kropka = param[0].isnumeric() 
    if len(param[0])!=3:
        return False
    druga_kropka = param[1].isnumeric()
    if len(param[1])!=3:
        return False
    trzecia_kropka = param[2].isnumeric()
    if len(param[2])!=3:
        return False
    czwarta_kropka = param[3].isnumeric()
    if len(param[3])!=1:
        return False
    return pierwsza_kropka and druga_kropka and trzecia_kropka and czwarta_kropka
    
if validate_ip("192.168.128.1"):
    print("T")
else:
    print ("N")


def validate_ip(ip):
    param = ip.split('.')
    for i in range(4):
        if param[i].isnumeric():
            return True
        else: 
            return False
    
if validate_ip("192.168.128.1"):
    print("T")
else:
    print ("N")


# UNFINISHED
def validate_NIP(nip:int):
    weights=[6,5,7,2,3,4,5,6,7]
    if len(nip) != 10:
        return False
    if nip.isdigit():
        return False
    suma=0
    for i in range(9):
        suma += int(nip[i])*weights[i]

    if suma%11 != nip[9]:
        return False
    return True