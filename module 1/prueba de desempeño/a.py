"""case = input()

match case:
    case 1:
        print("hola")
    case _:
        print("no)"""
books = ["horny","teller", "scrapper", "fucker", "horny","horny", "fucker", "fucker","fucker", "teller","teller","teller","scrapper","scrapper","scrapper","scrapper","scrapper","scrapper"]

value = 0 
value1 = 0
value2 = 0

for book in books:
    x = books[0]
    y = books[1]
    z = books[2]
    if book == x:
        value += 1
    if book == y:
        value1 += 1
    if book == z:
        value2 += 1

if value > value1 <value2:
    print(f"Los 3 mejores vendidos fueron {x},{y},{z}")
if value1 > value2 <value:
    print(f"Los 3 mejores vendidos fueron {x},{y},{z}")

if value2 > value <value1:
    print(f"Los 3 mejores vendidos fueron {x},{y},{z}")