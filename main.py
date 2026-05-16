#Importamos todas nuestras clases para poder correr nuestro programa 
from clases.cliente import Cliente
from clases.empleado import Empleado
from clases.categoria import Categoria

#Creamos los objetos de Cliente
def prueba_cliente():
    print("====== Datos Clientes ======")
    print()
    cliente1 = Cliente("Breiner Pinilla",1053125232,3007214025,"Calle 4A N 3-26, Bogotá, Colombia", 35)

    cliente1.mostrar_info()
    print()
    cliente1.acumular_puntos(5)
    print()
    cliente1.canjear_puntos(20)
    print()

#Creamos los objetos de Empleado 
def prueba_empleado():
    print("====== Datos Empleados ======")
    print()
    Empleado1 = Empleado("Fernando Rodriguez", 1053216785,3118241615,"Administrador","$3.000.000","Tarde")

    Empleado1.mostrar_info()
    print()

#Creamos los objetos de Categoria
def prueba_categoria():
    print(f"====== Categorías ======")
    print()
    cat1 = Categoria("☕ Bebidas Calientes","Especialidades para calentar tu día")
    cat2 = Categoria("🥤 Bebidas Frías","Frescura y sabor en cada sorbo")
    cat3 = Categoria("🍰 Postres","Dulces tentaciones que te acompañan")
    cat4 = Categoria("✨ Otros","Opciones para todos los gustos")
    
    cat1.mostrar_categoria()
    print()
    cat2.mostrar_categoria()
    print()
    cat3.mostrar_categoria()
    print()
    cat4.mostrar_categoria()
    print()




#Ejecuta el programa en orden que se quiere trabajar
def main():
    prueba_cliente()
    prueba_empleado()
    prueba_categoria()

#Inicia la ejecución del archivo 
main()
