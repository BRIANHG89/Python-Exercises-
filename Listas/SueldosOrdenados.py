
#sueldos de empleados ordenados 

cantidad=int(input("Cuantos empleados tiene la empresa?"))
sueldos=[]
for x in range(cantidad):
    su=int(input("Ingrse sueldo:"))
    sueldos.append(su)
    
#ordenamos lista
for k in range(cantidad-1):
    for k in range(cantidad-1-k):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux
             
print("Lista de sueldos ordenados")
print(sueldos)
