
"""
Utiliza un diccionario cuya clave sea la fecha. Permitir
almacenar distintas actividades para la misma fecha(se ingresa la hora y la actividad)
implementar las siguientes funciones
1.carga de datos de la agenda. 
2.Listado completo de la agenda. 
3. consulta de una fecha
"""

def cargar():
    agenda={}
    continua1="s"
    while continua1=="s":
        fecha=input("Ingrese la fecha con formato dd/mm/aa:")
        continua2="s"
        lista=[]
        while continua2=="s":
            hora=input("Ingrese la hora de la actividad con formato hh:mm")
            actividad=input("Ingrese la descripcion de la actividad:")
            lista.append((hora,actividad))
            continua2=input("Ingresa otra actividad para la misma fehca[s/n]:")
            agenda[fecha]=lista
            continua1=input("Ingresa otra fecha[s/n]:")
    return agenda
            
def imprimir(agenda):
    print("Listado completa de la agenda")
    for fecha in agenda:
        print("Para la fecha:",fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
        
def consulta_fecha(agenda):
    fecha=input("Ingrese la fecha que desea consultar:")
    if fecha in agenda:
        for hora,actividad in agenda[fecha]:
           print(hora,actividad)
    else:
          print("No hay actividades agendadas para dicha fecha")
        
#bloque principal

agenda=cargar()
imprimir(agenda)
consulta_fecha(agenda)


