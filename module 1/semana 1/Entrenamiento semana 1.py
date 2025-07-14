import os 
import time
global producto

"""calcular el costo total de compras de una tienda. El pŕograma debe interactuar con el usuario por inpu y pidiendo 4 datos escenciales
1 . nombre del producto ✅ 
2. precio por unidad del producto ✅ 
3. cantidad de productos comprados ✅ 
4. % de descuento ✅ 
5. si no aplica, podra ser 0% ✅ 
6. claridad en la interfaz """




#funcion para deteccion de errores en input, permite realizar el analisis de un input,
#toma los datos en parametros para el parsin y el input y los retorna como si se hubiera realizado
#un input directo permitiendo evitar la insersion de valores incorrectos en los campos deseados
def error_funtion(dato, texto):
 while True:
    try:
        variable = dato(input(texto))
        return variable
    except ValueError:
        print("| Dato incorrecto, intente de nuevo...")


#funcion para limpiar pantalla
def cls():
    os.system("clear")

#variables contenedoras de mensajes para formating
mensaje1 = "\033[1mBienvenido al sistema de calculo SM \033[0m"
mensaje2 = "Porfavor ingrese el numero del"
mensaje3 = "producto que desea comprar"
mensaje4 = "Ingrese porcentaje de descuento"
mensaje5 = "Que desea (sin %, max 100 min 0)"
mensaje6 = "Analizando por favor espere. "
mensaje7 = "Cuantas "
mensaje8 = "Si compra mas de 5 unidades de "
mensaje9 = "empieza a aplicar el descuento"
mensaje10 = " desea?"
mensaje11 = "Usted va a comprar "
mensaje12 = "No aplica descuento (0%)"
mensaje13 = "y va a pagar $"
mensaje14 = "En esta compra se ahorro $"
mensaje15 = " , con el descuento del"
rayita = "|"
subrayita = "-"
bajarayita = "_"
espacio = " "
flechita = ">"
igual = "="





#funcion de menu principal
def menu():
    #declaracion global de variables
    global producto
    global descuento_en_porcentaje
    global descuento

    #interfaz grafica de menu
    print((rayita + igual*180 + rayita) .center(95))
    print((rayita + espacio*63 + mensaje1 + espacio*(125-len(mensaje1)) + rayita).center(95))
    print((rayita + igual*180 + rayita) .center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*(78 - len(producto1))+ "1." + producto1 + rayita + "$" + (f"{precio1}") + espacio*(98 - len((f"{precio1}"))) + rayita).center(95))
    print((rayita + espacio*(78 - len(producto2))+ "2." + producto2 + rayita + "$" + (f"{precio2}") + espacio*(98 - len((f"{precio2}"))) + rayita).center(95))
    print((rayita + bajarayita*180 + rayita) .center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*63 + mensaje2 + espacio*(117-len(mensaje2)) + rayita).center(95))
    print((rayita + espacio*65 + mensaje3 + espacio*(115-len(mensaje3)) + rayita).center(95))
    
    #ingreso del id del producto deseado
    producto = error_funtion(int, (rayita + subrayita*2 + flechita))
    print((rayita + espacio*65 + mensaje4 + espacio*(115-len(mensaje4)) + rayita).center(95))
    print((rayita + espacio*65 + mensaje5 + espacio*(115-len(mensaje5)) + rayita).center(95))
    
    #ingreso del oircentaje de descuento deseado
    descuento = error_funtion(float, (rayita + subrayita*2 + flechita))
    print((rayita + espacio*65 + mensaje6 + espacio*(115-len(mensaje6)) + rayita).center(95))
    print((rayita + bajarayita*180 + rayita) .center(95))
    
    
    #pausa por cronometro virtual de 1,5 segundos
    time.sleep(1.5)

    #conversion interna del valor del descuento a decimales para procesamiento aritmetico
    descuento_en_porcentaje = descuento/100


