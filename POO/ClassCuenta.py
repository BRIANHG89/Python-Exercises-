
class Cuenta:
    
      def __init__(self,titular,monto):
          self.titular=titular
          self.monto=monto
          
      def imprimir(self):
          print("Titular:",self.titular)
          print("Monto:",self.monto)
          
class CajaAhorro(Cuenta):
    
      def __init__(self,titular,monto):
          super().__init__(titular,monto)
          
      def imprimir(self):
          print("Cuenta de caja de ahorro")
          super().imprimir()
          
class PlazoFijo(Cuenta):
    
      def __init__(self,titular,monto,plazo,interes):
          super().__init__(titular,monto)
          
      def imprimir(self):
          print("Cuenta de caja de ahorro")
          super().imprimir()
          
class PlazoFijo(Cuenta):
      
       def __init__(self,titular,monto,plazo,interes):
           super().__init__(titular,monto)
           self.plazo=plazo
           self.intereses=interes
           
        def imprimir(self):
            print("Cuenta de plazo fijo")
            super().imprimir()
            print("Plazo en días:",self.plazo) 
            print("Interes:",self.interes)
            self.ganancia_interes()
            
        def ganancia_interes(self):
            ganancia=self.monto*self.interes/100
            print("Importe del interes:",ganancia)

#bloque principal

cajaAhorro=CajaAhorro("Juan", 2000)
cajaAhorro.imprimir()

plazoFijo=PlazoFijo("Diego", 10000, 30, 0.75) 
plazoFijo.imprimir()


    
          