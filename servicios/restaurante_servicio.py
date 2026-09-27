from pathlib import Path

from modelos.usuario import Usuario
from modelos.producto import Producto
from modelos.venta import Venta

from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:

    def __init__(self):

        base = Path(__file__).resolve().parent.parent

        self.ruta_datos = base / "datos"

        self.ruta_usuarios = (
            self.ruta_datos / "usuarios.json"
        )

        self.ruta_productos = (
            self.ruta_datos / "productos.json"
        )

        self.ruta_ventas = (
            self.ruta_datos / "ventas.json"
        )

        self.usuarios = self.cargar_usuarios()
        self.productos = self.cargar_productos()
        self.ventas = self.cargar_ventas()

        self.mostrar_estado()

    # ==========================================
    # INFORMACIÓN INICIAL
    # ==========================================

    def mostrar_estado(self):

        print("=" * 40)
        print("SULTAN RESTAURANT")
        print("TURKISH BBQ")
        print("=" * 40)

        print("RUTA DE PRODUCTOS:")
        print(self.ruta_productos)

        print(
            f"PRODUCTOS CARGADOS: "
            f"{len(self.productos)}"
        )

        for producto in self.productos:

            print(
                producto.codigo,
                producto.nombre,
                producto.precio,
                producto.categoria,
                producto.stock
            )

        print(
            f"USUARIOS CARGADOS: "
            f"{len(self.usuarios)}"
        )

        print(
            f"VENTAS CARGADAS: "
            f"{len(self.ventas)}"
        )

        print("=" * 40)

    # ==========================================
    # USUARIOS
    # ==========================================

    def cargar_usuarios(self):

        datos = ArchivoServicio.cargar(
            self.ruta_usuarios
        )

        return [
            Usuario.desde_diccionario(item)
            for item in datos
        ]

    def validar_login(
        self,
        usuario,
        contrasena
    ):

        for persona in self.usuarios:

            if (
                persona.usuario == usuario
                and
                persona.contrasena == contrasena
            ):
                return persona

        return None

    def listar_usuarios(self):

        return self.usuarios

    def buscar_usuario(
        self,
        identificacion
    ):

        for usuario in self.usuarios:

            if usuario.identificacion == identificacion:
                return usuario

        return None

    # ==========================================
    # PRODUCTOS
    # ==========================================

    def cargar_productos(self):

        datos = ArchivoServicio.cargar(
            self.ruta_productos
        )

        return [
            Producto.desde_diccionario(item)
            for item in datos
        ]

    def listar_productos(self):

        return self.productos

    def buscar_producto(
        self,
        codigo
    ):

        for producto in self.productos:

            if producto.codigo == codigo:
                return producto

        return None

    def guardar_productos(self):

        datos = [
            producto.convertir_a_diccionario()
            for producto in self.productos
        ]

        ArchivoServicio.guardar(
            self.ruta_productos,
            datos
        )

    # ==========================================
    # VENTAS
    # ==========================================

    def cargar_ventas(self):

        datos = ArchivoServicio.cargar(
            self.ruta_ventas
        )

        ventas = []

        for posicion, item in enumerate(
            datos,
            start=1
        ):

            venta = Venta.desde_diccionario(
                item,
                id_por_defecto=posicion
            )

            ventas.append(venta)

        return ventas

    def listar_ventas(self):

        return self.ventas

    def guardar_ventas(self):

        datos = [
            venta.convertir_a_diccionario()
            for venta in self.ventas
        ]

        ArchivoServicio.guardar(
            self.ruta_ventas,
            datos
        )

    def generar_id_venta(self):

        if not self.ventas:
            return 1

        return max(
            venta.id
            for venta in self.ventas
        ) + 1

    # ==========================================
    # REGISTRAR VENTA
    # ==========================================

    def registrar_venta(
        self,
        usuario_id,
        producto_codigo
    ):

        usuario = self.buscar_usuario(
            usuario_id
        )

        if usuario is None:

            raise ValueError(
                "El usuario seleccionado no existe."
            )

        producto = self.buscar_producto(
            producto_codigo
        )

        if producto is None:

            raise ValueError(
                "El producto seleccionado no existe."
            )

        if not producto.disponible:

            raise ValueError(
                "El producto está agotado."
            )

        # ======================================
        # DESCONTAR UNA UNIDAD
        # ======================================

        producto.vender()

        # ======================================
        # CREAR VENTA
        # ======================================

        nueva_venta = Venta(
            id=self.generar_id_venta(),
            usuario_id=usuario.identificacion,
            producto_codigo=producto.codigo
        )

        # ======================================
        # GUARDAR EN MEMORIA
        # ======================================

        self.ventas.append(
            nueva_venta
        )

        # ======================================
        # GUARDAR EN JSON
        # ======================================

        self.guardar_productos()
        self.guardar_ventas()

        # ======================================
        # DEVOLVER EL OBJETO VENTA
        # ======================================

        return nueva_venta