numero = -2
numero_siguiente = 1
numero_nuevo = "1"

print(type(numero).__name__)
print(type(numero_siguiente).__name__)
print(type(numero_nuevo).__name__)

valor = input("ingrese algo: ")
print(type(valor).__name__)

if valor.isalpha():
    print("hola")
elif valor.isdigit():
    print("no")