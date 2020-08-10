
#definir una clase con el metodo init cargar los atributos por teclado y luego otro 
#metodo imprimir sus datos y por último uno que imprima 
#mensaje que debe pagar impuestos (si el sueldo a 3000)
#

class Empleado:
    
    def __init__(self):
        self.nombre=input("Ingrese el nombre del empleado")
        self.sueldo=float(input("Ingrese el sueldo:"))
        
    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Sueldo:",self.sueldo)
        
    def paga_impuestos(self):
        if self.sueldo>3000:
            print("Debe pagar impuestos")
        else:
            print("No paga impuestos")
        
    #bloque principal 
    empleado1=Empleado()
    empleado1.imprimir()
    empleado1.paga_impuestos()
    
    
        