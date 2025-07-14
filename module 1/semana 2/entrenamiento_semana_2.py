import os
import time




#Funcion para deteccion de errores al ingresar valores
def error_funtion(dato, texto):
    while True:
        try:
            variable = dato(input(texto))
            return variable
        except ValueError:
            print("\033[1m|\033[0m"  "\033[31m Dato incorrecto, intente de nuevo...\033[0m")


#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#

#Funcion para limpiar pantalla
def cls():
    os.system("clear")

#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#

#Funcion para sortear las notas entre aprobatorias y no aprobatorias
def sorting_notes():
    global notes
    if notes <= 59:
        print("| Desempeño bajo. Reprobado")
        time.sleep(1.5)
    elif notes <=79 and notes >= 60:
        print("| Desempeño basico. Aprobado")
    elif notes <= 94 and notes >=80:
        print("| Desempeño alto. Aprobado")
    elif notes == 100 or notes >=95 and notes < 100:
        print("| Desempeño superior. Aprobado")
    elif notes > 100:
        print("| Promedio excede 100. Ingrese valor valido")


#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#


#Confirmacion para seguir el proceso vigente, con S o N
def desea_insertar_mas():
    print((rayita + igual*180 + rayita) .center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*63 + mensaje12 + espacio*(117-len(mensaje12)) + rayita).center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + igual*180 + rayita))

#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#


