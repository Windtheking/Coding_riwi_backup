def calcularResta(PrimerValor: int, SegundoValor: int) -> int:
    resultado = float(PrimerValor) - float(SegundoValor)
    return resultado

"""PrimerValor = 2
SegundoValor = 3"""

PrimerValor = input("Ingrese el primer valor: ")
SegundoValor = input("Ingrese el segundo valor: ")


response = calcularResta(PrimerValor, SegundoValor)
print(type(response).__name__)
print(response)