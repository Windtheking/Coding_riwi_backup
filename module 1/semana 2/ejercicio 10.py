"""1. Solicita al usuario que ingrese una palabra 
   2. Solo puedes usar un único ciclo, ya sea for o while, para comparar letra por letra. """


#Solicita insertar la palabra que se va a evaluar
palin = input("Insert a word: ")

#se declara la lista para su llamada futura
inverted_word = [] 

#Este bucle for recorre con un iterador la palabra ingresada con el input

#Uno a uno los va leyendo e insertando en la lista de inverted_word

#La lectura de estos caracteres es invertida debido al haber seteado el start stop step 
#para iniciar en la longitud maxima de la palabra insertada

#Se establece el start tambien con un -1 para que el indexado no presente conflictos con
#el start stop ya que el len lee la cantidad de caracteres y empieza en 1 mientras que el 
#indexado empieza en 0

for pal in range(len(palin)-1, -1, -1):

   #Contiene en una variable cada caracter de la palabra insertada
   inverted = palin[pal]

   #Inserta dentro de la lista creada anteriormente cada caracter por cada iteracion del bucle
   inverted_word.append(inverted)
   

#La variable reverse_word contiene la palabra de la lista convertida a string
#La funcion .join con las '' vacias une todos los valores de la lista sin espacios
#Se tiene que colocar el nombre de la lista en el argumento de la funcion para que la identifique 
reverse_word = ''.join(inverted_word)

#Hacer un if y elif para hacer la comparacion, si la nueva variable es igual a palin
#Dira que es palindroma si no coinciden dira que no lo es
if palin == reverse_word:
   print("")
   print("\n Si es Palindromo")
   print("")
elif palin != reverse_word:
   print("\n No es palindromo")
