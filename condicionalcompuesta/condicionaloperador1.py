
"""
Se carga una fecha (dia, mes y año) por teclado. Mostrando un mensaje
si corresponde al primer trimestre del año (enero, febrero o marzo) 
cargar por teclado el valor numérico del día, mes y año
"""

dia=int(input("Ingrese nro de días:"))
mes=int(input("Ingrese nro de mes:"))
año=int(input("Ingrese nro de año:"))

  if mes==1 or mes==2 or mes==3:
      print("Corresponde al primer trimestre")