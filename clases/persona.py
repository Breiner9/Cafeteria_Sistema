#Importamos nuestra clase abstracta para poder crear nuestra clase persona 
from abc import ABC, abstractmethod

#Creamos clase persona 
class Persona(ABC):
    def __init__(self,nombre, identificacion, telefono):
        self.__nombre = nombre 
        self.__identificacion = identificacion
        self.__telefono = telefono

    @abstractmethod
    def mostrar_info(self):
        pass

#====================================================================
# GETTERS Y SETTERS
#====================================================================
 
    #Me trae el dato 

    def getnombre(self):
        return self.__nombre 
    
    def getidentificacion(self):
        return self.__identificacion
    
    def gettelefono(self):
        return self.__telefono
    
    #Cambio el dato 

    def setnombre(self, nombre):
        self.__nombre = nombre
    
    def setidentificacion(self, identificacion):
        self.__identificacion = identificacion
    
    def settelefono(self, telefono):
        self.__telefono = telefono
    
    


