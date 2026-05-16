#Creamos la clase pedido para gestionar nuestros pedidos 
class Servicio_pedido():
    def __init__(self):
        self.__pedidos = []

#Creamos métodos propios de la clase 
    def agregar_pedido(self, pedido):
        self.__pedidos.append(pedido)
    def eliminar_pedido(self, pedido):
        self.__pedidos.remove(pedido)
    def listar_pedidos(self):
        for pedido in self.__pedidos:
            pedido.mostrar_resumen()