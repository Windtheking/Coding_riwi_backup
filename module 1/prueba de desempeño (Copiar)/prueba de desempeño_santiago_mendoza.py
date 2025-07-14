
import time
import pprint
import os

"""Como encargado del área digital de una librería nacional, necesitas un sistema robusto que no
solo permita registrar ventas y productos, sino también generar reportes detallados, aplicar
descuentos por cliente, agrupar estadísticas (cuantas ventas, cuantos libros de ese autor, cantidad de ligbros de ese autor en stock) por autor y evaluar el rendimiento del inventario
con base en ventas."""


"""
1. Gestión del inventario
• Registrar, consultar, actualizar y eliminar productos.
• Cada producto debe tener: título, autor, categoría, precio, cantidad en stock."""

"""
2. Registro y consulta de ventas
• Permitir registrar ventas de productos, asociando: cliente, producto vendido,
cantidad, fecha y descuento (si aplica).
• Validar stock disponible y actualizarlo automáticamente."""

"""3. Módulo de reportes
• Mostrar el top 3 de productos más vendidos.
• Generar reporte de ventas totales agrupado por autor.
• Calcular ingreso neto y bruto (con y sin descuento)"""

"""
4. Validaciones avanzadas
• Validar entradas (números positivos, formatos correctos, campos obligatorios).
• No permitir ventas con stock insuficiente"""

#Library stock
eternal_knowledge_library = {
                        "fantasy" : {
                            "the lord of the ring" : [500,84000,"mawoa"],
                            "syrlock meows" : [300,20000,"ewa"],
                            "the good, the bad and the horny" : [800,14000,"mawoa"]
                        },

                        "adventure":{
                            "wings of fire: the dragonet profecy": [5000,48000,"Tui T. Sutherland"],
                            "wings of fire: The brightest night": [1000,62000,"Tui T. Sutherland"]
                        }

                    }

#---------------------------------------------------------------------------------------------------------------------#
#formating functions

#empty line functions
def space(x):
    for i in range(x):
        print((rayita + espacio*180 + rayita) .center(95))

#formating for center tittle text
def formated_title_text(title):
    print((rayita + espacio*63 + title + espacio*(117-len(title)) + rayita).center(len(title)))

#formating for normal text
def formated_welcome_text(message):
    print((rayita + espacio*63 + message + espacio*(125-len(message)) + rayita).center(len(message)))

def formated_text(message):
    print((rayita + espacio*63 + message + espacio*(117-len(message)) + rayita).center(len(message)))

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
#Formated Welcoming message 
def welcome_message():
    formated_welcome_text("\033[1m Welcome.  \033[0m")
    formated_welcome_text("\033[1m To the eternal knowledge library\033[0m")
    formated_welcome_text("\033[1m internal data base\033[0m")
    formated_welcome_text("\033[1m please select you query\033[0m")


#---------------------------------------------------------------------------------------------------------------------#
#console clear function
def cls():
    os.system("clear")


#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
#error managin functions
def error_targeting(typo,text):
    x = True
    while x == True:
        try:
            chosen = typo(input(text))
            return chosen
        except:
            print("\033[33m| Invalid values detected, please insert a valid selection \033[0m")

def Yes_No(x):
    y = True
    while y == True:
        x.lower()
        if x == "y" or x == "n":
            return x
            y = False

        else:
            print("\033[33m| Invalid values detected, please insert a valid selection \033[0m")
