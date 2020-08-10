
"""
Realizar un test para postular a empleo, se obtuvo la siguiente información
cantidad total de preguntas que se le realizaron
y cantidad de preguntas que contestó correctamente. 
Se pide confeccionar n programa que ingrese los dos datos por teclado e informe 
el nivel del mismo según el porcentaje de respuesta correctas. 

 Nivel máximo: procentaje>=90%
 Nivel medio:  porcentaje>=75% y < 90%
 Nivel Regular: porcentaje>=50% y 75%
 Fuera de Nivel: Porcentaje<50%
"""

totalpreguntas=int(input("Ingrese la cantidad total de preguntas del examen"))
totalcorrectas=int(input("Ingrese la cantidad total de preguntas contestadas correctamente"))
porcentaje=totalcorrectas * 100 / totalpreguntas

if porcentaje>=90:
    print("Nivel máximo")
else:
    if porcentaje>=75:
        print("Nivel Medio")
    else:
        if porcentaje>=50:
            print("Nivel regular")
        else:
            print("Fuera de nivel")


