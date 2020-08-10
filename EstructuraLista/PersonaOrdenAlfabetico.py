
"""
Cargar 5 nombres y almacenarlos en una lista.
 Mostrar el nombre de persona menor en orden 
 alfabetico.
"""

nombres=[]
for x in range(5):
    nom=input("Ingrese nombre persona:")
    nombres.append(nom)
    
    nombremenor=nombres[0]
    for x in range(1,5):
        if nombres[x]<nombremenor:
            nombremenor=nombres[x]
            
    print("La lista completa de nombres ingresado son")
    print(nombres)
    print("El nombre menor en orden alfabetico es:")
    print(nombremenor)
    