#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
#main menu function, with cases and avoiding incorrect inputs
def main_menu():
    global main
    end = False
    print((rayita + igual*180 + rayita))
    formated_title_text("The eternal knowledge library")
    print((rayita + igual*180 + rayita))
    space(3)
    welcome_message()
    space(2)
    formated_text("1. Browse Inventory")
    formated_text("2. Costumer wants a book?")
    formated_text("3. Overall report")
    formated_text("4. Exit")

    while end == False:
        #input for recieving the selected query
        selected_query = error_targeting(int, "\033[32m| --> \033[0m")
        
        #cases depending on the query that was selected
        match selected_query:
            case 1:
                cls()
                print((rayita + igual*180 + rayita))
                formated_text("You selected option 1 Browse inventory")
                formated_text("Presione enter para continuar . . .")
                print((rayita + igual*180 + rayita))
                input()
                cls()
                end = False
                browse_inventory()
            case 2:
                cls()
                print((rayita + igual*180 + rayita))
                formated_text("You selected option 2 Sell products")
                formated_text("Presione enter para continuar . . .")
                print((rayita + igual*180 + rayita))
                input()
                cls()
                costumer_wants_a_book()
                end = False

            case 3:
                cls()
                print((rayita + igual*180 + rayita))
                formated_text("You selected option 3 overall report")
                formated_text("Presione enter para continuar . . .")
                print((rayita + igual*180 + rayita))
                input()
                cls()
                Overall_report()
                end = False

            case 4:
                formated_text("Thank you for your time")
                formated_text("Have a good day")
                input()
                exit()
            case _:
                print("\033[33m| Invalid values detected, please insert a valid selection \033[0m")

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
def browse_inventory():
#   global main
    global y
    print((rayita + igual*180 + rayita))
    formated_text("What would you like to do today?")
    print((rayita + igual*180 + rayita))
    formated_text("1. Register a new book?")
    formated_text("2. Consult the database for books?")
    formated_text("3. Update a book's info?")
    formated_text("4. Delete a book from the database?")
    formated_text("5. Go back to main menu")
    
    y = True
    while y == True:
        inventory_selection = error_targeting(int, "\033[32m| --> \033[0m")
        if inventory_selection > 0 and inventory_selection < 6:
            y = False
            
        else:
            print("\033[33m| Invalid values detected, please insert a valid selection \033[0m")

        match inventory_selection:
            case 1:
                cls()
                add_book_to_database()
                y = False
                browse_inventory()
            case 2:
                cls()
                consult_book()
            case 3:
                cls()
                update_stock_books()
            case 4:
                cls()
                delete_book_from_database()
            case 5:
                cls()
                main_menu()
            case _:
                print("\033[33m| Invalid values detected, please insert a valid selection \033[0m")


#add on function
def add_book_to_database():
    formated_text("Do you want to insert a new category of books? Y/N")
    answer1 = error_targeting(str, "\033[32m| --> \033[0m")
    Yes_No(answer1)
    if answer1 == "y":
        formated_text("Inser the new category name")
        new_category = error_targeting(str, "\033[32m| --> \033[0m")
        eternal_knowledge_library[f"{new_category}"] = {}
        pprint.pprint(eternal_knowledge_library)
        input()
    elif answer1 == "n":
        formated_text("You selected to insert:")
        formated_text("New book to existing category")
        formated_text("Please insert the existing category you want to update")
        existing_category = error_targeting(str, "\033[32m| --> \033[0m")
        
        formated_text("Please insert the subcategory you want to update")
#        formated_text("Please note, if you insert an unexisting subcategory you'll be notified")
        subcategory = error_targeting(str, "\033[32m| --> \033[0m")
       
        formated_text("Please insert the stock count of the new book")
        sotck_count = error_targeting(int, "\033[32m| --> \033[0m")
        
        formated_text("Please insert the price of the new book")
        price = error_targeting(int, "\033[32m| --> \033[0m")
        
        formated_text("Please insert the author of the new book")
        author = error_targeting(str, "\033[32m| --> \033[0m")
        
        checking = eternal_knowledge_library.get(f"{existing_category}","None existent")
        if checking != "Inesxistente":
            checking2 = eternal_knowledge_library.get(f"{existing_category}{subcategory}","None existent")
            print(checking2)
            if checking2 != "None existent":
                formated_text("Usted ingreso un libro ya existente")
            elif checking2 == "None existent":
                eternal_knowledge_library[f"{existing_category}"][f"{subcategory}"] = [sotck_count, price, author]

        pprint.pprint(eternal_knowledge_library)
#consult data function
def consult_book():
        
        print((rayita + igual*180 + rayita))
        formated_text(("\033[1m  Books avalible based of category\033[0m").center(45))
        print((rayita + igual*180 + rayita))
        
        for key in eternal_knowledge_library.keys():
                print("|", "_"*178,"|")
                formated_text((f"\033[1m{key}\033[0m").center(45))
        
        print("|", "_"*178,"|")
        space(1)
        formated_text(("\033[1m  Insert the category you want to know about\033[0m").center(45))
        subcategory = error_targeting(str, "\033[32m| --> \033[0m").lower()
        comprobant = eternal_knowledge_library.get(f"{subcategory}","None existent")

        
        #si el directorio no existe se muestra un mensaje de inexistencia
        if comprobant == "None existent":
            print("|","="*178 ,"|")
            formated_text((f"The subdirectory is {comprobant}"))
            formated_text("press enter to go back to menu")
            print("|","="*178 ,"|")
            input()
            cls()
            browse_inventory()


        #si el directorio existe se muestran los productos y sus valores
        if comprobant != "None existent":
            print("|", "="*178,"|")
            formated_text(f"Subdirectorios de {subcategory}")
            print("|", "="*178 , "|")
            space(1)
            formated_text("Author" + " | " + "Stock" + " | " + "Price")
            for key, valu in eternal_knowledge_library[f"{subcategory}"].items():
                print("|", "_"*178, "|")
                space(1)
                content = f"{key}" + " | " +  f"{valu[0]}" + " | " + f"${valu[1]:.2f}"
                formated_text((content.center(35)))
            print("|","="*178 ,"|")
            formated_text("press enter to go back to menu")
            input()
            cls()
            browse_inventory()


