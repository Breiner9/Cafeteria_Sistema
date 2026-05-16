#Creamos nuestra clase producto
class Producto():
    def __init__(self,nombre,precio_base,categoria):
        self.__nombre = nombre
        self.__precio_base = precio_base
        self.__categoria = categoria

#Creamos métodos para la clase producto
    def calcular_precio(self):
        return self.__precio_base 

    def mostrar_producto(self):
        print(f"Nombre: {self.getnombre()}  Precio: ${self.calcular_precio()} Categoría: {self.getcategoria().getnombre()}")
#====================================================================
# GETTERS Y SETTERS
#====================================================================
#Me trae el dato que quiero
    def getnombre(self):
        return self.__nombre
    
    def getprecio_base(self):
        return self.__precio_base
    
    def getcategoria(self):
        return self.__categoria

#Cambia mi dato 
    def setnombre(self,nombre):
        self.__nombre = nombre
    
    def setprecio_base(self,precio_base):
        self.__precio_base = precio_base

    def setcategoria(self,categoria):
        self.__categoria = categoria