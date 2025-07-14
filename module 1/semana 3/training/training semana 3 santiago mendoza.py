import time
import pprint
import os
"""Eres parte del equipo de desarrollo de software de una tienda que desea mejorar la gestión de su inventario digital. Te han asignado la tarea de crear un programa en Python que permita al equipo añadir, consultar, actualizar y eliminar productos del inventario de manera eficiente, así como calcular el valor total del inventario. Tu programa debe interactuar con el usuario para realizar las siguientes operaciones:"""



"""    Añadir productos:
        Cada producto debe estar definido por su nombre, precio y cantidad disponible
        Esta información será almacenada de modo que el inventario pueda crecer dinámicamente
    Consultar productos:
        Se debe poder buscar un producto por su nombre y obtener detalles como su precio y cantidad disponible
        Si el producto no está en el inventario, se debe notificar adecuadamente
    Actualizar precios:
        El programa debe permitir al usuario seleccionar un producto e introducir un nuevo precio, asegurando que este se actualice correctamente en el inventario
    Eliminar productos:
        El programa debe permitir al usuario eliminar productos del inventario de manera segura
    Calcular el valor total del inventario:
        El programa debe calcular el valor total de los productos en inventario y mostrarlo al usuario
        Para ello, utilizarás una función anónima (lambda) que facilite este cálculo.
"""
main = True
mercado_productos = {
                        "pudin":{
                                    "pudin_de_fresa":[(10000.259),(20)],
                                    "pudin_de_gelatina":[(12000),(30)]
                                },
                        "verduras":{
                                    "berenjena":[(2500),(40)],
                                    "Lechuga":  [(4000),(10)]
                                }
                    }

#funcion para limpiar la pantalla en linux
def cls():
    os.system("clear")

#funcion para manejar errores de input
def error_targeting(typo,text):
    x = True
    while x == True:
        try:
            chosen = typo(input(text))
            return chosen
        except:
            print("valores incorrectos detectados, porfavor ingrese valores validos")

#funcion principal del menu principal
def main_menu():
    print("=" * 200)
    print(("\033[1mBienvenido al servicio de la tienda Orion\033[0m").center(200))
    print("_" * 200)
    print(("\n ") + ("Inventario vigente en la tienda actualmente\n").center(192))
    print("=" * 200)
    print("1. Añadir productos")
    print("2. Consultar productos")
    print("3. Actualizar precios")
    print("4. Eliminar productos")
    print("5. Calcular el valor total del inventario")
    print("6. Salir")
    print("Escoja la opcion de su preferencia")
    variable = error_targeting(int,"--> ")

    #match para las opciones del menu
    match variable:
        #funcion para añadir datos
        case 1:
            añadir()
        #funcion para consultar los datos
        case 2:
            consulta()
        #funcoin para actualizas datos
        case 3:
            actualizar()
        #funcion para eliminar datos
        case 4:
            borrado_datos()
        #funcion para hacer la suma total de productos en stock
        case 5:
            total_inventareado()

        #escape del programa
        case 6:
            print("Gracias por su tiempo")
            time.sleep(1.5)
            exit()

        #caso default para manejar errores de input
        case _:
            print("valor fuera de rango detectados, porfavor ingrese valor validos")
            time.sleep(1.5)
            cls()



#funcion de inventareado total
def total_inventareado():
    cls()
    lis = []
    print("="*200)
    selection = error_targeting(str, "Ingrese el nombre del directorio al que quiere entrar: ")
    comprobando = mercado_productos.get(f"{selection}","Inexistente")
    #comprobacio de existencia del directorio a buscar
    if comprobando == "Inexistente":
        print("="*200)
        print((f"\nEl valor actual ingresado es {comprobando}").center(100))
        print("="*200)
        input("\nPresione enter para volver al menu principal")
    
    elif comprobando != "Inexistente":
        for valor in mercado_productos[f"{selection}"].values():
            lis.append(valor[1])
        
        #suma de valores del directorio buscado
        sumatory = sum(lis)
        print(f"el valor total de productos en el Directorio de verduras es: {sumatory}")
        input("Presione enter para continuar")