#Update values function
def update_stock_books():
    print((rayita + igual*180 + rayita))
    formated_text("What do you want to update?")
    space(2)
    formated_text("1. Price")
    formated_text("2. Stock")
    formated_text("3. Author")
    formated_text("Choose the number of what you want to update")
    print((rayita + igual*180 + rayita))
    option_selected = error_targeting(int,"| --> ")
   
    
   
    #caso de actualizacion de precio


    def model1(value, place):
        update = error_targeting(int, f"| Insert new {value}: ")
        directory1 = error_targeting(str, "| Insert book category name: ")
        checking = eternal_knowledge_library.get(f"{directory1}","None existent")
        directory2 = error_targeting(str, "| Insert the book name to update: ")
        if checking != "None existent":
            checking1 = eternal_knowledge_library[f"{directory1}"].get(f"{directory2}","None existent")
        else:
            checking1 = "None existent"

        if checking != "None existent" and checking1 != "None existent":

            if update == 0:
                update = "Not in stock"
            
            eternal_knowledge_library[f"{directory1}"][f"{directory2}"][place] = (update)
        if checking == "None existent" or checking1 == "None existentistente":
            print("|","="*178 ,"|")
            formated_text(f"The genre {directory1} with the book {directory2} are {checking}")
            input("\npress enter to go back")

    def model2(value, place):
        update = error_targeting(str, f"| Insert new {value}: ")
        directory1 = error_targeting(str, "| Insert book category name: ")
        checking = eternal_knowledge_library.get(f"{directory1}","None existent")
        directory2 = error_targeting(str, "| Insert the book name to update: ")
        if checking != "None existent":
            checking1 = eternal_knowledge_library[f"{directory1}"].get(f"{directory2}","None existent")
        else:
            checking1 = "None existent"

        if checking != "None existent" and checking1 != "None existent":

            if update == 0:
                update = "Not in stock"
            
            eternal_knowledge_library[f"{directory1}"][f"{directory2}"][place] = (update)
        if checking == "None existent" or checking1 == "None existentistente":
            print("|","="*178 ,"|")
            formated_text(f"The genre {directory1} with the book {directory2} are {checking}")
            input("\npress enter to go back")

    match option_selected:
        case 1:
            model1("price", 1)
    #caso de actualizacion de stock
        case 2:
            model1("stock", 0)

        case 3: 
            model2("Author", 3)
        case _:
            formated_text("\033[33m| Invalid values detected, please insert a valid selection \033[0m")
            time.sleep(2)
            cls()
            update_stock_books()
#delete data function
def delete_book_from_database():
    election = error_targeting(str, "Insert the name of the genre of book you want to explore: ")
    cheking = eternal_knowledge_library.get(f"{election}","None existent")
    directory1 = error_targeting(str, "Insert the book you want to delete: ")
    #comporbacio de existencia
    if cheking == "None existent":
        print(rayita + igual*180 + rayita)
        formated_text((f"The asked book is {cheking}").center(100))
        input("Press enter to go back to menu")
        print(rayita + igual*180 + rayita)
        input()
        cls()
        browse_inventory()
    
    elif cheking != "None existent":
        print(rayita + igual*180 + rayita)
        formated_text(f"the book {directory1} will be deleted from the genre {election}")
        #busqueda del valor por directorio y producto
        try:
            del eternal_knowledge_library[f"{election}"][f"{directory1}"]
            formated_text(f"The book {directory1} has been deleted properly from '{election}' ")
        except:
            formated_text(f"the book {directory1} does not existe in the genre {election}")
       
        formated_text("Press enter to go back to menu")
        print(rayita + igual*180 + rayita)
        input()
        cls()
        browse_inventory()
            
#---------------------------------------------------------------------------------------------------------------------#