#Menu principal retenido en una funcion
def match_menu():
    #declaracion global de variable
    global notes
    
    match selection:
        #1ra opcion del menu
        case 1:
            cls()
            repetition = True

            print(" ")
            print("Planilla del estudiante")

            print(" ")
            print("Ingrese las notas del estudiante (0-100)")
            print(" ")
            #funcion anteriomente mencionada, capaz de evitar ingreso de tipo de dato erroneo
            notes = round(error_funtion(float, "| --> "))
            sorting_notes()
            desea_insertar_mas()
            yes_or_no = error_funtion(str, "| --> ").upper()

            #Bucle que permite la reiteracion del proceso vigente o su terminacion para regresra al menu principal
            while repetition == True:
                #Condicional de si, continua el proceso 
                if yes_or_no == "Y":
                    cls()
                    print(" ")
                    print("Ingrese las notas del estudiante (0-100)")
                    print(" ")
                    notes = round(error_funtion(float, "| --> "))
                    sorting_notes()
                    desea_insertar_mas()
                    yes_or_no = error_funtion(str, "| --> ").upper()
                    cls()

                #condicional de no, termina el proceso y salta al menú
                elif yes_or_no == "N":
                        
                        print("Gracias por su tiempo")
                        time.sleep(1.5)
                        cls()
                        repetition = False
                        menu()


                #resultado si no, permite evitar el ingreso de valores inadecuados
                else:
                    print("valor incorrecto, ingrese un valor valido")
                    time.sleep(1.5)
                    cls()
                    desea_insertar_mas()
                    election = error_funtion(str, "| --> ").upper()
                    repetition = True
        #2daa opcion del menu
        case 2:
            #limpieza de pantalla y declaracion global de variable
            cls()
            global temporal

            #listas involucradas
            temporal = []
            average = []
            invalid = []
            #variable que marca inicio de bucle
            repetition = True
            
            #interfaz que solicita una lista de numeros separadas por comas
            print((rayita + igual*180 + rayita))
            print((rayita + espacio*63 + mensaje10 + espacio*(117-len(mensaje10)) + rayita).center(95))            
            print((rayita + espacio*180 + rayita) .center(95))
            print((rayita + espacio*180 + rayita) .center(95))
            print((rayita + espacio*53 + mensaje11 + espacio*(127-len(mensaje11)) + rayita).center(95))
            print((rayita + igual*180 + rayita))  
            notes = error_funtion(str, "| --> ").upper().split(",")
            print((rayita + igual*180 + rayita))


            

            desea_insertar_mas()
            election = error_funtion(str, "| --> ").upper()
            
            #bucle while que permite 
            while repetition == True:


                if election == "Y":
                    print((rayita + igual*180 + rayita))
                    print((rayita + espacio*53 + mensaje11 + espacio*(127-len(mensaje11)) + rayita).center(95))  
                    notes = error_funtion(str, "| --> ").upper().split(",")
                    print((rayita + igual*180 + rayita))

                    #en caso de recibir respuesta positiva a ingresas nuevos datos, 
                    #replite el proceso de analisis de lista y parseado de la misma
                    try:
                        for note in notes:
                            parsed = float(note)

                            if parsed <= 100 and parsed >= 0:
                                average.append(parsed)

                            elif not parsed.isdigit():
                                invalid.append(parsed)
                            else:
                                cls()
                                print("valor incorrecto")
                                cls()
                                invalid.append(parsed)

                    except:
                        cls()
                        print("Valores ingresados invalidos porfavor intente denuevo")

                    desea_insertar_mas()
                    election = error_funtion(str, "| --> ").upper()
            
            
                elif election == "N":
                    try:
                        #Analisis indexado de los elementos de  la lista y parseo a float para operarlos 
                        for note in notes:
                            cls()
                            parsed = float(note)
                            #print(parsed)
                            if parsed <= 100 and parsed >= 0:
                                average.append(parsed)
                                temporal.append(parsed)

                                #print(average)
                            else:
                                cls()
                                print("valor incorrecto")
                                cls()
                                invalid.append(parsed)
                    except:
                        #excepcion que permite analizar datos y evitar ingreso de valores equivocados
                        print("Valores invalidos ingresados han sido omitidos")      
                    
                    #Analizador de lista de valores invalidos, expresa cuales fueron los caracteres invalidos
                    if len(invalid) > 0:
                        cls()
                        print(invalid)
                        print(f"\nusted ingreso {len(invalid)} valores invalidos, y fueron omitidos\n")
                        time.sleep(1.5)

                    #Condicional evaluador de si la lista tiene valores y proceso aritmetico
                    if len(average) > 0:
                        cls
                        promedio = sum(average)/len(average)
                        print(f"\nel promedio de notas del estudiante es {promedio:.1f}\n")


                        #Declaracion de equivalncia de variables para poder hacer funcional la funcion de flitro de notas 
                        notes = promedio
                        sorting_notes()

                        input("| presione enter para continuar")
                        print("| Gracias por su tiempo")
                        repetition = False
                        time.sleep(1)
                        cls()
                        menu()
                    
                    #ruta alternativa que analiza si las listas estan vacias
                    if len(average) == 0 and len(invalid) == 0:
                        print("sus valores ingresados no son validos, regresando al menu principal")
                        cls()
                        menu()
            
                #previene el ingreso de valores invalidos
                else:
                    print("valor incorrecto, ingrese un valor valido")
                    time.sleep(1.5)
                    cls()
                    desea_insertar_mas()
                    election = error_funtion(str, "| --> ").upper()
                    Repetition = True
        

        #3ra opcion del menu
        case 3:
            #variable de iniciazion del bucle
            bucle = True
            #bucle while
            while bucle == True:
                #contador de numeros mayores que el ingresado
                cantidad_variabes_mayores = 0
                
                #Enunciado informativo
                print("Interfaz de conteo y filtrado")
                print("Ingrese la nota que desea buscar")
                
                #variable de ingreso de datos
                para_buscar = error_funtion(float, "| -->")

                #Recorrido de la lista para analizar los elementos internos y comparar si es mayor a la variable dada
                #con tal de permitir un conteo apropiado de cuantos valores son mayores al
                for i in range(len(temporal)):
                    
                    #variable de conversion de iterador
                    counter = temporal[i]

                    #condicional if que permite comparar                    
                    if counter > para_buscar:
                        cantidad_variabes_mayores += 1
                

                #Texto informativo sobre la busqueda y metodo interactivo con el usuario para avanzar 
                print(f"Usted busco la nota {para_buscar} y se encontraron {cantidad_variabes_mayores} nota(s) mayor(es)")
                input("Presione enter para continuar")
                cls()
                #finalizacion del bucle 
                bucle = False
        
        case 4:
            #variables de conteo iniciadas en 0
            quantity =  0
            point_stop = 0
            #texto informativo
            print("\nInterfaz de conteo y filtrado")
            print("\nIngrese la nota que desea buscar\n")
            para_buscar = error_funtion(float, "| -->")

            #for iterador sobre la lista
            for i in range(len(temporal)):

                similarity = temporal[i]


                try:
                    #Bloque condicional que permite analizar si el valor que contiene es similar al que lo estan comparadno 
                    
                    if similarity == para_buscar:
                        quantity += 1
                        point_stop += 1
                    
                    #Si point stop llegar a 5 repeticiones enseñara el mensaje de repeticiones maximas pero preguntara si se desean mas detalles
                    if point_stop > 5:
                        print("\nSe encontraron mas de 5 coincidencias con las notas\n")
                        print("\n¿Desea ver mas a detalle cuantas notas fueron?\n")
                        answer = error_funtion(str, "N/Y  -->").upper()
                        if answer.isalpha():
                            #En caso positivo, imprime mensaje detallado
                            if answer == "Y":
                                print(f"Usted busco la nota {para_buscar} y se encontraron {quantity} coincidencias")
                            #En caso negativo despide del usuario
                            elif answer == "N":
                                print("\nGracias por su tiempo\n")
                    
                            #En caso diferente de cualquiera de los dos ingresa un mensaje de error y pide denuevo el input
                            elif answer != "Y" or answer != "N":
                                print("ingrese un valor correcto")
                                answer = error_funtion(str, "N/Y  -->").upper()
                        else:
                            print("ingrese un valor correcto")
                            answer = error_funtion(str, "N/Y  -->").upper()
                    #si el contador no llega a 5 dara el mensaje detallado de una manera u otra
                    elif point_stop < 5:
                         print(f"Usted busco la nota {para_buscar} y se encontraron {quantity} coincidencias")
                         input("presione enter para continuar")
                #Atrapa errores en caso de no existir valores de ese tipo que se consulta
                except:
                    print("no existen coincidencias")
                    break
                    cls()

        #Funcion de despedida
        case 5:
            cls()
            print("Gracias por su tiempo")
            time.sleep(1.5)
            exit()

        #caso deffault si sucede algo por fuera de los establecidos informara el error por parte del usuario
        case _:
            cls()
            print("Ingrese una opcion valida")
            time.sleep(1)

