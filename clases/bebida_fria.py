#Importamos la clase producto 
from clases.producto import Producto

#Creamos nuestra clase Bebida_fría 
class Bebida_fria(Producto):
    def __init__(self, nombre, precio_base, categoria, tamanio, tiene_hielo):
        super().__init__(nombre, precio_base, categoria)
        self.__tamanio = tamanio
        self.__tiene_hielo = tiene_hielo

#Calculamos el precio 
    def calcular_precio(self):
        if self.__tamanio == "S":
            precio = self.getprecio_base()
        elif self.__tamanio == "M":
            precio = self.getprecio_base()*1.3
        elif self.__tamanio == "L":
            precio = self.getprecio_base()*1.5
        
        if self.__tiene_hielo == True:
            precio = precio + 500

        return precio 

        


