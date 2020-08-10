"""
Definir una lista y mostrar por pantalla
solo los elementos con valor iguales o superior a 7

"""

lista=[8,1,9,2,10]
x=0
print("Elementos de la lista con valores iguales o superiores a 7")
while x<len(lista):
    if lista[x]>=7:
        print(lista[x])
    x=x+1
    