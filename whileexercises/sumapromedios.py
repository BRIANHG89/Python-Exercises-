
#cargar 10 valores por teclado y nos muestre 
#posteriormente la suma de ellos valores ingresados 
#y su promedio 
contenedor=1
suma=0
while contenedor<=10:
    valor=int(input("Ingrese un valor:"))
    suma=suma+valor
    contenedor=contenedor+1
promedio=suma/10
print("La suma de los 10 valores es")
print(suma)
print("El promedio es")
print(promedio)