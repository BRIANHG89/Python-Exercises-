
"""cargar dos listas de 15 valores cada una.
   Informar con un mensaje cual de las dos listas tiene un valor acumulado mayor
   (mensajes "Lista 1 mayor", "Lista 2 mayor", "Listas iguales")
   Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.
"""


cont=1
acum1=0
acum2=0
print("Prime lista")
while cont<=15:
  valor=int(input("Ingrese valor:"))
  acum1=acum1+valor
  cont=cont+1
  print("Segunda lista")
  cont=1
  while cont<=15:
      valor=int(input("Ingrese valor:"))
      acum2=acum2+valor
      cont=cont+1
 if acum1>acum2:
     print("Lista 1 mayor.")
 else: 
     if acum2>acum1:
         print("Lista2 mayor.")
     else:
         print("Listas iguales.")
         