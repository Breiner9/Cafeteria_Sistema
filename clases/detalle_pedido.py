#Creamos nuestra clase detalle_pedido 
class Detalle_pedido():
    def __init__(self, producto, cantidad):
        self.__producto = producto
        self.__cantidad = cantidad

#Creamos métodos propios de nuestra clase 
    def calcular_subtotal(self):
        subtotal = self.__producto.calcular_precio()*self.__cantidad
        return subtotal
        
#====================================================================
# GETTERS Y SETTERS
#====================================================================
#Me trae mi dato 
    def getproducto(self):
        return self.__producto
    
    def getcantidad(self):
        return self.__cantidad

#Me cambia el dato 
    def setproducto(self, producto):
        self.__producto = producto
    
    def setcantidad(self, cantidad):
        self.__cantidad = cantidad 