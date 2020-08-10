
class Agenda:
    
    def __init__(self):
        self.contactos={} #diccionario para almacenar los datos
        
    def menu(self):
        opcion=0
        while opcion!=5:
            print("1- Carga de un contacto en la agenda")
            print("2- Listado completo de agenda")
            print("3- Consulta ingresando el nombre de la persona")
            print("4- Finalizar programa")
            opcion=int(input("Ingrese su opción"))
            if opcion=1:
                self.cargar()
            elif opcion=2:
                self.listado()
            elif opcion=3:
                self.consulta()
            elif opcion==4:
                self.modificacion()
                   
    def cargar(self):
        nombre=input("Ingrese el nombre de la persona")
        telefono=input("Ingrese el numero de telefono:")
        mail=input("Ingrese el mail:")
        self.contactos[nombre]=(telefono,mail)
        print("_________________________________")
        
    def listado(self):
        print("______________________________")
        print("Listado completo de la agenda")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombres][0],self.contactos[nombre[1]])
            print("______________________________________")
    def consulta(self):
        print("___________________________________")
        nombre=input("Ingrese el nombre de la persona a consultar:")
        if nombre in self.contactos:
            print(nombre, "Su telefono es",self.contactos[nombre][0],"y su mail es",self.contactos[nombre][1])
        else:
            print("No existe un contacto con ese nombre")
        print("_________________________________")

    def modificacion(self):
        print("____________________________________")
        nombre=input("Ingrese el nombre de la persona a modificar el telefono y mail:")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo telefono:")
            mail=input("Ingrese el nuevo mail:")
            self.contactos[nombre]=(telefono,mail)
        else:
            print("No existe un contacto con ese nombre") 
            print("_____________________________________________")
            
    #bloque principal
    agenda=Agenda()
    agenda.menu()
                                       
                                   