
"""
Definir por asignación una lista con 8 elementos enteros.
 cuantos de dichos valores almacenan un valor superior a 100.
"""

elementos=[800, 120, 99, 29, 280]
cantidad=0
x=0
while x<len(elementos):
    if elementos[x]>100:
        cantidad=cantidad+1
        x=x+1
print("La lista esta constituida por los elementos:")
print(elementos)
print("La cantidad de valores mayores  100 en la lista son:")
print(cantidad)
        