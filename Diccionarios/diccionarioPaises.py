"""
definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes.
Implementar una función para mostrar cada clave y valor.
"""

def imprimir(paises):
    for clave in paises:
        print(clave, paises[clave])
        
#bloque principal
paises={"Ecuador": 16.800000, "Argentina":400.000000, "España":460.000000}
imprimir(paises)

