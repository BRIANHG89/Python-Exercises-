
#función que envie parametros el valor del lado de un cuadrado
# y nos retorne su superficie

def retornar_superfice(lado):
    sup=lado*lado
    return sup

# bloque principal del programa

  va=int(input("Ingrese el valor del lado del cuadrado:"))
  superficie=retornar_superfice(va)
  print("La superficie del cuadrado es", superficie)
  
  