#----------------------------------------------------------------------------------------------------#
# #----------------------------------------------------------------------------------------------------#
# # #----------------------------------------------------------------------------------------------------#       



#Variables contenedoras de texto
mensaje1 = "\033[1mInstitucion educativa San sanjacinto \033[0m"#
mensaje2 = "Planilla de notas del grado n"
mensaje3 = "\033[30mIngrese el procedimiento que desea evaluar\033[0m"
mensaje4 = "1) Rangos de desemepeño en notas"
mensaje5 = "2) Promediación de notas"
mensaje6 = "3) Comparacion de calificacion"
mensaje7 = "4) Busqueda de calificacion"
mensaje8 = "5) Salir del programa"
mensaje9 = "\033[1mEscoja el numero de la opcion que desea ejecutar\033[0m"
mensaje10 = "Planilla de promedio del estudiante"
mensaje11 = "Ingrese la lista de notas separada por comas(0 - 100)"
mensaje12 = "Desea insertar mas notas? Y/N"
rayita = "|"
subrayita = "-"
bajarayita = "_"
espacio = " "
flechita = ">"
igual = "="



#Interfaz grafica
def menu():
    global selection
    print((rayita + igual*180 + rayita))
    print((rayita + espacio*63 + mensaje1 + espacio*(125-len(mensaje1)) + rayita).center(95))
    print((rayita + igual*180 + rayita) .center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*63 + mensaje2 + espacio*(117-len(mensaje2)) + rayita).center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*58 + mensaje3 + espacio*(131-len(mensaje3)) + rayita).center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + bajarayita*180 + rayita) .center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*58 + mensaje9 + espacio*(130-len(mensaje9)) + rayita).center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*65 + mensaje4 + espacio*(115-len(mensaje4)) + rayita).center(95))    
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*65 + mensaje5 + espacio*(115-len(mensaje5)) + rayita).center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*65 + mensaje6 + espacio*(115-len(mensaje6)) + rayita).center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*65 + mensaje7 + espacio*(115-len(mensaje7)) + rayita).center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    print((rayita + espacio*65 + mensaje8 + espacio*(115-len(mensaje8)) + rayita).center(95))
    print((rayita + espacio*180 + rayita) .center(95))
    selection = error_funtion(int, "| --> ")
    print((rayita + bajarayita*180 + rayita) .center(95))
    match_menu()


#iniciador del menu principal
while True:
    menu()


