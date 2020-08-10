#recibir un string y nos retorne el que tiene mas caracteres 
# si hay mas de uno con dicha cantidad debe retornar el que tiene
#un valor de componente mas baja

 def cantidadcaracteres(word):
     pos=0
     for x in range(len(word)):
         if len(palabras[x])>len(palabras[pos]):
             pos=x
             return word[pos]
        
#bloque principal

word=["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"]
print("Palabra con mas caracteres:", cantidadcaracteres(word))



