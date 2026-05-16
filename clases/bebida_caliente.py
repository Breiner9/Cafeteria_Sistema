#Importamos la clase producto
from clases.producto import Producto

#Creamos nuestra clase Bebida_caliente que hereda a producto 
class Bebida_caliente(Producto):
    def __init__(self, nombre,precio_base,categoria,tamanio):
        super().__init__(nombre,precio_base,categoria)
        self.__tamanio = tamanio

#Reescribimos el método calcular_precio
    def calcular_precio(self):
        if self.__tamanio == "S":
            return self.getprecio_base()
        elif self.__tamanio == "M":
            return self.getprecio_base() * 1.3
        elif self.__tamanio == "L":
            return self.getprecio_base() * 1.5