#funcion para borrar datos, busca datos por su directorio y producto y los borra
def borrado_datos():
    selection = error_targeting(str, "Ingrese el nombre del directorio al que quiere entrar: ")
    comprobando = mercado_productos.get(f"{selection}","Inexistente")
    Directorio2 = error_targeting(str, "Ingrese el producto que quiere eliminar: ")
    #comporbacio de existencia
    if comprobando == "Inexistente":
        print("="*200)
        print((f"\nEl valor actual ingresado es {comprobando}").center(100))
        print("="*200)
        input("\nPresione enter para volver al menu principal")
    
    elif comprobando != "Inexistente":
        print("="*200)
        print(f"el producto {Directorio2} sera eliminado del directorio {selection}")
        #busqueda del valor por directorio y producto
        try:
            del mercado_productos[f"{selection}"][f"{Directorio2}"]
            print(f"El producto {Directorio2} ha sido eliminado correctamente del directorio {selection}")
        except:
            print(f"El producto {Directorio2} no existe en el directorio {selection}")
        input("\nPresione enter para volver al menu principal")

#funcion para actualizar datos
def actualizar():
        print("="*200)
        print("Que desea actualizar?")
        print("1. Precio")
        print("2. Stock")
        print("Escoja el numero corresopndiente a su deseo")
        divergin = error_targeting(int,"--> ")
        #minimenu para escoger que actualizar
        if divergin > 2 and divergin < 1:
            print("Ingrese valores validos")
            time.sleep(2)
            cls()
            actualizar()
        #caso de actualizacion de precio
        elif divergin == 1:
            update = error_targeting(int, "Inserte el nuevo stock del producto: ")
            Directorio1 = error_targeting(str, "Inserte el directorio al que quiere acceder: ")
            comprobando = mercado_productos.get(f"{Directorio1}","Inexistente")
            Directorio2 = error_targeting(str, "Ingrese el producto que quiere editar su precio: ")
            if comprobando != "Inexistente":
                comprobando1 = mercado_productos[f"{Directorio1}"].get(f"{Directorio2}","Inexistente")
            else:
                comprobando1 = "Inexistente"

            if comprobando != "Inexistente" and comprobando1 != "Inexistente":

                if update == 0:
                    update = "No hay stock"
                
                mercado_productos[f"{Directorio1}"][f"{Directorio2}"][1] = (update)
            if comprobando == "Inexistente" or comprobando1 == "Inexistente":

                print("="*200)
                print(f"El directorio {Directorio1} con el producto {Directorio2} son {comprobando}")
                input("\nPresione enter para volver al menu principal")
        #caso de actualizacion de stock
        elif divergin == 2:
            update = error_targeting(int, "Inserte el nuevo stock del producto: ")
            Directorio1 = error_targeting(str, "Inserte el directorio al que quiere acceder: ")
            comprobando = mercado_productos.get(f"{Directorio1}","Inexistente")
            Directorio2 = error_targeting(str, "Ingrese el producto que quiere editar su stock: ")
            if comprobando != "Inexistente":
                comprobando1 = mercado_productos[f"{Directorio1}"].get(f"{Directorio2}","Inexistente")
            else:
                comprobando1 = "Inexistente"
            
            if comprobando != "Inexistente" and comprobando1 != "Inexistente":

                if update == 0:
                    update = "No hay stock"
                
                mercado_productos[f"{Directorio1}"][f"{Directorio2}"][1] = (update)
            if comprobando == "Inexistente" or comprobando1 == "Inexistente":

                print("="*200)
                print(f"El directorio {Directorio1} con el producto {Directorio2} son {comprobando}")
                input("\nPresione enter para volver al menu principal")

