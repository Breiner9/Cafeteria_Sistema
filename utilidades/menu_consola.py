#Importamos todas nuestras clases para poder empezar a construir nuestra consola
from clases.cliente import Cliente
from clases.empleado import Empleado
from clases.categoria import Categoria  
from clases.bebida_caliente import Bebida_caliente
from clases.bebida_fria import Bebida_fria
from clases.postre import Postre
from clases.mesa import Mesa
from clases.detalle_pedido import Detalle_pedido
from clases.pedido import Pedido
from clases.pago import Pago
from servicios.servicio_pago import Servicio_pago
from servicios.servicio_pedido import Servicio_pedido
from servicios.servicio_producto import Servicio_producto

#Creamos nuestra clase 
class Menu_consola():
    def __init__(self):
        self.__servicio_producto = Servicio_producto()
        self.__servicio_pedido = Servicio_pedido()
        self.__servicio_pago = Servicio_pago()
        self.__clientes = []
        self.__empleados = []
        self.__mesas = []

#Creamos métodos propios de nuestra clase los cuáles nos ayudarán con la experiencia del usuario 
    def mostrar_menu(self):
        print("\n╔══════════════════════════════════╗")
        print("║        ☕ COFFEE SHOP            ║")
        print("╠══════════════════════════════════╣")
        print("║  1. Registrar cliente            ║")
        print("║  2. Registrar empleado           ║")
        print("║  3. Gestionar productos          ║")
        print("║  4. Gestionar mesas              ║")
        print("║  5. Crear pedido                 ║")
        print("║  6. Registrar pago               ║")
        print("║  7. Salir                        ║")
        print("╚══════════════════════════════════╝")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Elige una opción: ")

            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.registrar_empleado()
            elif opcion == "3":
                print("Cargando...")
            elif opcion == "4":
                print("Cargando...")
            elif opcion == "5":
                print("Cargando...")
            elif opcion == "6":
                print("Cargando...")
            elif opcion == "7":
                print("¡¡¡Gracias por visitarnos!!!")
                break 
    
    def registrar_cliente(self):
        nombre = input("Nombre: ")
        identificacion = input("Identificación: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")

        cliente = Cliente(nombre, identificacion, telefono, direccion, 0)
        self.__clientes.append(cliente)
        print("¡¡¡Cliente registrado exitosamente!!!")

    def registrar_empleado(self):
        nombre = input("Nombre Empleado: ")
        identificacion = input("ID:")
        telefono = input("Teléfono: ")
        cargo = input("Cargo: ")
        salario = input("Salario: ")
        turno = input("Turno: ")

        empleado = Empleado(nombre, identificacion, telefono, cargo, salario, turno)
        self.__empleados.append(empleado)
        print("¡¡¡Registro completado!!!")



        