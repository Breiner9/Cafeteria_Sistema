#Importamos la clase producto 
from clases.producto import Producto

#Creamos la clase postre que está heredando producto 
class Postre(Producto):
    def __init__(self, nombre, precio_base, categoria, es_vegano):
        super().__init__(nombre, precio_base, categoria)
        self.__es_vegano = es_vegano

#Calculamos el precio 
    def calcular_precio(self):
        if self.__es_vegano == True:
            return self.getprecio_base() + 1000
        else:
            return self.getprecio_base()