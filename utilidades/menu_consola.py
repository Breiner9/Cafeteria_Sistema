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

 #Categorías 
        self.__cat_caliente = Categoria("Bebidas Calientes", "Preparaciones artesanales para calentar tu día")
        self.__cat_fria = Categoria("Bebidas Frías", "Frescura y sabor en cada sorbo")
        self.__cat_postre = Categoria("Postres", "Dulces tentaciones para acompañar tu momento")

 #Bebidas Calientes
        self.__servicio_producto.agregar(Bebida_caliente("Cappuccino", 5000, self.__cat_caliente, "S"))
        self.__servicio_producto.agregar(Bebida_caliente("Latte", 5500, self.__cat_caliente, "S"))
        self.__servicio_producto.agregar(Bebida_caliente("Espresso", 3500, self.__cat_caliente, "S"))
        self.__servicio_producto.agregar(Bebida_caliente("Americano", 4000, self.__cat_caliente, "S"))
        self.__servicio_producto.agregar(Bebida_caliente("Mocaccino", 6000, self.__cat_caliente, "S"))

#Bebidas Frías
        self.__servicio_producto.agregar(Bebida_fria("Jugo de Naranja", 4000, self.__cat_fria, "S", False))
        self.__servicio_producto.agregar(Bebida_fria("Smoothie de Fresa", 5500, self.__cat_fria, "S", False))
        self.__servicio_producto.agregar(Bebida_fria("Frappé de Café", 6500, self.__cat_fria, "S", False))
        self.__servicio_producto.agregar(Bebida_fria("Limonada Natural", 3500, self.__cat_fria, "S", False))
        self.__servicio_producto.agregar(Bebida_fria("Té Helado", 3000, self.__cat_fria, "S", False))

#Postres
        self.__servicio_producto.agregar(Postre("Brownie", 3500, self.__cat_postre, False))
        self.__servicio_producto.agregar(Postre("Cheesecake", 5000, self.__cat_postre, False))
        self.__servicio_producto.agregar(Postre("Galleta de Avena", 2500, self.__cat_postre, True))
        self.__servicio_producto.agregar(Postre("Torta de Chocolate", 5500, self.__cat_postre, False))
        self.__servicio_producto.agregar(Postre("Bowl de Frutas", 4000, self.__cat_postre, True))

#Mesas
        self.__mesas.append(Mesa(1, 4, True))
        self.__mesas.append(Mesa(2, 2, False))
        self.__mesas.append(Mesa(3, 6, False))
        self.__mesas.append(Mesa(4, 4, True))
        self.__mesas.append(Mesa(5, 2, True))

#Creamos métodos propios de nuestra clase los cuáles nos ayudarán con la experiencia del usuario 
    def mostrar_menu(self):
        print("\n╔══════════════════════════════════╗")
        print("║        ☕ COFFEE SHOP            ║")
        print("╠══════════════════════════════════╣")
        print("║  1. Registrar cliente            ║")
        print("║  2. Registrar empleado           ║")
        print("║  3. Ver Menú                     ║")
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
                self.ver_menu()
            elif opcion == "4":
                self.gestionar_mesas()
            elif opcion == "5":
                self.crear_pedido()
            elif opcion == "6":
                self.registrar_pago()
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

    def ver_menu(self):
        productos = self.__servicio_producto.getproductos()

        print("\n╔══════════════════════════════════════╗")
        print("║           📋 MENÚ COFFEE SHOP        ║")
        print("╚══════════════════════════════════════╝")

        print("\n  ☕ BEBIDAS CALIENTES")
        print("  ─────────────────────────────────")
        for producto in productos:
                if producto.getcategoria().getnombre() == "Bebidas Calientes":
                    print(f"    {producto.getnombre()} ......... ${producto.calcular_precio()}")

        print("\n  🥤 BEBIDAS FRÍAS")
        print("  ─────────────────────────────────")
        for producto in productos:
            if producto.getcategoria().getnombre() == "Bebidas Frías":
                print(f"    {producto.getnombre()} ......... ${producto.calcular_precio()}")

        print("\n  🍰 POSTRES")
        print("  ─────────────────────────────────")
        for producto in productos:
            if producto.getcategoria().getnombre() == "Postres":
                print(f"    {producto.getnombre()} ......... ${producto.calcular_precio()}")

        print("\n  ─────────────────────────────────")
        print("  * Precios base (Tamaño S)")
        print("  * Tamaño M (+30%) | L (+50%)")

    def gestionar_mesas(self):
        print("\n=== Mesas ===")
        for mesa in self.__mesas:
            mesa.mostrar_estado()

    def crear_pedido(self):
        if len(self.__clientes) == 0:
            print("No hay clientes registrados")
            return
        if len(self.__empleados) == 0:
            print("No hay empleados registrados")
            return
        
        print("\n=== Clientes registrados ===")
        for i, cliente in enumerate(self.__clientes):
         print(f"{i + 1}. {cliente.getnombre()}")

        opcion = int(input("Elige cliente: ")) - 1
        cliente = self.__clientes[opcion]

        print("\n=== Empleados registrados ===")
        for i, empleado in enumerate(self.__empleados):
         print(f"{i + 1}. {empleado.getnombre()}")

        opcion = int(input("Elige empleado: ")) - 1
        empleado = self.__empleados[opcion]

        print("\n¿Mesa o para llevar?")
        print("1. Mesa")
        print("2. Para llevar")
        opcion_mesa = input("Elige: ")

        if opcion_mesa == "1":
            self.gestionar_mesas()
            num = int(input("Elige número de mesa: "))
            mesa = self.__mesas[num - 1]
            mesa.ocupar()
        else:
            mesa = None

        pedido = Pedido(cliente, empleado, mesa)

        while True:
            self.ver_menu()
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))

            producto = self.__servicio_producto.buscar(nombre)

            if producto is not None:
                detalle = Detalle_pedido(producto, cantidad)
                pedido.agregar_detalle(detalle)
                print("Producto agregado ✅")
            else:
                print("Producto no encontrado ❌")

            otro = input("¿Agregar otro producto? (sí/no): ")
            if otro == "no":
                break

        pedido.mostrar_resumen()
        self.__servicio_pedido.agregar_pedido(pedido)


    def registrar_pago(self):
        if len(self.__servicio_pedido.getpedidos()) == 0:
            print("No hay pedidos registrados")
            return
    
        pedidos = self.__servicio_pedido.getpedidos()
        for i, pedido in enumerate(pedidos):
            print(f"{i + 1}. Pedido de {pedido.getcliente().getnombre()}")
        opcion = int(input("Elige pedido: ")) - 1
        pedido = pedidos[opcion]
    
        print(f"Total a pagar: ${pedido.calcular_total()}")

        metodo = input("Método de pago (Efectivo/Tarjeta): ")
        monto = float(input("Monto: $"))

        print()
        
        pago = Pago(pedido, metodo, monto)
        pago.procesar_pago()
        pago.generar_recibo()
        self.__servicio_pago.agregar_pago(pago)