#funcion para consultar los datos
def consulta():
    jaja = True
    valor = 1
    cls()
    print("="*200)
    #display de los directorios principales para escoger bien
    print("Directorio pricipal")
    for claves in mercado_productos.keys():
        print("_"*200)
        print(f"\n{valor}.", claves)
        valor += 1
    #bucle para pedir el directorio a buscar y evitar errores de input
    while jaja == True:
        print("\nInserte el nombre del directorio que desea buscar")
        direcroty = error_targeting(str, "--> ")
        if not direcroty.isalpha():
            print("Ingrese un valor valido")
        if direcroty.isalpha():
            jaja = False
    
    #comprobacion de existencia del directorio
    #si no existe se notifica al usuario
    cls()
    comprobant = mercado_productos.get(f"{direcroty}","Inexistente")
    val1 = 1
    
    #si el directorio no existe se muestra un mensaje de inexistencia
    if comprobant == "Inexistente":
        print("="*200)
        print((f"\nEl valor actual ingresado es {comprobant}").center(100))
        print("="*200)
        input("\nPresione enter para volver al menu principal")


    #si el directorio existe se muestran los productos y sus valores
    if comprobant != "Inexistente":
        print("="*200)
        print(f"\nsubdirectorios de {direcroty}")
        for claves, valor in mercado_productos[f"{direcroty}"].items():
            print("_"*200)
            print(f"\n{val1}.", claves, "|", f"${valor[0]:.2f}", "|", f"{valor[1]}")
            
            val1 += 1
        
        input("\nPresione enter para volver al menu principal")
        cls()

        
#funcion para agregar valores al diccionario
def añadir():
    cls()
    constant = True
    
    print("="*200)
    #input creado para evitar errores
    path = error_targeting(str, "desea ingresar un nuevo directorio vacio? S/N: ").upper()
    #bucle que contiene variantes  diseñadas para crear directorios vacios 
    #si no existe un directorio vacio no podra entrar a un directorio que no sean los existentes
    #tambien funcion para entrar en directorios y añadir datos como productos y sus detalles
    while constant == True:

        if path != "N" and path != "S":
            print("Valores incorrectos porfavor ingrese un valor valido")
            path = error_targeting(str, " \ndesea ingresar un numevo directorio vacio? S/N: ").upper()
            print(path)
        elif path == "S":
            print("inserte el valor para agregar")
            clav = input("Clave: ").lower()
            mercado_productos[f"{clav}"] = {}
            pprint.pprint(mercado_productos, indent=3)
            path1 = error_targeting(str, "desea ingresar un nuevo directorio? S/N:  ").upper()
            
            
            if path1 != "S" and path1 != "N":
                print("valor incorrecto, inserte nuevo valor")
                path1 = error_targeting(str, "desea ingresar un nuevo directorio? S/N:  ").upper()

            if path1 == "N":
                
                path = "N"
                path1= "N"
                print(path)
                print(path1)
                constant = False
            elif path1 == "S":
                añadir()
                constant = False

        
        elif path == "N":
            print("usted decidio ingresar datos a un directorio existente")
            clav = input("Directorio: ").lower()
            clav1 = input("Producto: ").lower()
            val_precio = error_targeting(float, "Valor del producto: ")
            val_unidades = error_targeting(int, "Cantidad de productos: ")
            comprobando = mercado_productos.get(f"{clav}","Inexistente")
            
            if not comprobando == "Inexistente":
                mercado_productos[f"{clav}"][f"{clav1}"] = [(val_precio), (val_unidades)]
            elif comprobando == "Inexistente":
                print(f"Directorio {clav} no existente")
            
            path1 = error_targeting(str, "desea ingresar un nuevo directorio? S/N:  ").upper()
            
            if path1 != "S" and path1 != "N":
                print("valor incorrecto, inserte nuevo valor")
                path1 = error_targeting(str, "desea ingresar un nuevo directorio? S/N:  ").upper()
            else:   
                if path1 == "S":
                    añadir()
                    constant = False
                    
                elif path1 == "N":
                    pprint.pprint(mercado_productos, indent=3)
                    time.sleep(2.5)
                    path = "N"
                    path1= "N"
                    constant = False


#bucle principal del programa, se ejecuta hasta que el usuario decida salir
while main == True:
    cls()
    main_menu()

   
