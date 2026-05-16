#Creamos la clase categoría 
class Categoria():
    def __init__(self, nombre, descripcion):
        self.__nombre = nombre
        self.__descripcion = descripcion

#Creamos un método propio de la clase 

    def mostrar_categoria(self):
        print(f"  ╔════════════════════════════════════════════════╗ ")
        print(f"                   {self.getnombre()}")
        print(f'         "{self.getdescripcion()}"                   ')
        print(f"  ╚════════════════════════════════════════════════╝ ")

#====================================================================
# GETTERS Y SETTERS
#====================================================================
#Me trae mi dato 
    def getnombre(self):
        return self.__nombre
    
    def getdescripcion(self):
        return self.__descripcion
    
#Cambia mi dato 
    def setnombre(self,nombre):
        self.__nombre = nombre
    
    def setdescripcion(self,descripcion):
        self.__descripcion = descripcion 
    

    