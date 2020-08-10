"""
Comprueba si una cadena de texto es palindrome o no 
"""

cadena='''
Allí por la tropa portado, traído a ese paraje
de maniobras, una tipa como capitán usar boina
me dejara, pese a odiar toda tropa por tal ropilla
.'''

#pasamos todas las letras a minúscula

minusculas = cadena.lower()
palabras = minusculas.split()

#quitamos las comas y puntos

lista_plana = []
 
for p in palabras:
      q = p.strip(".").strip(",")
      lista_plana.append(q)
  
  print(lista_plana)
  
  cadena_plana = "".join(lista_plana)
  print(cadena_plana)
  