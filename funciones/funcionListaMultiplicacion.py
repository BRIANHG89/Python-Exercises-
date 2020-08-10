#cargar 5 enteros y un segundo parámetro de tipo entero
#dentro de la función mostrar cada elemento 

def multiplicar(lista,va):
    for x in range(len(lista)):
        multi=lista[x]*va
        print(multi)
        
# bloque principal

lista=[3, 7, 8, 10, 2]
print("Lista original:", lista)
print("Lista multiplicando cada elemento por 3")
multiplicar(lista,3)


