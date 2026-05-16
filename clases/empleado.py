#Importamos la clase persona 
from clases.persona import Persona

#Creamos la clase empleado y heredamos la clase persona 
class Empleado(Persona):
    def __init__(self, nombre, identificacion, telefono, cargo, salario, turno):
        super().__init__(nombre, identificacion, telefono)
        self.__cargo = cargo
        self.__salario = salario
        self.__turno = turno 

#Creamos el método mostrar categoría 
    def mostrar_info(self):
        print(f"Nombre: {self.getnombre()}")
        print(f"Identificación: {self.getidentificacion()}")
        print(f"Teléfono: {self.gettelefono()}")
        print(f"Cargo: {self.getcargo()}")
        print(f"Salario: {self.getsalario()}")
        print(f"Turno: {self.getturno()}")

#====================================================================
# GETTERS Y SETTERS
#====================================================================
        
# Me trae el dato 
    def getcargo(self):
        return self.__cargo
    
    def getsalario(self):
        return self.__salario
    
    def getturno(self):
        return self.__turno
#Cambia el dato 
    def setcargo(self,cargo):
        self.__cargo = cargo
    
    def setsalario(self,salario):
        self.__salario = salario

    def setturno(self,turno):
        self.__turno = turno 


