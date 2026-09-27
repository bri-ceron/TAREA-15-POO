# SULTAN RESTAURANT - TURKISH BBQ

## Proyecto TAREA-15-POO

Aplicación de escritorio desarrollada en Python para la gestión básica de un restaurante, aplicando conceptos de Programación Orientada a Objetos (POO), manejo de eventos con Tkinter y almacenamiento de información mediante archivos JSON.

---

## 👩‍💻 Autora

**Briggitte Cerón**

---

## 🎯 Objetivo del proyecto

Desarrollar una aplicación de escritorio para gestionar usuarios, productos y ventas de un restaurante, utilizando Programación Orientada a Objetos y eventos de interfaz gráfica.

El proyecto permite iniciar sesión, consultar información registrada y realizar ventas mediante una interfaz gráfica desarrollada con Tkinter.

---

## 🍽️ Nombre del sistema

**SULTAN RESTAURANT**  
**TURKISH BBQ**

---

## 🛠️ Tecnologías utilizadas

- Python
- Tkinter
- Programación Orientada a Objetos (POO)
- Archivos JSON
- Visual Studio Code
- Git y GitHub

---

## 📂 Estructura del proyecto

```text
TAREA-15-POO/
│
├── assets/
│   ├── icono.png
│   └── logo.png
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── usuario.py
│   ├── producto.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── main.py
└── README.md
👤 Módulo de usuarios

El sistema permite cargar y consultar los usuarios almacenados en el archivo:

datos/usuarios.json

Cada usuario contiene:

Identificación
Nombre
Nombre de usuario
Contraseña

También se utiliza la información de los usuarios para validar el inicio de sesión y relacionarlos con las ventas realizadas.

🍔 Módulo de productos

Los productos se almacenan en:

datos/productos.json

Cada producto contiene:

Código
Nombre
Precio
Categoría
Stock

El sistema permite consultar los productos disponibles y controlar el stock al registrar una venta.

💰 Módulo de ventas

Las ventas se almacenan en:

datos/ventas.json

Cada venta contiene:

ID de venta
Identificación del usuario
Código del producto
Fecha y hora

Al registrar una venta, el sistema verifica que el usuario exista y que el producto tenga stock disponible.

Posteriormente:

Se registra la venta.
Se descuenta una unidad del stock.
Se guarda nuevamente el archivo productos.json.
Se guarda la información en ventas.json.
Se actualiza la tabla de ventas en la interfaz.
🧩 Programación Orientada a Objetos

El proyecto está organizado mediante diferentes clases.

Clase Usuario

Representa a los usuarios del sistema.

Clase Producto

Representa los productos disponibles en el restaurante y controla su stock.

Clase Venta

Representa una venta realizada y relaciona:

Usuario
Producto
Fecha
ID de venta
Clase ArchivoServicio

Se encarga de leer y guardar información en archivos JSON.

Clase RestauranteServicio

Contiene la lógica principal del sistema, como:

Validación del inicio de sesión.
Búsqueda de usuarios.
Búsqueda de productos.
Carga de información.
Registro de ventas.
Control de stock.
Guardado de ventas.
🖥️ Interfaz gráfica

La interfaz fue desarrollada utilizando Tkinter.

El sistema cuenta con:

Inicio de sesión

Permite ingresar utilizando un usuario y contraseña registrados.

Menú principal

El menú lateral contiene:

Usuarios
Productos
Ventas
Cerrar sesión
Usuarios

Muestra la información de los usuarios registrados.

Productos

Muestra:

Código
Nombre
Precio
Categoría
Stock
Estado
Ventas

Permite seleccionar un usuario y un producto para registrar una venta.

Después de registrar la venta, la información aparece automáticamente en la tabla.

⚡ Manejo de eventos

El proyecto aplica el manejo de eventos de Tkinter mediante command=.

El flujo principal para registrar una venta es:

Usuario realiza una acción
        ↓
Botón "Registrar venta"
        ↓
command=
        ↓
Callback registrar_venta()
        ↓
RestauranteServicio
        ↓
Validación
        ↓
Guardar venta
        ↓
Actualizar stock
        ↓
Actualizar interfaz

Esto permite separar la interfaz gráfica de la lógica del sistema.

💾 Persistencia de datos

La información se almacena utilizando archivos JSON.

Archivos utilizados:

usuarios.json
productos.json
ventas.json

De esta manera, los datos permanecen guardados aunque el programa se cierre.

▶️ Ejecución del proyecto

Para ejecutar el programa se debe abrir una terminal dentro de la carpeta del proyecto y utilizar:

python main.py

También puede ejecutarse desde Visual Studio Code utilizando el archivo:

main.py
🔐 Datos de acceso de prueba

Para realizar las pruebas del sistema se puede utilizar:

Usuario: briggitte
Contraseña: 1234

También existen otros usuarios registrados en el archivo:

datos/usuarios.json
🧪 Pruebas realizadas

Se verificó el funcionamiento de:

Inicio de sesión.
Carga de usuarios.
Carga de productos.
Carga de ventas.
Consulta de información.
Selección de usuario.
Selección de producto.
Registro de una venta.
Descuento del stock.
Guardado de la venta en ventas.json.
Actualización de la tabla de ventas.
Cierre de sesión.
Persistencia de la información.
📌 Características principales
Interfaz gráfica con Tkinter.
Diseño organizado por módulos.
Programación Orientada a Objetos.
Manejo de eventos.
Persistencia mediante JSON.
Control de stock.
Registro de ventas.
Validación de usuarios y productos.
Separación entre modelos, servicios e interfaz gráfica.

📚 Conclusión

El desarrollo de SULTAN RESTAURANT - TURKISH BBQ permitió aplicar los conocimientos adquiridos sobre Programación Orientada a Objetos, manejo de eventos e interfaces gráficas en Python.

La aplicación permite gestionar información básica de un restaurante y registrar ventas mediante una interfaz gráfica, manteniendo los datos almacenados en archivos JSON.

Además, la estructura del proyecto facilita la separación de responsabilidades entre los modelos, servicios y componentes de la interfaz.

👩‍💻 Autora

Briggitte Cerón