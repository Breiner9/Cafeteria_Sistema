# ☕ Coffee Shop — Sistema de Cafetería

Sistema de gestión para una cafetería desarrollado en **Python**, aplicando los principios de **Programación Orientada a Objetos (POO)**.

Permite registrar clientes, empleados, gestionar mesas, visualizar el menú de productos, crear pedidos y registrar pagos desde una interfaz de consola interactiva.

---

## 📋 Tabla de contenidos

- [Características](#-características)
- [Estructura del proyecto](#-estructura-del-proyecto)
- [Conceptos POO aplicados](#-conceptos-poo-aplicados)
- [Requisitos](#️-requisitos)
- [Instalación y ejecución](#-instalación-y-ejecución)
- [Uso del sistema](#️-uso-del-sistema)
- [Clases del sistema](#-clases-del-sistema)
- [Autor](#-autor)

---

## ✨ Características

- Registro de clientes con sistema de puntos de fidelidad (Coffee Points)
- Registro de empleados con datos de cargo, salario y turno
- Menú de productos organizado por categorías (Bebidas Calientes, Bebidas Frías, Postres)
- Precios dinámicos según tamaño (S, M, L) y atributos especiales (crema, vegano)
- Gestión de mesas con estado de disponibilidad
- Creación de pedidos (en mesa o para llevar)
- Registro de pagos con validación de monto y generación de recibo
- Interfaz de consola interactiva con menú visual

---

## 📁 Estructura del proyecto

```
Proyecto Cafetería/
│
├── clases/
│   ├── persona.py             # Clase abstracta (padre de Cliente y Empleado)
│   ├── cliente.py             # Hereda de Persona — datos del comprador
│   ├── empleado.py            # Hereda de Persona — datos del trabajador
│   ├── categoria.py           # Categoría de productos
│   ├── producto.py            # Clase base Producto
│   ├── bebida_caliente.py     # Hereda de Producto — precio por tamaño
│   ├── bebida_fria.py         # Hereda de Producto — precio por tamaño y crema
│   ├── postre.py              # Hereda de Producto — recargo si es vegano
│   ├── mesa.py                # Mesa del local (disponible/no disponible)
│   ├── detalle_pedido.py      # Producto + cantidad (composición)
│   ├── pedido.py              # Pedido completo (composición)
│   └── pago.py                # Registro de pago (composición)
│
├── servicios/
│   ├── servicio_producto.py   # Gestiona la lista de productos
│   ├── servicio_pedido.py     # Gestiona la lista de pedidos
│   └── servicio_pago.py       # Gestiona la lista de pagos
│
├── utilidades/
│   └── menu_consola.py        # Menú interactivo del sistema
│
├── main.py                    # Punto de entrada del programa
└── README.md
```

---

## 🧠 Conceptos POO aplicados

| Concepto | Dónde se aplica |
|---|---|
| **Constructor** | Todas las clases |
| **Encapsulamiento** | Atributos privados (`__`) con getters y setters |
| **Herencia** | Cliente/Empleado ← Persona · BebidaCaliente/BebidaFria/Postre ← Producto |
| **Abstracción** | Persona es clase abstracta (ABC + abstractmethod) |
| **Polimorfismo** | `mostrar_info()` en Cliente vs Empleado · `calcular_precio()` en hijas de Producto |
| **Sobreescritura** | `mostrar_info()` y `calcular_precio()` redefinidos en clases hijas |
| **Composición** | DetallePedido contiene Producto · Pedido contiene Cliente, Empleado, Mesa · Pago contiene Pedido |
| **Sobrecarga** | Constructor de Pedido con `mesa=None` para pedidos para llevar |

---

## ⚙️ Requisitos

- Python 3.10 o superior

---

## 🚀 Instalación y ejecución

1. Clona el repositorio:
```bash
git clone https://github.com/TU_USUARIO/Proyecto-Cafeteria.git
```

2. Entra a la carpeta del proyecto:
```bash
cd Proyecto-Cafeteria
```

3. Ejecuta el programa:
```bash
python main.py
```

---

## 🖥️ Uso del sistema

Al ejecutar el programa se muestra el menú principal:

```
╔══════════════════════════════════╗
║        ☕ COFFEE SHOP            ║
╠══════════════════════════════════╣
║  1. Registrar cliente            ║
║  2. Registrar empleado           ║
║  3. Ver Menú                     ║
║  4. Gestionar mesas              ║
║  5. Crear pedido                 ║
║  6. Registrar pago               ║
║  7. Salir                        ║
╚══════════════════════════════════╝
```

### Flujo recomendado:
1. **Registrar** un cliente y un empleado
2. **Ver el menú** de productos disponibles
3. **Crear un pedido** → elegir cliente, empleado, mesa y productos
4. **Registrar el pago** → elegir método de pago e ingresar monto

---

## 📦 Clases del sistema

### Persona (abstracta)
Clase base para Cliente y Empleado. Define atributos comunes (nombre, identificación, teléfono) y el método abstracto `mostrar_info()`.

### Cliente
Hereda de Persona. Agrega dirección y coffee_points. Métodos propios: `acumular_puntos()` y `canjear_puntos()`.

### Empleado
Hereda de Persona. Agrega cargo, salario y turno. Sobreescribe `mostrar_info()` con datos laborales.

### Categoría
Define el tipo de producto (Bebidas Calientes, Bebidas Frías, Postres) con nombre y descripción.

### Producto
Clase base con nombre, precio base y categoría (composición). Método `calcular_precio()` retorna el precio base.

### BebidaCaliente
Hereda de Producto. Atributo propio: tamaño (S, M, L). Sobreescribe `calcular_precio()` ajustando el precio según el tamaño (S = base, M = +30%, L = +50%).

### BebidaFria
Hereda de Producto. Atributos propios: tamaño y tiene_crema. Sobreescribe `calcular_precio()` con recargo por crema (+$500).

### Postre
Hereda de Producto. Atributo propio: es_vegano. Sobreescribe `calcular_precio()` con recargo del 20% si es vegano.

### Mesa
Gestiona mesas del local con número, capacidad y estado (disponible/no disponible). Métodos: `ocupar()` y `liberar()`.

### DetallePedido
Composición: contiene un producto y una cantidad. Calcula el subtotal (precio × cantidad).

### Pedido
Composición: contiene cliente, empleado, mesa (o None para llevar) y lista de detalles. Métodos: `agregar_detalle()`, `calcular_total()`, `mostrar_resumen()`.

### Pago
Composición: contiene un pedido, método de pago, monto y fecha. Métodos: `procesar_pago()` (valida monto) y `generar_recibo()`.

---

## 👤 Autor

**Breiner Pinilla**

---