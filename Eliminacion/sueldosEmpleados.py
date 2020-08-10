"""
Crear dos listas paralelas. En la primera cargar los nombres de los empleados
en la segunda los sueldos
Borrar luego todos los empleados que tienen un sueldo mayor a 1000
tanto el sueldo como su nombre
"""

empleados=[]
sueldos=[]
cant=int(input("Cuantos empleados tiene la empresa"))
for x in range(cant):
    nom=input("Ingrese el nombre:")
    empleados.append(nom)
    su=int(input("Ingrese el importe del sueldo"))
    sueldos.append(su)
    
    print("Listado completo de emplados")
    for x in range(len(sueldos)):
        print(empleados[x], sueldos[x])
        
    posicion=0
    while posicion<len(sueldos):
        if sueldos[posicion]>1000:
            sueldos.pop(posicion)
            empleados.pop(posicion)
        else:
            posicion=posicion+1
            
    print("Listado de empleados que cobran 10000 o menos")
    
    for x in range(len(sueldos)):
        print(empleados[x], sueldos[x])
        
        