#-list()
# -add(tytul, autor, rok)
# -save
# -delete(id)
# -edit(id, tytul, autor, rok)
# -search(kyterium, wartosc)
# {"klucz":"wartosc"}
import json

path_book = 'database_book.json'
def load(path):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save(path, database):
    with open(path, 'w') as file:
        json.dump(database, file, indent=4)

def add(database, tytul, autor, rok):
    # if id in database:
    #     raise ValueError("Książka o takim ID już istnieje.")
    id=len(database)+1

    database[id] = {'tytul':tytul,
                  'autor':autor, 
                  'rok':rok}
def delete(database, id):
    if id not in database:
        raise ValueError("Nie znaleziono książki o tym ID.")
    del database[id]

def edit(database, id, tytul=None, autor=None, rok=None):
    if id not in database:
        raise ValueError("Nie znaleziono książki o tym ID.")
    if tytul:
        database[id]['tytul'] = tytul
    if autor:
        database[id]['autor'] = autor
    if rok:
        database[id]['rok'] = rok



def book_list(base):            #inna zmienna niz database, zeby w petli sie nie mylilo
    for id, book in base.items():
        print(f"ID: {id}, tytuł: {book['tytul']}, autor: {book['autor']}, Rok: {book['rok']}")

database = load(path_book)
# add(database, 'Python dla bystrzaków', 'Nolan Illes', 2012)
book_list(database)
save(path_book, database)