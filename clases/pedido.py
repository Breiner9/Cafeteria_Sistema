#Importamos datetime para que la fecha sea automática 
from datetime import datetime

#Creamos la clase pedido 
class Pedido():
    def __init__(self,cliente, empleado, mesa = None):
        self.__cliente = cliente
        self.__empleado = empleado
        self.__mesa = mesa
        self.__detalles = []
        self.__fecha = datetime.now()

#Creamos métodos propios de esta clase 
    def agregar_detalle(self, detalle):
        self.__detalles.append(detalle)

    def eliminar_detalle(self, detalle):
        self.__detalles.remove(detalle)

    def calcular_total(self):
        total = 0
        for detalle in self.__detalles:
                total = total + detalle.calcular_subtotal()
        return total

    def mostrar_resumen(self):
        print(f"Fecha: {self.__fecha}")
        print(f"Cliente: {self.__cliente.getnombre()}")
        print(f"Empleado: {self.__empleado.getnombre()}")

        if self.__mesa is None:
            print("Para llevar")
        else:
            print(f"Mesa: {self.__mesa.getnumero()}")

        for detalle in self.__detalles:
            print(f"Detalles: {detalle.getproducto().getnombre()} {detalle.getcantidad()} ${detalle.calcular_subtotal()}")

        print(f"Total: ${self.calcular_total()}")

#====================================================================
# GETTERS Y SETTERS
#====================================================================
#Trae mi dato 
    def getcliente(self):
        return self.__cliente
    def getempleado(self):
        return self.__empleado
    def getmesa(self):
        return self.__mesa
    def getdetalles(self):
        return self.__detalles
    def getfecha(self):
        return self.__fecha
#Cambia mi dato 
    def setcliente(self,cliente):
        self.__cliente = cliente
    def setempleado(self,empleado):
        self.__empleado = empleado
    def setmesa(self,mesa):
        self.__mesa = mesa 
    def setdetalles(self, detalles):
        self.__detalles = detalles 
    def setfecha(self, fecha):
        self.__fecha = fecha 