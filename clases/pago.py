from datetime import datetime 

#Creamos la clase pago para procesar nuestros pagos 
class Pago():
    def __init__(self ,pedido, metodo_pago, monto):
        self.__pedido = pedido 
        self.__metodo_pago = metodo_pago
        self.__monto = monto 
        self.__fecha = datetime.now() 

#Creamos métodos propios de la clase pago
    def procesar_pago(self):
        if self.__monto >= self.__pedido.calcular_total():
            cambio = self.__monto - self.__pedido.calcular_total() 
            print("¡¡¡Pago Exitoso!!!")
            print(f"{cambio}")
        else: 
            print("No se pudo procesar, intente nuevamente")
    
    def generar_recibo(self):
        print(f"Fecha: {self.__fecha}")
        print(f"Monto: {self.__monto}")
        print(f"Método de Pago: {self.__metodo_pago}")
        print(f"Total: {self.__pedido.calcular_total()}")

#====================================================================
# GETTERS Y SETTERS
#====================================================================
#Me trae mi dato 
    def getpedido(self):
        return self.__pedido
    def getmetodo_pago(self):
        return self.__metodo_pago
    def getmonto(self):
        return self.__monto 
    def getfecha(self):
        return self.__fecha
#Cambia mi dato 
    def setpedido(self, pedido):
        self.__pedido = pedido 
    def setmetodo_pago(self, metodo_pago):
        self.__metodo_pago = metodo_pago
    def setmonto(self, monto):
        self.__monto = monto 
    def setfecha(self,fecha):
        self.__fecha = fecha 
