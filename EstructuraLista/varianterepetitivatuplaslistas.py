
#cargar 5 enteros
#imprimir en forma completa
#obtener y mostrar el mayor 
#mostrar la suma de todas sus componentes
#usar la nueva sintaxis del for 

def cargar():
    lista=[]
    for x in range(5):
        num=int(input("Ingrese un valor:"))
        lista.append(num)
        
    return lista

#obtener y mostrar el mayor
def imprimirmayor(lista):
    print("Lista completa")
    for elemento in lista:
        print(elemento)

#imprimir el mayor 
def mayor(lista):
    may=lista[0]
    for elemento in lista:
        if elemento>may:
            may=elemento
    print("El elemento mayor de la lista es:",may) 
 
    
def sumar_elementos(lista):
    suma=0
    for elemento in lista:
        suma=suma+elemento
    print("La suma de todos los elementos es", suma) 
    
#bloque principal

lista=cargar()
imprimirmayor(lista)
mayor(lista)
sumar_elementos(lista)          
        