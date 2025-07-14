import pprint
import os
import time

#Funcion para limpiar pantalla
def cls():
    os.system('clear')


#funcion de menu principal
def main_menu():
    cls()
    global eleccion
    print("=" * 227)
    print(("Asistente de cocina virtual CocInA").center(200))
    print("=" * 227)
    print("1. Ensalada César con pollo")
    print("2. Wrap de pollo con salsa César")
    print("3. Sándwich clásico de pollo")
    print("4. Salir")
    print("_"*227)
    print("Escoga el numero de la opcion que desea: ")
    eleccion = int(input("-->"))
    #seleccion de casos dependiendo de que producto se escoje
    match eleccion:
        #caso de ensalada cesar
        case 1:
            #consulta de tipo de pollo
            preparar_pollo_a_la_plancha(input("Como desea su pollo (tiras o normal): ").lower())
            #consulta sobre la pimienta en salsa
            preparar_salsa_cesar((input("desea pimienta negra molida?: ")).lower())
            print("="*220)
            emplatado()
            print("="*220)
        #caso de wrap cesar
        case 2:
            #consulta de tipo de pollo
            preparar_pollo_a_la_plancha(input("Como desea su pollo (tiras o normal): "))
            #consulta sobre la pimienta en salsa
            preparar_salsa_cesar((input("desea pimienta negra molida?: ")).lower())
            print("="*220)
            emplatado()
            print("="*220)
        #caso de sandwiche
        case 3:
            #consulta de tipo de pollo
            preparar_pollo_a_la_plancha(input("Como desea su pollo (tiras o normal): "))
            #Sandwiche no contiene salsa
            print("No contiene salsa Cesar")
            print("="*220)
            emplatado()
            print("="*220)
        #caso de salida
        case 4:
            print("Gracias por su tiempo")
            time.sleep(1.5)
            exit()
        #caso default (catching de errores)
        case _:
            constant = True
            while constant == True:
                print("Valor invalido, ingrese un numero correcto")
                print("Escoga el numero de la opcion que desea: ")
                eleccion = int(input("-->"))







#opciones de presentacion de pollo
def preparar_pollo_a_la_plancha(presentacion):
    #declaracion global de variables
    global presentation
    #variable para empezar el bucle
    reiteration = True
    while reiteration == True:
        #condicional para evaluar si ingreso una palabra correcta
        if presentacion == "tiras" or presentacion == "normal":
            #descripcion dependiente de que escogio, normal o tiras
            if presentacion == "tiras":
                print("En camino un pollo jugoso en tiras gruesas🔥")
                time.sleep(1.5)
            #descripcion dependiente de que escogio, normal o tiras
            elif presentacion == "normal":
                print ("buena proteina en gramos conjuntos, a disfrutar🔥")
                time.sleep(1.5)
            #quiebre del bucle con variable
            reiteration = False
        #interaccion si se inserta valores invalidos
        elif presentacion != "tiras" or presentacion != "normal":
            print("Ingrese un valor valido")
            presentacion = input("Como desea su pollo (tiras o normal): ").lower()

    #conversion de variable para trato futuro
    presentation = presentacion

#funcion para evitar alergias a la pimienta
def preparar_salsa_cesar(pimienta_negra_molida):
    #declaracion global de la pimienta
    global want
    #iniciador de bucle
    reiteration = True
    while reiteration == True:
        #condicional para evaluar si inserta valor positivo
        if pimienta_negra_molida == "si" or pimienta_negra_molida == "true":
            #quiebre de bucle
            reiteration = False
        #condicional para evaluar si inserta valor falso
        elif pimienta_negra_molida == "no" or pimienta_negra_molida == "false":
            #quiebre de bucle
            reiteration = False
        #interaccion si se inserta valores invalidos
        else:
            print("Ingrese un valor valido")
            pimienta_negra_molida = input("Como desea su pollo (tiras o normal): ").lower()


    #conversion de variable para trato futuro
    want = pimienta_negra_molida


#funcion para determinar los valores del directorio futuro
def preparar_ensalada_cesar():
    global thing
    global ingredients
    global steps
    thing = "ensalada"
    ingredients = ["1 lechuga costina grande","1 pechuga de pollo a la plancha", "½ taza de queso parmesano en lonjas o rallado grueso", "1 ½ taza de cubos de pan", "2 cucharadas de aceite de oliva","1 cucharadita de Pimentón Páprika "]
    steps = ["Calentar el horno a 200°C.", 
            "Para los crutones: Mezclar el pan con el aceite de oliva y con el pimentón páprika. Poner el pan en una lata de horno (en una sola capa). Hornear por 3 a 5 minutos o hasta que el pan esté crujiente y dorado", 
            "Poner la lechuga en un plato, rociar con el aliño. Decorar con el pollo, crutones y queso parmesano. Servir inmediatamente."]


#funcion para determinar los valores del directorio futuro
def preparar_wrap_cesar():
    global thing
    global ingredients
    global steps
    thing = "Wrap"
    ingredients = ["2 unidades PECHUGAS DE POLLO DESHUESADAS","4 unidades TORTILLAS DE HARINA", "4 unidades HOJAS DE LECHUGA", "1 taza TOMATES CHERRY EN MITADES", "1 taza PEPINOS EN BASTONES","Aderezo Caesar","SAL AL GUSTO", "ACEITE"]
    steps = ["Sazona las pechugas con la salsa de ajo y cocinalas en una sartén o a la parrilla.", 
            "Corta el pollo en tiras.", 
            "Coloca una tortilla en una superficie plana y sobre esta, pon una hoja de lechuga, tomates, pepino y tiras de pollo.",
            "Baña con aderezo caesar y agrega topping para ensalada caesar y enrolla para formar el wrap.",
            "Sirve el wrap con tu aderezo favorito."]


#funcion para determinar los valores del directorio futuro
def preparar_sandwich_pollo():
    global thing
    global ingredients
    global steps
    thing = "Sandwich"
    ingredients =  ["pan de sándwich", "queso", "lechuga", "tomate"],
    steps =  ["Tostar ligeramente el pan", "Colocar el pollo" , "Colocar queso", "agregar salsa"]


#funcion para asignar la posicion adecuada a las variables electas anteriormente y declarar como booleano el deseo de la pimienta
def emplatado():
    global want
    if eleccion == 1:
        preparar_ensalada_cesar()
        if want == "true" or want == "si":
            want = True
        elif want == "false" or want == "no":
            want = False
        else:
            print("Not valid input")
    elif eleccion == 2:
        preparar_wrap_cesar()
        if want == "true" or want == "si":
            want = True
        elif want == "false" or want == "no":
            want = False
        else:
            print("Not valid input")
        
    elif eleccion == 3:
        preparar_sandwich_pollo()
        want = False

    #directorio de producto
    product = {
            "receta": thing,
            "salsa":{
                "pimienta_negra": want,
                "sal" :  "al gusto",
                "zumo_limon" :  "10 ml"
            },
            "presentacion_pollo" : presentation,
            "ingredientes": ingredients,
            "pasos": steps
        }
    #funcion para formatting y desplegar el directorio con apariencia de json desde la consola
    pprint.pprint(product)


#iniciacion de codigo
main_menu()