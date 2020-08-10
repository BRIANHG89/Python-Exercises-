#ingrsar 5 enteros, una segunda función debe recibir una lista
# y retornar el mayor y el menor valor de la lista. 
#desde el bloque principal del programa llamar a ambas funciones


def carga_lista():
    li=[]
    for x in range(5):
        valor=int(input("Ingrese valor:"))
        li.append(valor)
        return li
    
def retornar_mayormenor(li):
    ma=li[0]
    me=li[0]
    for x in range(1, len(li)):
        if li[x]>ma:
            ma=li[x]
        else:
            if li[x]<me:
                me=li[x]
        return [ma, me]

#bloque principal

lista=carga_lista()
rango=retornar_mayormenor(lista) 
print("Mayor elemento de la lista:", rango[0])
print("Menor elemento de la lista:", rango[1])           