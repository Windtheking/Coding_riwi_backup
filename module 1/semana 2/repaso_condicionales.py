"""
construe un algoritmo que nos 
permita verificar si podemos ir a 
cine tomando como punto de partida 
si tenemos o no dinero
"""


valor_entrada_cine = 6000
cliente_con_tarjeta = True

Dinero_disponible = int(input("Ingrese la cantidad de dinero que tiene disponible: "))

#------------------------------------------------------#

if cliente_con_tarjeta:
    valor_entrada_cine = valor_entrada_cine * 0.5
    
#------------------------------------------------------#
#------------------------------------------------------#


if Dinero_disponible >= valor_entrada_cine:
    print("puedes ir a cine")
else:
    print("No puede ir a cine")