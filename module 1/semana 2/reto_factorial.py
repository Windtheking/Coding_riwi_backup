#utilizar un programa para hayar la factorial

numero_entero_positivo = int(input("Ingrese el numero que desea usar para hayar la factorial:  "))

if numero_entero_positivo < 0:
    print("ingrse un numero positivo valido")
else: 
    x = 1
    factorial = 1
    for i in range(x , numero_entero_positivo+1):
        factorial= factorial * i
        print(factorial)
    print(f"el factorial de {numero_entero_positivo} es: {factorial}")

