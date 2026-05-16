#Creamos la clase mesa para mejorar la organización en el café 
class Mesa():
    def __init__(self, numero, capacidad, estado):
        self.__numero = numero
        self.__capacidad = capacidad
        self.__estado = estado

#Creamos métodos propios de la clase mesa 
    def ocupar(self):
       self.__estado = True

    def liberar(self):
        self.__estado = False

    def mostrar_estado(self):
        if self.__estado == True:
            print(f"Mesa {self.__numero} Disponible")
        else:   
            print(f"Mesa {self.__numero} No Disponible")

#====================================================================
# GETTERS Y SETTERS
#====================================================================
#Me trae mi dato 
    def getnumero(self):
        return self.__numero

    def getcapacidad(self):
        return self.__capacidad
    
    def getestado(self):
        return self.__estado
#Me cambia el dato 
    def setnumero(self,numero):
        self.__numero = numero 
    
    def setcapacidad(self,capacidad):
        self.__capacidad = capacidad
    
    def setestado(self,estado):
        self.__estado = estado 