#bucle principal del programa
while True:
    

    print("antes de empezar con el taller")
    print("porfavor ingrese los productos con que vamos a trabajar")

    #este try permite capturar excepciones, si ocurre algun error saltara al fragmento de exception, 
    #si se coloca algun valor diferente a un entero en los precios no dejara avanzar hasta ingresar el valor correcto
    #se aplica el uso de la funcion definida para deteccion de errores
    try:
        print("inserte producto 1")
        producto1 = error_funtion(str, "--> ")
        print("inserte producto 2")
        producto2 = error_funtion(str, "--> ")
        print("Y sus respectivos precios (sin el signo peso($))")
        print("precio 1:")
        precio1 =  error_funtion(int, "--> ")
        print("precio 2:")
        precio2 =  error_funtion(int, "--> ")
    

    #en caso de fallar el try solicita un reintento
    except:
        print("ingrese valores validos para cada campo")
        time.sleep(2)
        cls()
        continue
    
    menu()

    #Entra si el descuento es un valor valido, es decir es un numero superior a 0
    #En caso tal de entrar negativos no ejecutara el codigo principal y pedira reinsersion de datos
    if descuento >= 0:


        #Utiliza las opciones ofrecidas en el menu para decidir el camino de accion, el caso 1 o 2 dependiendo de la elección
        #Posee formating para entregar un entorno visualmente ameno
        match producto:
            case 1:
                cls()
                #Mensaje de aclaracion para el descuento, y consulta de cuantos productos desea comprar
                #Este segundo caso aplica al segundo producto solicitado
                #Posee formating para un entorno visualmente ameno    
                print((rayita + bajarayita*180 + rayita) .center(95))
                print((rayita + espacio*(81 - len(mensaje8))+ mensaje8 + producto1 + espacio* 98 + rayita).center(95))
                print((rayita + espacio*63 + mensaje9 + espacio*(117-len(mensaje9)) + rayita).center(95))
                print((rayita + espacio*180 + rayita) .center(95))
                print((rayita + igual*180 + rayita) .center(95))
                print((rayita + espacio*63 + mensaje7 + producto1 + mensaje10 + espacio*(117-len(mensaje7)) + rayita).center(95))
                cantidad_manzanas = error_funtion(int, "| --> ")
                print((rayita + bajarayita*180 + rayita) .center(95))

                #Operador logico, permite realizar una accion si no se llega al requerimiento de productos para el descuento
                if cantidad_manzanas < 5:

                    #Precio total y descuento invalido
                    precio = cantidad_manzanas * precio1
                    valor_descuento = 0

                    #Dialogo final de la compra sin descuento, expone precio a pagar y cuantos productos se van a comprar
                    #Posee formating para un entorno visualmente ameno
                    print((espacio*180) .center(95))
                    print((espacio*180) .center(95))
                    print((rayita + igual*180 + rayita) .center(95))
                    print((rayita + espacio*63 + mensaje11 + f"{cantidad_manzanas} " + producto1 + espacio*(100-len(mensaje11))).center(95))
                    print((rayita + espacio*63 + mensaje12 + espacio*(100-len(mensaje12))).center(95))
                    print((rayita + espacio*63 + mensaje13 + f"{precio:.5f}" + espacio*(100-len(mensaje12))).center(95))
                    print((rayita + espacio*63 + mensaje14 + f"{valor_descuento:.5f}" + espacio*(100-len(mensaje12))).center(95))

                    #funcion para permitir al usuario leer con tranquilidad y limpiar la pantalla
                    time.sleep(6)
                    cls()
                    break 

                if cantidad_manzanas >= 5:
                    #Valor real sin descuento
                    valor_real = cantidad_manzanas * precio1
                    
                    #Valor en pesos que obtienes tras aplicar el descuento
                    #Valor en pesos que obtienes tras aplicar el descuento, correspondiente al valor a deducir del precio total
                    valor_descuento = (cantidad_manzanas * precio1)* descuento_en_porcentaje

                    #Valor total a pagar
                    precio = valor_real - valor_descuento


                    #Dialogo final de la compra con descuento, expone el descuento en porcentaje
                    #Posee formating para un entorno visualmente ameno
                    print((espacio*180) .center(95))
                    print((espacio*180) .center(95))
                    print((rayita + igual*180 + rayita) .center(95))
                    print((rayita + espacio*63 + mensaje11 + f"{cantidad_manzanas} " + producto1 + mensaje15 + f" {descuento}%" + espacio*(100-len(mensaje11))).center(95)) #aqui el descuento
                    print((rayita + espacio*63 + mensaje13 + f"{precio:.5f}" + espacio*(100-len(mensaje12))).center(95))
                    print((rayita + espacio*63 + mensaje14 + f"{valor_descuento:.5f}" + espacio*(100-len(mensaje12))).center(95))
                    
                    #Funcion para permitir al usuario leer con tranquilidad y limpiar la pantalla
                    time.sleep(6)
                    cls()

                    #Agradecimiento y Despedida
                    print("\033[1mGracias por su compra\033[0m")
                    time.sleep(1.5)
                    cls() 
                    break        

            case 2: 
                #Mensaje de aclaracion para el descuento, y consulta de cuantos productos desea comprar
                #Este segundo caso aplica al segundo producto solicitado
                #Posee formating para un entorno visualmente ameno                
                cls()
                print((rayita + bajarayita*180 + rayita) .center(95))
                print((rayita + espacio*(81 - len(mensaje8))+ mensaje8 + producto2 + espacio* 98 + rayita).center(95))
                print((rayita + espacio*63 + mensaje9 + espacio*(117-len(mensaje9)) + rayita).center(95))
                print((rayita + espacio*180 + rayita) .center(95))
                print((rayita + igual*180 + rayita) .center(95))
                print((rayita + espacio*63 + mensaje7 + producto2 + mensaje10 + espacio*(117-len(mensaje7)) + rayita).center(95))
                cantidad_peras = error_funtion(int, "| --> ")
                print((rayita + bajarayita*180 + rayita) .center(95))

                #Operador logico, permite realizar una accion si no se llega al requerimiento de productos para el descuento
                if cantidad_peras < 5:

                    #precio total y descuento invalido
                    precio = cantidad_peras * precio2
                    valor_descuento = 0

                    #Dialogo final de la compra
                    #Posee formating para un entorno visualmente ameno
                    print((espacio*180) .center(95))
                    print((espacio*180) .center(95))
                    print((rayita + igual*180 + rayita) .center(95))
                    print((rayita + espacio*63 + mensaje11 + f"{cantidad_peras} " + producto2 + espacio*(100-len(mensaje11))).center(95))
                    print((rayita + espacio*63 + mensaje12 + espacio*(100-len(mensaje12))).center(95))
                    print((rayita + espacio*63 + mensaje13 + f"{precio:.5f}" + espacio*(100-len(mensaje12))).center(95))
                    print((rayita + espacio*63 + mensaje14 + f"{valor_descuento:.5f}" + espacio*(100-len(mensaje12))).center(95))

                    #Funcion para permitir al usuario leer con tranquilidad y limpiar la pantalla
                    time.sleep(6)
                    cls()

                    #Agradecimiento y despedida
                    print("\033[1mGracias por su compra\033[0m")
                    time.sleep(1.5)
                    cls()
                    break


                #Operador logico, permite realizar una accion si llega al requerimiento de productos para el descuento
                if cantidad_peras >= 5:
                    #Valor real sin descuento
                    valor_real = cantidad_peras * precio2
                    
                    #Valor en pesos que obtienes tras aplicar el descuento, correspondiente al valor a deducir del precio total
                    valor_descuento = (cantidad_peras * precio2)* descuento_en_porcentaje

                    #Valor total a pagar
                    precio = valor_real - valor_descuento


                    #Dialogo final de la compra
                    #Posee formating para un entorno visualmente ameno
                    print((espacio*180) .center(95))
                    print((espacio*180) .center(95))
                    print((rayita + igual*180 + rayita) .center(95))
                    print((rayita + espacio*63 + mensaje11 + f"{cantidad_peras} " + producto2 + mensaje15 + f" {descuento}%" + espacio*(100-len(mensaje11))).center(95)) #aqui el descuento
                    print((rayita + espacio*63 + mensaje13 + f"{precio:.5f}" + espacio*(100-len(mensaje12))).center(95))
                    print((rayita + espacio*63 + mensaje14 + f"{valor_descuento:.5f}" + espacio*(100-len(mensaje12))).center(95))

                    
                    #Funcion para permitir al usuario leer con tranquilidad y limpiar la pantalla
                    time.sleep(6)
                    cls()

                    #Agradecimiento y despedida
                    print("\033[1mGracias por su compra\033[0m")
                    time.sleep(1.5)
                    cls()
                    break


            case _:
                print("Valor invalido")
                print("Ingrese un producto existente")
                menu()


    elif descuento < 0:
        cls()
        print("ERROR")
        print("Valor invalido")
        print("Ingrese un descuento valido")
        time.sleep(3)
        cls()


#SANTIAGO ANDRÉS MENDOZA ALMANZA. 
# DE MI PARA RIWI.
# OIGAN MIREN EL CODIGO COMPLETO PORFA, ME DEMORE 10 HORAS FORMATEANDO
# CON ABSOLUTO CARIÑO Y DEDICACION, ESPERO LES GUSTE :D