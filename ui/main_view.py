import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


class MainView:

    def __init__(self, root, servicio, usuario, cerrar_sesion):

        self.root = root
        self.servicio = servicio
        self.usuario = usuario
        self.cerrar_sesion = cerrar_sesion

        self.root.title("SULTAN RESTAURANT - TURKISH BBQ")
        self.root.geometry("1200x720")
        self.root.resizable(True, True)

        # ==========================================
        # RUTAS
        # ==========================================

        base = Path(__file__).resolve().parent.parent

        ruta_logo = base / "assets" / "logo.png"
        ruta_icono = base / "assets" / "icono.png"

        # ==========================================
        # LOGO
        # ==========================================

        try:

            self.logo = tk.PhotoImage(
                file=ruta_logo
            )

            # Reducir el logo para que no quede gigante
            while (
                self.logo.width() > 180
                or self.logo.height() > 100
            ):

                self.logo = self.logo.subsample(
                    2,
                    2
                )

        except Exception:

            self.logo = None

        # ==========================================
        # ICONO
        # ==========================================

        try:

            self.icono = tk.PhotoImage(
                file=ruta_icono
            )

            self.root.iconphoto(
                True,
                self.icono
            )

        except Exception:

            self.icono = None

        # ==========================================
        # ESTILOS
        # ==========================================

        self.configurar_estilos()

        # ==========================================
        # INTERFAZ
        # ==========================================

        self.crear_interfaz()

    # =================================================
    # ESTILOS
    # =================================================

    def configurar_estilos(self):

        estilo = ttk.Style()

        try:
            estilo.theme_use("clam")
        except Exception:
            pass

        estilo.configure(
            "Treeview",
            font=("Arial", 10),
            rowheight=30,
            background="white",
            fieldbackground="white"
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold"),
            background="#E5E7EB",
            foreground="#333333"
        )

        estilo.map(
            "Treeview",
            background=[
                ("selected", "#65C020")
            ],
            foreground=[
                ("selected", "white")
            ]
        )

    # =================================================
    # INTERFAZ PRINCIPAL
    # =================================================

    def crear_interfaz(self):

        contenedor = tk.Frame(
            self.root,
            bg="#F4F4F4"
        )

        contenedor.pack(
            expand=True,
            fill="both"
        )

        # ==========================================
        # PANEL IZQUIERDO
        # ==========================================

        self.menu = tk.Frame(
            contenedor,
            bg="#CFDDDA",
            width=290
        )

        self.menu.pack(
            side="left",
            fill="y"
        )

        self.menu.pack_propagate(False)

        # ==========================================
        # LOGO
        # ==========================================

        zona_logo = tk.Frame(
            self.menu,
            bg="#F5EEDC",
            height=125
        )

        zona_logo.pack(
            fill="x",
            pady=(15, 0)
        )

        zona_logo.pack_propagate(False)

        if self.logo:

            etiqueta_logo = tk.Label(
                zona_logo,
                image=self.logo,
                bg="#F5EEDC"
            )

            etiqueta_logo.pack(
                expand=True
            )

        # ==========================================
        # NOMBRE DEL RESTAURANTE
        # ==========================================

        nombre = tk.Label(
            self.menu,
            text="SULTAN RESTAURANT",
            font=("Arial", 16, "bold"),
            fg="#3B2F2F",
            bg="#D7D6E0"
        )

        nombre.pack(
            pady=(5, 0)
        )

        subtitulo = tk.Label(
            self.menu,
            text="TURKISH BBQ",
            font=("Arial", 12, "bold"),
            fg="#AA0BB8",
            bg="#F5EEDC"
        )

        subtitulo.pack(
            pady=(0, 20)
        )

        # ==========================================
        # LINEA DECORATIVA
        # ==========================================

        tk.Frame(
            self.menu,
            bg="#C49A3A",
            height=2
        ).pack(
            fill="x",
            padx=20,
            pady=(0, 20)
        )

        # ==========================================
        # BOTONES
        # ==========================================

        self.crear_boton_menu(
            "USUARIOS",
            self.mostrar_usuarios
        )

        self.crear_boton_menu(
            "PRODUCTOS",
            self.mostrar_productos
        )

        self.crear_boton_menu(
            "VENTAS",
            self.mostrar_ventas
        )

        # ==========================================
        # ESPACIO
        # ==========================================

        tk.Frame(
            self.menu,
            bg="#F5EEDC"
        ).pack(
            expand=True
        )

        # ==========================================
        # CERRAR SESIÓN
        # ==========================================

        boton_cerrar = tk.Button(
            self.menu,
            text="CERRAR SESIÓN",
            font=("Arial", 11, "bold"),
            bg="#52B474",
            fg="white",
            activebackground="#A91414",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.cerrar_sesion
        )

        boton_cerrar.pack(
            fill="x",
            padx=20,
            pady=20,
            ipady=10
        )

        # ==========================================
        # PANEL DERECHO
        # ==========================================

        self.panel = tk.Frame(
            contenedor,
            bg="#F4F4F4"
        )

        self.panel.pack(
            side="right",
            expand=True,
            fill="both"
        )

        self.mostrar_inicio()

    # =================================================
    # BOTONES DEL MENU
    # =================================================

    def crear_boton_menu(
        self,
        texto,
        comando
    ):

        boton = tk.Button(
            self.menu,
            text=texto,
            font=("Arial", 11, "bold"),
            bg="#E8D8B5",
            fg="#3B2F2F",
            activebackground="#C49A3A",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=comando
        )

        boton.pack(
            fill="x",
            padx=20,
            pady=5,
            ipady=10
        )

    # =================================================
    # LIMPIAR PANEL DERECHO
    # =================================================

    def limpiar_panel(self):

        for widget in self.panel.winfo_children():

            try:
                widget.destroy()
            except tk.TclError:
                pass

    # =================================================
    # INICIO
    # =================================================

    def mostrar_inicio(self):

        self.limpiar_panel()

        titulo = tk.Label(
            self.panel,
            text="Panel principal",
            font=("Arial", 26, "bold"),
            bg="#F4F4F4",
            fg="#3B2F2F"
        )

        titulo.pack(
            anchor="w",
            padx=35,
            pady=(40, 5)
        )

        subtitulo = tk.Label(
            self.panel,
            text=(
                "Consulte usuarios, gestione productos "
                "y registre ventas desde el menú lateral."
            ),
            font=("Arial", 11),
            bg="#F4F4F4",
            fg="#666666"
        )

        subtitulo.pack(
            anchor="w",
            padx=35
        )

        # ==========================================
        # TARJETAS
        # ==========================================

        tarjetas = tk.Frame(
            self.panel,
            bg="#F4F4F4"
        )

        tarjetas.pack(
            fill="x",
            padx=30,
            pady=30
        )

        self.crear_tarjeta(
            tarjetas,
            "Usuarios registrados",
            len(self.servicio.usuarios),
            "#2563EB"
        )

        self.crear_tarjeta(
            tarjetas,
            "Productos registrados",
            len(self.servicio.productos),
            "#16A34A"
        )

        self.crear_tarjeta(
            tarjetas,
            "Ventas registradas",
            len(self.servicio.ventas),
            "#D97706"
        )

    # =================================================
    # TARJETAS
    # =================================================

    def crear_tarjeta(
        self,
        padre,
        titulo,
        valor,
        color
    ):

        tarjeta = tk.Frame(
            padre,
            bg="white",
            bd=1,
            relief="solid"
        )

        tarjeta.pack(
            side="left",
            expand=True,
            fill="both",
            padx=7,
            ipady=15
        )

        tk.Label(
            tarjeta,
            text=titulo,
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#555555"
        ).pack(
            pady=(15, 0)
        )

        tk.Label(
            tarjeta,
            text=str(valor),
            font=("Arial", 25, "bold"),
            bg="white",
            fg=color
        ).pack(
            pady=5
        )

    # =================================================
    # ENCABEZADO
    # =================================================

    def crear_encabezado(
        self,
        titulo,
        descripcion
    ):

        encabezado = tk.Frame(
            self.panel,
            bg="#F4F4F4"
        )

        encabezado.pack(
            fill="x",
            padx=35,
            pady=(25, 5)
        )

        tk.Label(
            encabezado,
            text=titulo,
            font=("Arial", 25, "bold"),
            bg="#F4F4F4",
            fg="#3B2F2F"
        ).pack(
            anchor="w"
        )

        tk.Label(
            encabezado,
            text=descripcion,
            font=("Arial", 10),
            bg="#F4F4F4",
            fg="#666666"
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

    # =================================================
    # USUARIOS
    # =================================================

    def mostrar_usuarios(self):

        self.limpiar_panel()

        self.crear_encabezado(
            "USUARIOS",
            "Gestión y consulta de usuarios registrados."
        )

        botones = tk.Frame(
            self.panel,
            bg="#F4F4F4"
        )

        botones.pack(
            pady=10
        )

        self.crear_boton_accion(
            botones,
            "REGISTRAR",
            "#16A34A",
            self.registrar_usuario
        )

        self.crear_boton_accion(
            botones,
            "CONSULTAR",
            "#2563EB",
            self.consultar_usuarios
        )

        self.crear_boton_accion(
            botones,
            "ACTUALIZAR",
            "#D97706",
            self.actualizar_usuario
        )

        self.crear_boton_accion(
            botones,
            "ELIMINAR",
            "#DC2626",
            self.eliminar_usuario
        )

        self.crear_boton_accion(
            botones,
            "LIMPIAR",
            "#6B7280",
            self.limpiar_tabla
        )

        # ==========================================
        # TABLA
        # ==========================================

        tabla_frame = tk.Frame(
            self.panel,
            bg="#F4F4F4"
        )

        tabla_frame.pack(
            expand=True,
            fill="both",
            padx=30,
            pady=15
        )

        columnas = (
            "identificacion",
            "nombre",
            "usuario"
        )

        self.tabla_usuarios = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        self.tabla_usuarios.heading(
            "identificacion",
            text="ID / CÉDULA"
        )

        self.tabla_usuarios.heading(
            "nombre",
            text="NOMBRE"
        )

        self.tabla_usuarios.heading(
            "usuario",
            text="USUARIO"
        )

        self.tabla_usuarios.column(
            "identificacion",
            width=170
        )

        self.tabla_usuarios.column(
            "nombre",
            width=280
        )

        self.tabla_usuarios.column(
            "usuario",
            width=180
        )

        self.tabla_usuarios.pack(
            expand=True,
            fill="both"
        )

        self.cargar_usuarios()

    # =================================================
    # CARGAR USUARIOS
    # =================================================

    def cargar_usuarios(self):

        if not hasattr(
            self,
            "tabla_usuarios"
        ):
            return

        try:

            self.tabla_usuarios.delete(
                *self.tabla_usuarios.get_children()
            )

        except tk.TclError:

            return

        for usuario in self.servicio.usuarios:

            self.tabla_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    # =================================================
    # PRODUCTOS
    # =================================================

    def mostrar_productos(self):

        self.limpiar_panel()

        self.crear_encabezado(
            "PRODUCTOS",
            "Gestión y consulta de productos del restaurante."
        )

        botones = tk.Frame(
            self.panel,
            bg="#F4F4F4"
        )

        botones.pack(
            pady=10
        )

        self.crear_boton_accion(
            botones,
            "REGISTRAR",
            "#16A34A",
            self.registrar_producto
        )

        self.crear_boton_accion(
            botones,
            "CONSULTAR",
            "#2563EB",
            self.consultar_productos
        )

        self.crear_boton_accion(
            botones,
            "ACTUALIZAR",
            "#D97706",
            self.actualizar_producto
        )

        self.crear_boton_accion(
            botones,
            "ELIMINAR",
            "#DC2626",
            self.eliminar_producto
        )

        self.crear_boton_accion(
            botones,
            "LIMPIAR",
            "#6B7280",
            self.limpiar_tabla
        )

        tabla_frame = tk.Frame(
            self.panel,
            bg="#F4F4F4"
        )

        tabla_frame.pack(
            expand=True,
            fill="both",
            padx=25,
            pady=15
        )

        columnas = (
            "codigo",
            "nombre",
            "precio",
            "categoria",
            "stock",
            "estado"
        )

        self.tabla_productos = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "codigo": "CÓDIGO",
            "nombre": "PRODUCTO",
            "precio": "PRECIO",
            "categoria": "CATEGORÍA",
            "stock": "STOCK",
            "estado": "ESTADO"
        }

        for columna in columnas:

            self.tabla_productos.heading(
                columna,
                text=encabezados[columna]
            )

        self.tabla_productos.column(
            "codigo",
            width=90
        )

        self.tabla_productos.column(
            "nombre",
            width=220
        )

        self.tabla_productos.column(
            "precio",
            width=100
        )

        self.tabla_productos.column(
            "categoria",
            width=160
        )

        self.tabla_productos.column(
            "stock",
            width=80
        )

        self.tabla_productos.column(
            "estado",
            width=130
        )

        self.tabla_productos.pack(
            expand=True,
            fill="both"
        )

        self.cargar_productos()

    # =================================================
    # CARGAR PRODUCTOS
    # =================================================

    def cargar_productos(self):

        if not hasattr(
            self,
            "tabla_productos"
        ):
            return

        try:

            self.tabla_productos.delete(
                *self.tabla_productos.get_children()
            )

        except tk.TclError:

            return

        for producto in self.servicio.productos:

            self.tabla_productos.insert(
                "",
                "end",
                values=(
                    producto.codigo,
                    producto.nombre,
                    f"${producto.precio:.2f}",
                    producto.categoria,
                    producto.stock,
                    producto.estado
                )
            )

    # =================================================
    # VENTAS
    # =================================================

    def mostrar_ventas(self):

        self.limpiar_panel()

        self.crear_encabezado(
            "VENTAS",
            "Registre y consulte las ventas realizadas."
        )

        # ==========================================
        # FORMULARIO
        # ==========================================

        formulario = tk.Frame(
            self.panel,
            bg="white",
            bd=1,
            relief="solid"
        )

        formulario.pack(
            fill="x",
            padx=35,
            pady=10
        )

        tk.Label(
            formulario,
            text="USUARIO / CÉDULA:",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#3B2F2F"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=15
        )

        self.combo_usuario = ttk.Combobox(
            formulario,
            state="readonly",
            width=28
        )

        self.combo_usuario.grid(
            row=0,
            column=1,
            padx=10
        )

        tk.Label(
            formulario,
            text="PRODUCTO:",
            font=("Arial", 10, "bold"),
            bg="white",
            fg="#3B2F2F"
        ).grid(
            row=0,
            column=2,
            padx=10
        )

        self.combo_producto = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )

        self.combo_producto.grid(
            row=0,
            column=3,
            padx=10
        )

        boton = tk.Button(
            formulario,
            text="REGISTRAR VENTA",
            font=("Arial", 10, "bold"),
            bg="#16A34A",
            fg="white",
            activebackground="#15803D",
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=self.registrar_venta
        )

        boton.grid(
            row=0,
            column=4,
            padx=15,
            pady=10,
            ipady=6
        )

        self.cargar_combos()

        # ==========================================
        # TABLA DE VENTAS
        # ==========================================

        tabla_frame = tk.Frame(
            self.panel,
            bg="#F4F4F4"
        )

        tabla_frame.pack(
            expand=True,
            fill="both",
            padx=35,
            pady=15
        )

        columnas = (
            "id",
            "cedula",
            "usuario",
            "producto",
            "fecha"
        )

        self.tabla_ventas = ttk.Treeview(
            tabla_frame,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "id": "ID VENTA",
            "cedula": "CÉDULA / ID",
            "usuario": "USUARIO",
            "producto": "PRODUCTO",
            "fecha": "FECHA"
        }

        for columna in columnas:

            self.tabla_ventas.heading(
                columna,
                text=encabezados[columna]
            )

        self.tabla_ventas.column(
            "id",
            width=80
        )

        self.tabla_ventas.column(
            "cedula",
            width=150
        )

        self.tabla_ventas.column(
            "usuario",
            width=180
        )

        self.tabla_ventas.column(
            "producto",
            width=230
        )

        self.tabla_ventas.column(
            "fecha",
            width=180
        )

        self.tabla_ventas.pack(
            expand=True,
            fill="both"
        )

        self.actualizar_ventas()

    # =================================================
    # CARGAR COMBOS
    # =================================================

    def cargar_combos(self):

        if not hasattr(
            self,
            "combo_usuario"
        ):
            return

        if not hasattr(
            self,
            "combo_producto"
        ):
            return

        usuarios = []

        for usuario in self.servicio.usuarios:

            usuarios.append(
                f"{usuario.identificacion} - "
                f"{usuario.nombre}"
            )

        self.combo_usuario["values"] = usuarios

        productos = []

        for producto in self.servicio.productos:

            if producto.disponible:

                productos.append(
                    f"{producto.codigo} - "
                    f"{producto.nombre} - "
                    f"${producto.precio:.2f} - "
                    f"Stock: {producto.stock}"
                )

        self.combo_producto["values"] = productos

    # =================================================
    # REGISTRAR VENTA
    # =================================================

    def registrar_venta(self):

        usuario_seleccionado = (
            self.combo_usuario.get()
        )

        producto_seleccionado = (
            self.combo_producto.get()
        )

        if not usuario_seleccionado:

            messagebox.showwarning(
                "Datos incompletos",
                "Seleccione un usuario."
            )

            return

        if not producto_seleccionado:

            messagebox.showwarning(
                "Datos incompletos",
                "Seleccione un producto."
            )

            return

        # ==========================================
        # OBTENER CÉDULA
        # ==========================================

        cedula = (
            usuario_seleccionado
            .split(" - ", 1)[0]
        )

        # ==========================================
        # OBTENER CÓDIGO
        # ==========================================

        codigo = (
            producto_seleccionado
            .split(" - ", 1)[0]
        )

        try:

            resultado = self.servicio.registrar_venta(
                cedula,
                codigo
            )

            # ======================================
            # COMPATIBLE CON RESULTADO DICCIONARIO
            # ======================================

            if isinstance(
                resultado,
                dict
            ):

                if not resultado.get(
                    "ok",
                    False
                ):

                    messagebox.showwarning(
                        "No se pudo registrar",
                        resultado.get(
                            "mensaje",
                            "No se pudo registrar la venta."
                        )
                    )

                    return

                venta = resultado.get(
                    "venta"
                )

            else:

                venta = resultado

            # ======================================
            # ACTUALIZAR SOLO LA VISTA DE VENTAS
            # ======================================

            self.actualizar_ventas()

            # Actualizar productos disponibles
            # del ComboBox
            self.cargar_combos()

            # ======================================
            # LIMPIAR SELECCIÓN
            # ======================================

            self.combo_usuario.set("")
            self.combo_producto.set("")

            # ======================================
            # MENSAJE
            # ======================================

            if venta is not None:

                id_venta = getattr(
                    venta,
                    "id",
                    "N/A"
                )

                messagebox.showinfo(
                    "Venta registrada",
                    "¡Venta registrada correctamente!\n\n"
                    f"ID de venta: {id_venta}\n"
                    f"Cédula: {cedula}\n"
                    f"Producto: {codigo}"
                )

            else:

                messagebox.showinfo(
                    "Venta registrada",
                    "¡Venta registrada correctamente!"
                )

        except Exception as error:

            messagebox.showerror(
                "Error al registrar venta",
                str(error)
            )

    # =================================================
    # ACTUALIZAR VENTAS
    # =================================================

    def actualizar_ventas(self):

        if not hasattr(
            self,
            "tabla_ventas"
        ):
            return

        try:

            self.tabla_ventas.delete(
                *self.tabla_ventas.get_children()
            )

        except tk.TclError:

            return

        for venta in self.servicio.ventas:

            usuario = (
                self.servicio.buscar_usuario(
                    venta.usuario_id
                )
            )

            producto = (
                self.servicio.buscar_producto(
                    venta.producto_codigo
                )
            )

            nombre_usuario = (
                usuario.nombre
                if usuario
                else "Desconocido"
            )

            nombre_producto = (
                producto.nombre
                if producto
                else "Desconocido"
            )

            try:

                self.tabla_ventas.insert(
                    "",
                    "end",
                    values=(
                        venta.id,
                        venta.usuario_id,
                        nombre_usuario,
                        nombre_producto,
                        venta.fecha
                    )
                )

            except tk.TclError:

                return

    # =================================================
    # BOTONES DE ACCIONES
    # =================================================

    def crear_boton_accion(
        self,
        padre,
        texto,
        color,
        comando
    ):

        boton = tk.Button(
            padre,
            text=texto,
            font=("Arial", 9, "bold"),
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=comando
        )

        boton.pack(
            side="left",
            padx=5,
            ipadx=10,
            ipady=7
        )

    # =================================================
    # USUARIOS
    # =================================================

    def consultar_usuarios(self):

        self.cargar_usuarios()

    def registrar_usuario(self):

        messagebox.showinfo(
            "Registrar usuario",
            "La opción de registrar usuarios "
            "está disponible para implementar."
        )

    def actualizar_usuario(self):

        messagebox.showinfo(
            "Actualizar usuario",
            "Seleccione un usuario para actualizar."
        )

    def eliminar_usuario(self):

        messagebox.showinfo(
            "Eliminar usuario",
            "Seleccione un usuario para eliminar."
        )

    # =================================================
    # PRODUCTOS
    # =================================================

    def consultar_productos(self):

        self.cargar_productos()

    def registrar_producto(self):

        messagebox.showinfo(
            "Registrar producto",
            "La opción de registrar productos "
            "está disponible para implementar."
        )

    def actualizar_producto(self):

        messagebox.showinfo(
            "Actualizar producto",
            "Seleccione un producto para actualizar."
        )

    def eliminar_producto(self):

        messagebox.showinfo(
            "Eliminar producto",
            "Seleccione un producto para eliminar."
        )

    # =================================================
    # LIMPIAR TABLAS
    # =================================================

    def limpiar_tabla(self):

        if hasattr(
            self,
            "tabla_usuarios"
        ):

            try:

                self.tabla_usuarios.delete(
                    *self.tabla_usuarios.get_children()
                )

            except tk.TclError:
                pass

        if hasattr(
            self,
            "tabla_productos"
        ):

            try:

                self.tabla_productos.delete(
                    *self.tabla_productos.get_children()
                )

            except tk.TclError:
                pass

        if hasattr(
            self,
            "tabla_ventas"
        ):

            try:

                self.tabla_ventas.delete(
                    *self.tabla_ventas.get_children()
                )

            except tk.TclError:
                pass