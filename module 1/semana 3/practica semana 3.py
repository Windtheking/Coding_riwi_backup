#def suma(a: int, b: int) -> int:    
"""    
    Suma dos numeros enteros.
    
    Args:
        a (int): primer numero entero
        b (int): Segundo numero entero
    
    Returns:
        int: Resultado de la suma de a y b
    """
#    return a + b


auto_cayena = {
    "sedan" : {
        "marcas": ["Kia", "Toyota"],
        "modelos": ("k3","fortuner")
    },        #La clave se asigna como su mismo valor si no esta con el modelo "clave" : "valor" 
    "suv" : {
        "marcas": ["Kia", "Toyota"],
        "modelos": ("k3 cross","rav")
    },
}


for data in auto_cayena.items():
    print(data)


frutas = {
        "dulce" : ["Manzana","Fresas"],
        "indice_peso" : "100" 

}