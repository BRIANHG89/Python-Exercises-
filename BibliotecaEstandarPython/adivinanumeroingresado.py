
import random

intento=0
aleatorio=random.randint(1,100)
elegido=1
print("Intenta adivinar el numero que pense entre 1 y 100")
while (elegido!=aleatorio):
    elegido=int(input("Cual numero elige?"))
    if aleatorio>elegido:
        print("Pense un valor mayor")
    else:
        if aleatorio<elegido:
            print("Pense un valor menor")
        intento=intento+1
    print("Ganaste en",intento,"intentos")
    