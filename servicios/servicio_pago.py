#Creamos la clase servicio_pago para gestionar los pagos
class Servicio_pago():
    def __init__(self):
        self.__pagos = []
    
#Creamos métodos propios de la clase 
    def agregar_pago(self, pago):
        self.__pagos.append(pago)
    def listar_pagos(self):
        for pago in self.__pagos:
            pago.generar_recibo()