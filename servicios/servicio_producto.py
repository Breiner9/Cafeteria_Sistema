#Creamos la clase servicio_producto que va a gestionar listas 
class Servicio_producto():
    def __init__(self):
        self.__productos = []

#Creamos el métodos propios para nuestra clase 
    def agregar(self, producto):
        self.__productos.append(producto)
    def eliminar(self, producto):
        self.__productos.remove(producto)
    def buscar(self, nombre):
        for producto in self.__productos:
            if producto.getnombre()== nombre:
                return producto
            
    def listar(self):
        for producto in self.__productos:
            producto.mostrar_producto()

#Creo un getter para poder acceder a mis productos en el menú
    def getproductos(self):
        return self.__productos

