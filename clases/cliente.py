#Importamos nuestra clase persona 
from clases.persona import Persona

#Creamos la clase cliente que hereda la clase persona
class Cliente(Persona):
    def __init__(self, nombre, identificacion, telefono, direccion, coffee_points):
        super().__init__(nombre, identificacion, telefono)
        self.__direccion = direccion
        self.__coffee_points = coffee_points

#Creamos nuevamente el mismo método que en persona
    def mostrar_info(self):
            print(f"Nombre: {self.getnombre()}")
            print(f"Identificación: {self.getidentificacion()}")
            print(f"Teléfono: {self.gettelefono()}")
            print(f"Dirección: {self.getdireccion()}")
            print(f"Coffee Points: {self.getcoffee_points()}")

#Creamos métodos propios de la clase cliente 
    def acumular_puntos(self, coffee_points):
            self.__coffee_points = self.__coffee_points + coffee_points

    def canjear_puntos(self, coffee_points):
            if self.__coffee_points >= coffee_points:
                self.__coffee_points = self.__coffee_points - coffee_points
                print("¡¡Ganaste un Café!!")
            else:
                print("No tienes puntos suficientes para canjear")
#====================================================================
# GETTERS Y SETTERS
#====================================================================
        
# Me trae el dato 
    def getdireccion(self):
            return self.__direccion 
        
    def getcoffee_points(self):
            return self.__coffee_points
        
#Cambia el dato 
    def setdireccion(self, direccion):
            self.__direccion = direccion

    def setcoffee_points(self, coffee_points):
            self.__coffee_points = coffee_points