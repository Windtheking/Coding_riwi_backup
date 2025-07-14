import os
import time

def valicadion_calificacion(calificacion: float):
        return 0 <= calificacion <= 100 




def error_funtion(dato, texto):
    while True:
        try:
            variable = dato(input(texto))
            return variable
        except ValueError:
            print("\033[1m|\033[0m"  "\033[31m Dato incorrecto, intente de nuevo...\033[0m")


#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#

def repetir_variables():
    while constante == True:
        print("Cuantas notas va a ingresar?")
        error_funtion(int, "--> ")
        

#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#

def cls():
    os.system("clear")

#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#


def sorting_notes():
    if notes <= 59:
        print("Desempeño bajo. Reprobado")
    elif notes <=79 and notes >= 60:
        print("Desempeño basico. Aprobado")
    elif notes <= 94 and notes >=80:
        print("Desempeño alto. Aprobado")
    elif notes == 100 or notes >=95 and notes < 100:
        print("Desempeño superior. Aprobado")
    elif notes > 100:
        print("| Promedio excede 100. Ingrese valor valido")

#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#

def desea_insertar_mas():
    print(" ")
    print("Desea insertar mas notas? Y/N")
    print(" ")

#----------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------#

def match_menu():
    global notes
    match selection:
        case 1:
            repetition = True

            print(" ")
            print("Planilla del estudiante")

            print(" ")
            print("Ingrese las notas del estudiante (0-100)")
            print(" ")
            notes = round(error_funtion(float, "| --> "))
            sorting_notes()
            print(" ")
            print("Desea insertar mas notas? Y/N")
            print(" ")
            yes_or_no = error_funtion(str, "| --> ").upper()

            while repetition == True:

                if yes_or_no == "Y":
                    print(" ")
                    print("Ingrese las notas del estudiante (0-100)")
                    print(" ")
                    notes = round(error_funtion(float, "| --> "))
                    sorting_notes()
                    desea_insertar_mas()
                    yes_or_no = error_funtion(str, "| --> ").upper()

                    cls()


                elif yes_or_no == "N":
                        
                        print("Gracias por su tiempo")
                        time.sleep(1.5)
                        cls()
                        repetition = False
                        menu()

                else:
                    print("valor incorrecto, ingrese un valor valido")
                    time.sleep(1.5)
                    cls()
                    desea_insertar_mas()
                    election = error_funtion(str, "| --> ").upper()
                    repetition = True
        
        #----------------------------------------------------------------------------------------------------#
        #----------------------------------------------------------------------------------------------------#

        case 2:

        case 3:
            pass
        
        case 4:
            pass

        case 5:
            cls()
            print("gracias por su tiempo")
            time.sleep(1.5)
            exit()

        case _:
            print("Ingrese una opcion valida")

#----------------------------------------------------------------------------------------------------#
# #----------------------------------------------------------------------------------------------------#
# # #----------------------------------------------------------------------------------------------------#       




mensaje1 = "\033[1mInstitucion educativa San sanjacinto \033[0m"
mensaje2 = "Planilla de notas del grado n"
mensaje3 = "\033[30mIngrese el procedimiento que desea evaluar\033[0m"
mensaje4 = "1) Ingresar notas"
mensaje5 = "2) Promediación de notas"
mensaje6 = "3) Comparacion de calificacion"
mensaje7 = "4) Busqueda de calificacion"
mensaje8 = "5) Salir del programa"
mensaje9 = "\033[1mEscoja el numero de la opcion que desea ejecutar\033[0m"
rayita = "|"
subrayita = "-"
bajarayita = "_"
espacio = " "
flechita = ">"
igual = "="




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



while True:
    menu()