current_sales = []
books = []
#Receipt function for sales
def costumer_wants_a_book():
    global current_sales
    dates = []

    print((rayita + igual*180 + rayita))
    formated_text("Now, the client wants a book?")
    formated_text("(If entered by mistake insert 1 to go back)")
    formated_text("Ask the client what genre is he/she buying")
    decision = error_targeting(str, "\033[32m| --> \033[0m").lower()

    if decision == "1":
        cls()
        main_menu()


    formated_text("and what book is he/she buying")
    fate = error_targeting(str, "\033[32m| --> \033[0m").lower()
    books.append(fate)

    formated_text("whats the name of the costumer?")
    name = error_targeting(str, "\033[32m| --> \033[0m").lower()
    formated_text("how many books are desired?")
    formated_text("if more than 10 applies 20 percent off")
    count = error_targeting(int, "\033[32m| --> \033[0m")
    formated_text("Insert today's date separated by slashes(/) ")
    date = error_targeting(str, "\033[32m| --> \033[0m").lower().split("/")
    

    price = eternal_knowledge_library[f"{decision}"][f"{fate}"][1]
    
    #descuento
    if count >= 10:

        discount = lambda x: x * 0.2
        discount(price)
        total_price = (price*count) - discount
        discounted = "Valid"

    elif count < 10:

        total_price = price * count
        discounted = "Invalid"


    vital_stok = eternal_knowledge_library[f"{decision}"][f"{fate}"][0]

    if vital_stok < count:
        print((rayita + igual*180 + rayita))
        formated_text("Imposible to sell, not enough books in stock")
    else: 
        current_stock = vital_stok - count
        eternal_knowledge_library[f"{decision}"][f"{fate}"][0] = (current_stock)

    cls()
    print((rayita + igual*180 + rayita))
    formated_text("Costumers receipt")
    formated_text(f"the client {name}")
    formated_text(f"bought {count} copies the book {fate}")
    formated_text(f"(Discount: {discounted})")
    formated_text(f"In the day {dates[0]}/{dates[1]}/{dates[2]}")
    formated_text(f"total to pay {total_price}")
    current_sales.append(total_price)
    print(total_price)
#overall report for not working funcions
def Overall_report():
    global current_sales
    value = 0
    print((rayita + igual*180 + rayita))
    formated_title_text("Welcome admin, here is the overall report")
    print((rayita + igual*180 + rayita))
    space(3)

    formated_text("would you like to know the top 3 best sellers?Y/N")
    Y_N = Yes_No(error_targeting(str, "\033[32m|--> \033[0m"))
    if Y_N == "y":
        try:
            for book in books:
                x = books[0]
                y = books[1]
                z = books[2]
                if book == x:
                    value += 1
                if book == y:
                    value1 += 1
                if book == z:
                    value2 += 1

            if value > value1 <value2:
                print(f"the 3 best sellers where {x},{y},{z}")
            if value1 > value2 <value:
                print(f"the 3 best sellers where {x},{y},{z}")
            if value2 > value <value1:
                print(f"the 3 best sellers where {x},{y},{z}")
        except:
            formated_text("An exception has occurred we are sorry for the malfunction, you will see this feature working soon")
            formated_text("Thank you for you patience")

    elif Y_N == "n":
        formated_text("OKay! going total sales made by author")
        time.sleep(2)
    
    formated_text("would you like to know the total sales made by author?")
    Y_N = Yes_No(error_targeting(str, "\033[32m|--> \033[0m"))
    if Y_N == "y":
        try:
            1 + 1 == False
            print(empty)
           
        except:
            formated_text("An exception has occurred we are sorry for the malfunction, you will see this feature working soon")
            formated_text("Thank you for you patience")

    elif Y_N == "n":
        formated_text("OKay! going to income")
        time.sleep(2)

    formated_text("would you like to know brute and total income? Y/N")
    Y_N = Yes_No(error_targeting(str, "\033[32m|--> \033[0m"))
    if Y_N == "y":
        iteration = True

        formated_text("Insert total moth investment ")
        outs = error_targeting(int, "\033[32m|--> \033[0m")
        outs.isnumeric()
        if outs < 1:
            formated_text("\033[33mInvalid values detected, please insert a valid selection \033[0m")
            outs = error_targeting(int, "\033[32m|--> \033[0m")
        else:
            gross_income = sum(current_sales)
            net_income = gross_income - outs
            formated_text(f"the net income from this month is {net_income} and the gross income is {gross_income}")
            formated_text("Going back to main menu")
            time.sleep(2)
            iteration = False
            cls()
            main_menu()
    elif Y_N == "n":
        formated_text("Understood going back to main menu")
        time.sleep(1)
        cls()
        main_menu()
    
    
        
                




#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#


rayita = "|"
subrayita = "-"
bajarayita = "_"
espacio = " "
flechita = ">"
igual = "="





main_menu()