
#cargar los sueldos de 10 personas en una lista
#imprimir todos los sueldos
#cuantos tienen un sueldo superior a $4000
#retornar el promedio de sueldos
#mostrar todos los sueldos que estan por debajo del promedio 

def cargar_sueldos():
    sueldos=[]
    for x in range(10):
        su=int(input("Ingrese sueldo:"))
        sueldos.append(su)
    return sueldos

#imprimir sueldos 
def imprimir_sueldos(sueldos):
    print("Listado de sueldos")
    for x in range(len(sueldos)):
        print(sueldos[x])
               
#imprimir sueldos mayor a 4000
def sueldos_mayor4000(sueldos):
    cant=0
    for x in range(len(sueldos)):
        if sueldos[x]>4000:
            cant=cant+1
            
    print("Cantidad de empleados con un sueldo superior a 4000:", cant) 

#promedio de sueldos 
def promedio(sueldos):
    suma=0
    for x in range(len(sueldos)):
        suma=suma+sueldos[x]
    promedio=suma//10
    return promedio  

#imprimir sueldos bajos 

def sueldos_bajos(sueldos):
    pro=promedio(sueldos)
    print("Sueldo promedio de la empresa:", pro)
    print("Sueldos inferiores al promedio:")
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print(sueldos[x])
        
#bloque principal

sueldos=cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayor4000(sueldos)
sueldos_bajos(sueldos) 