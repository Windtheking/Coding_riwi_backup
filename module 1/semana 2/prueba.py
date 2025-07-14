"""
#for
lis  = [1,2,3,4,5,6,7,8,9,10,11,12,13]

for index in range(len(lis), 7, -1):
    print("valor de index es: ", index)



#While
flag = "si"

while flag != "no":
    print("hola mundo")
    flag = input("Ingrese cualqiuera cosa para continuar: ")


#while con variable
i = 0

while i < 5:
    print(f"hola {i}")
    i += 1

#

datas = ["Rojo","Azul","Verde"]

for i, data in enumerate(datas):
    print(f"el valor {data} tiene la posicion {i}")"""


def prueba():
    lista = input("ingrese valor: ")

    añadir = lista.split(", ")

    for lis in lista:

        parseado = float(añadir)


    print(añadir)