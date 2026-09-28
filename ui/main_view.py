import tkinter as tk
from tkinter import ttk, messagebox
from pathlib import Path


class MainView:

    def __init__(
        self,
        root,
        servicio,
        usuario,
        cerrar_sesion
    ):

        self.root = root
        self.servicio = servicio
        self.usuario = usuario
        self.cerrar_sesion = cerrar_sesion

        self.root.title(
            "SULTAN RESTAURANT - TURKISH BBQ"
        )

        self.root.geometry(
            "1200x720"
        )

        self.root.minsize(
            1000,
            650
        )

        self.logo = None
        self.icono = None

        base = Path(
            __file__
        ).resolve().parent.parent

        assets = base / "assets"

        try:

            self.logo = tk.PhotoImage(
                file=assets / "logo.png"
            )

        except Exception:

            self.logo = None

        try:

            self.icono = tk.PhotoImage(
                file=assets / "icono.png"
            )

            self.root.iconphoto(
                True,
                self.icono
            )

        except Exception:

            self.icono = None

        self.configurar_estilos()
        self.crear_interfaz()

        self.mostrar_inicio()

    # ==========================================================
    # ESTILOS
    # ==========================================================

    def configurar_estilos(self):

        estilo = ttk.Style()

        try:

            estilo.theme_use(
                "clam"
            )

        except Exception:

            pass

        estilo.configure(
            "Treeview",
            font=("Arial", 10),
            rowheight=30
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        estilo.configure(
            "TCombobox",
            padding=5,
            font=("Arial", 10)
        )

    # ==========================================================
    # INTERFAZ
    # ==========================================================

    def crear_interfaz(self):

        self.menu = tk.Frame(
            self.root,
            bg="#CFDDDA",
            width=290
        )

        self.menu.pack(
            side="left",
            fill="y"
        )

        self.menu.pack_propagate(
            False
        )

        self.contenido = tk.Frame(
            self.root,
            bg="#F4F4F4"
        )

        self.contenido.pack(
            side="right",
            fill="both",
            expand=True
        )

        # LOGO

        self.logo_frame = tk.Frame(
            self.menu,
            bg="#F5EEDC",
            height=125
        )

        self.logo_frame.pack(
            fill="x"
        )

        self.logo_frame.pack_propagate(
            False
        )

        if self.logo:

            logo_mostrar = self.logo

            try:

                while (
                    logo_mostrar.width() > 180
                    or
                    logo_mostrar.height() > 100
                ):

                    logo_mostrar = (
                        logo_mostrar.subsample(
                            2,
                            2
                        )
                    )

            except Exception:

                pass

            self.logo_label = tk.Label(
                self.logo_frame,
                image=logo_mostrar,
                bg="#F5EEDC"
            )

            self.logo_label.image = logo_mostrar

            self.logo_label.pack(
                pady=8
            )

        # NOMBRE

        tk.Label(
            self.menu,
            text="SULTAN RESTAURANT",
            bg="#D7D6E0",
            fg="#3B2F2F",
            font=("Arial", 16, "bold")
        ).pack(
            fill="x"
        )

        tk.Label(
            self.menu,
            text="TURKISH BBQ",
            bg="#F5EEDC",
            fg="#AA0BB8",
            font=("Arial", 12, "bold")
        ).pack(
            fill="x",
            pady=(0, 10)
        )

        tk.Frame(
            self.menu,
            bg="#C49A3A",
            height=3
        ).pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        self.crear_boton_menu(
            "INICIO",
            self.mostrar_inicio
        )

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

        tk.Frame(
            self.menu,
            bg="#CFDDDA"
        ).pack(
            fill="both",
            expand=True
        )

        tk.Button(
            self.menu,
            text="CERRAR SESIÓN",
            command=self.cerrar_sesion,
            bg="#52B474",
            fg="white",
            activebackground="#A91414",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            height=2
        ).pack(
            fill="x",
            padx=20,
            pady=20
        )

    # ==========================================================
    # BOTÓN MENÚ
    # ==========================================================

    def crear_boton_menu(
        self,
        texto,
        comando
    ):

        tk.Button(
            self.menu,
            text=texto,
            command=comando,
            bg="#CFDDDA",
            fg="#3B2F2F",
            activebackground="#B7C9C5",
            activeforeground="#3B2F2F",
            font=("Arial", 11, "bold"),
            relief="flat",
            cursor="hand2",
            height=2
        ).pack(
            fill="x",
            padx=20,
            pady=4
        )

    # ==========================================================
    # LIMPIAR CONTENIDO
    # ==========================================================

    def limpiar_contenido(self):

        for widget in self.contenido.winfo_children():

            widget.destroy()

        # Eliminamos referencias a tablas antiguas
        if hasattr(
            self,
            "tabla_usuarios"
        ):

            del self.tabla_usuarios

        if hasattr(
            self,
            "tabla_productos"
        ):

            del self.tabla_productos

        if hasattr(
            self,
            "tabla_ventas"
        ):

            del self.tabla_ventas

    # ==========================================================
    # INICIO
    # ==========================================================

    def mostrar_inicio(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Panel principal",
            bg="#F4F4F4",
            fg="#3B2F2F",
            font=("Arial", 24, "bold")
        ).pack(
            pady=(35, 5)
        )

        tk.Label(
            self.contenido,
            text="Bienvenida a SULTAN RESTAURANT - TURKISH BBQ",
            bg="#F4F4F4",
            fg="#666666",
            font=("Arial", 12)
        ).pack(
            pady=(0, 30)
        )

        contenedor = tk.Frame(
            self.contenido,
            bg="#F4F4F4"
        )

        contenedor.pack()

        self.crear_tarjeta(
            contenedor,
            "USUARIOS",
            len(self.servicio.usuarios),
            "#4A90E2",
            0
        )

        self.crear_tarjeta(
            contenedor,
            "PRODUCTOS",
            len(self.servicio.productos),
            "#52B474",
            1
        )

        self.crear_tarjeta(
            contenedor,
            "VENTAS",
            len(self.servicio.ventas),
            "#F39C12",
            2
        )

    # ==========================================================
    # TARJETAS
    # ==========================================================

    def crear_tarjeta(
        self,
        padre,
        titulo,
        cantidad,
        color,
        columna
    ):

        tarjeta = tk.Frame(
            padre,
            bg="white",
            width=220,
            height=150,
            relief="solid",
            bd=1
        )

        tarjeta.grid(
            row=0,
            column=columna,
            padx=15
        )

        tarjeta.grid_propagate(
            False
        )

        tk.Label(
            tarjeta,
            text=titulo,
            bg="white",
            fg=color,
            font=("Arial", 13, "bold")
        ).pack(
            pady=(25, 8)
        )

        tk.Label(
            tarjeta,
            text=str(cantidad),
            bg="white",
            fg="#333333",
            font=("Arial", 28, "bold")
        ).pack()

    # ==========================================================
    # USUARIOS
    # ==========================================================

    def mostrar_usuarios(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de Usuarios",
            bg="#F4F4F4",
            fg="#3B2F2F",
            font=("Arial", 22, "bold")
        ).pack(
            pady=(25, 15)
        )

        botones = tk.Frame(
            self.contenido,
            bg="#F4F4F4"
        )

        botones.pack(
            pady=(0, 15)
        )

        self.crear_boton_accion(
            botones,
            "REGISTRAR",
            "#52B474",
            self.registrar_usuario,
            0
        )

        self.crear_boton_accion(
            botones,
            "CONSULTAR",
            "#4A90E2",
            self.consultar_usuarios,
            1
        )

        self.crear_boton_accion(
            botones,
            "ACTUALIZAR",
            "#F39C12",
            self.actualizar_usuario,
            2
        )

        self.crear_boton_accion(
            botones,
            "ELIMINAR",
            "#D9534F",
            self.eliminar_usuario,
            3
        )

        self.crear_boton_accion(
            botones,
            "LIMPIAR",
            "#777777",
            self.limpiar_tabla,
            4
        )

        tabla_frame = tk.Frame(
            self.contenido,
            bg="#F4F4F4"
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
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
            width=180,
            anchor="center"
        )

        self.tabla_usuarios.column(
            "nombre",
            width=300,
            anchor="center"
        )

        self.tabla_usuarios.column(
            "usuario",
            width=220,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_usuarios.yview
        )

        self.tabla_usuarios.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_usuarios.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.cargar_usuarios()

    def cargar_usuarios(self):

        if not hasattr(
            self,
            "tabla_usuarios"
        ):

            return

        if not self.tabla_usuarios.winfo_exists():

            return

        for item in self.tabla_usuarios.get_children():

            self.tabla_usuarios.delete(
                item
            )

        for usuario in self.servicio.listar_usuarios():

            self.tabla_usuarios.insert(
                "",
                "end",
                values=(
                    usuario.identificacion,
                    usuario.nombre,
                    usuario.usuario
                )
            )

    def consultar_usuarios(self):

        self.cargar_usuarios()

        messagebox.showinfo(
            "Consulta",
            f"Usuarios registrados: "
            f"{len(self.servicio.usuarios)}"
        )

    # ==========================================================
    # REGISTRAR USUARIO
    # ==========================================================

    def registrar_usuario(self):

        ventana = tk.Toplevel(
            self.root
        )

        ventana.title(
            "Registrar usuario"
        )

        ventana.geometry(
            "430x430"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            bg="#F4F4F4"
        )

        ventana.transient(
            self.root
        )

        ventana.grab_set()

        tk.Label(
            ventana,
            text="REGISTRAR USUARIO",
            bg="#F4F4F4",
            fg="#3B2F2F",
            font=("Arial", 18, "bold")
        ).pack(
            pady=20
        )

        campos = {}

        datos = [
            ("ID / CÉDULA", "identificacion"),
            ("NOMBRE", "nombre"),
            ("USUARIO", "usuario"),
            ("CONTRASEÑA", "contrasena")
        ]

        for texto, clave in datos:

            tk.Label(
                ventana,
                text=texto,
                bg="#F4F4F4",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).pack(
                anchor="w",
                padx=40,
                pady=(5, 2)
            )

            entrada = tk.Entry(
                ventana,
                font=("Arial", 11),
                width=35
            )

            if clave == "contrasena":

                entrada.config(
                    show="*"
                )

            entrada.pack(
                padx=40,
                pady=(0, 5)
            )

            campos[clave] = entrada

        def guardar():

            try:

                self.servicio.registrar_usuario(
                    campos["identificacion"].get(),
                    campos["nombre"].get(),
                    campos["usuario"].get(),
                    campos["contrasena"].get()
                )

                ventana.destroy()

                self.cargar_usuarios()

                messagebox.showinfo(
                    "Éxito",
                    "Usuario registrado correctamente."
                )

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        tk.Button(
            ventana,
            text="GUARDAR",
            command=guardar,
            bg="#52B474",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=18,
            height=2
        ).pack(
            pady=20
        )

    # ==========================================================
    # ACTUALIZAR USUARIO
    # ==========================================================

    def actualizar_usuario(self):

        if not hasattr(
            self,
            "tabla_usuarios"
        ):

            return

        seleccion = (
            self.tabla_usuarios.selection()
        )

        if not seleccion:

            messagebox.showwarning(
                "Actualizar",
                "Seleccione un usuario de la tabla."
            )

            return

        valores = self.tabla_usuarios.item(
            seleccion[0],
            "values"
        )

        identificacion = valores[0]

        usuario_obj = (
            self.servicio.buscar_usuario(
                identificacion
            )
        )

        if usuario_obj is None:

            messagebox.showerror(
                "Error",
                "No se encontró el usuario."
            )

            return

        ventana = tk.Toplevel(
            self.root
        )

        ventana.title(
            "Actualizar usuario"
        )

        ventana.geometry(
            "430x430"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            bg="#F4F4F4"
        )

        ventana.grab_set()

        tk.Label(
            ventana,
            text="ACTUALIZAR USUARIO",
            bg="#F4F4F4",
            fg="#3B2F2F",
            font=("Arial", 18, "bold")
        ).pack(
            pady=20
        )

        campos = {}

        datos = [
            (
                "ID / CÉDULA",
                "identificacion",
                usuario_obj.identificacion
            ),
            (
                "NOMBRE",
                "nombre",
                usuario_obj.nombre
            ),
            (
                "USUARIO",
                "usuario",
                usuario_obj.usuario
            ),
            (
                "CONTRASEÑA",
                "contrasena",
                usuario_obj.contrasena
            )
        ]

        for texto, clave, valor in datos:

            tk.Label(
                ventana,
                text=texto,
                bg="#F4F4F4",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).pack(
                anchor="w",
                padx=40,
                pady=(5, 2)
            )

            entrada = tk.Entry(
                ventana,
                font=("Arial", 11),
                width=35
            )

            entrada.insert(
                0,
                str(valor)
            )

            if clave == "contrasena":

                entrada.config(
                    show="*"
                )

            entrada.pack(
                padx=40,
                pady=(0, 5)
            )

            campos[clave] = entrada

        def guardar():

            try:

                self.servicio.actualizar_usuario(
                    identificacion,
                    campos["identificacion"].get(),
                    campos["nombre"].get(),
                    campos["usuario"].get(),
                    campos["contrasena"].get()
                )

                ventana.destroy()

                self.cargar_usuarios()

                messagebox.showinfo(
                    "Éxito",
                    "Usuario actualizado correctamente."
                )

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        tk.Button(
            ventana,
            text="GUARDAR CAMBIOS",
            command=guardar,
            bg="#F39C12",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=20,
            height=2
        ).pack(
            pady=20
        )

    # ==========================================================
    # ELIMINAR USUARIO
    # ==========================================================

    def eliminar_usuario(self):

        if not hasattr(
            self,
            "tabla_usuarios"
        ):

            return

        seleccion = (
            self.tabla_usuarios.selection()
        )

        if not seleccion:

            messagebox.showwarning(
                "Eliminar",
                "Seleccione un usuario de la tabla."
            )

            return

        valores = self.tabla_usuarios.item(
            seleccion[0],
            "values"
        )

        identificacion = valores[0]
        nombre = valores[1]

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Desea eliminar al usuario?\n\n"
            f"{nombre}\n"
            f"ID: {identificacion}"
        )

        if not confirmar:

            return

        try:

            self.servicio.eliminar_usuario(
                identificacion
            )

            self.cargar_usuarios()

            messagebox.showinfo(
                "Éxito",
                "Usuario eliminado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==========================================================
    # PRODUCTOS
    # ==========================================================

    def mostrar_productos(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de Productos",
            bg="#F4F4F4",
            fg="#3B2F2F",
            font=("Arial", 22, "bold")
        ).pack(
            pady=(25, 15)
        )

        botones = tk.Frame(
            self.contenido,
            bg="#F4F4F4"
        )

        botones.pack(
            pady=(0, 15)
        )

        self.crear_boton_accion(
            botones,
            "REGISTRAR",
            "#52B474",
            self.registrar_producto,
            0
        )

        self.crear_boton_accion(
            botones,
            "CONSULTAR",
            "#4A90E2",
            self.consultar_productos,
            1
        )

        self.crear_boton_accion(
            botones,
            "ACTUALIZAR",
            "#F39C12",
            self.actualizar_producto,
            2
        )

        self.crear_boton_accion(
            botones,
            "ELIMINAR",
            "#D9534F",
            self.eliminar_producto,
            3
        )

        self.crear_boton_accion(
            botones,
            "LIMPIAR",
            "#777777",
            self.limpiar_tabla,
            4
        )

        tabla_frame = tk.Frame(
            self.contenido,
            bg="#F4F4F4"
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
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
            "nombre": "NOMBRE",
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
            width=100,
            anchor="center"
        )

        self.tabla_productos.column(
            "nombre",
            width=230,
            anchor="center"
        )

        self.tabla_productos.column(
            "precio",
            width=100,
            anchor="center"
        )

        self.tabla_productos.column(
            "categoria",
            width=180,
            anchor="center"
        )

        self.tabla_productos.column(
            "stock",
            width=90,
            anchor="center"
        )

        self.tabla_productos.column(
            "estado",
            width=120,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_productos.yview
        )

        self.tabla_productos.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_productos.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.cargar_productos()

    def cargar_productos(self):

        if not hasattr(
            self,
            "tabla_productos"
        ):

            return

        if not self.tabla_productos.winfo_exists():

            return

        for item in self.tabla_productos.get_children():

            self.tabla_productos.delete(
                item
            )

        for producto in self.servicio.listar_productos():

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

    def consultar_productos(self):

        self.cargar_productos()

        messagebox.showinfo(
            "Consulta",
            f"Productos registrados: "
            f"{len(self.servicio.productos)}"
        )

    # ==========================================================
    # REGISTRAR PRODUCTO
    # ==========================================================

    def registrar_producto(self):

        ventana = tk.Toplevel(
            self.root
        )

        ventana.title(
            "Registrar producto"
        )

        ventana.geometry(
            "430x500"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            bg="#F4F4F4"
        )

        ventana.grab_set()

        tk.Label(
            ventana,
            text="REGISTRAR PRODUCTO",
            bg="#F4F4F4",
            fg="#3B2F2F",
            font=("Arial", 18, "bold")
        ).pack(
            pady=20
        )

        campos = {}

        datos = [
            ("CÓDIGO", "codigo"),
            ("NOMBRE", "nombre"),
            ("PRECIO", "precio"),
            ("CATEGORÍA", "categoria"),
            ("STOCK", "stock")
        ]

        for texto, clave in datos:

            tk.Label(
                ventana,
                text=texto,
                bg="#F4F4F4",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).pack(
                anchor="w",
                padx=40,
                pady=(5, 2)
            )

            entrada = tk.Entry(
                ventana,
                font=("Arial", 11),
                width=35
            )

            entrada.pack(
                padx=40,
                pady=(0, 5)
            )

            campos[clave] = entrada

        def guardar():

            try:

                self.servicio.registrar_producto(
                    campos["codigo"].get(),
                    campos["nombre"].get(),
                    campos["precio"].get(),
                    campos["categoria"].get(),
                    campos["stock"].get()
                )

                ventana.destroy()

                self.cargar_productos()

                messagebox.showinfo(
                    "Éxito",
                    "Producto registrado correctamente."
                )

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        tk.Button(
            ventana,
            text="GUARDAR",
            command=guardar,
            bg="#52B474",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=18,
            height=2
        ).pack(
            pady=20
        )

    # ==========================================================
    # ACTUALIZAR PRODUCTO
    # ==========================================================

    def actualizar_producto(self):

        if not hasattr(
            self,
            "tabla_productos"
        ):

            return

        seleccion = (
            self.tabla_productos.selection()
        )

        if not seleccion:

            messagebox.showwarning(
                "Actualizar",
                "Seleccione un producto de la tabla."
            )

            return

        valores = self.tabla_productos.item(
            seleccion[0],
            "values"
        )

        codigo = valores[0]

        producto_obj = (
            self.servicio.buscar_producto(
                codigo
            )
        )

        if producto_obj is None:

            messagebox.showerror(
                "Error",
                "No se encontró el producto."
            )

            return

        ventana = tk.Toplevel(
            self.root
        )

        ventana.title(
            "Actualizar producto"
        )

        ventana.geometry(
            "430x500"
        )

        ventana.resizable(
            False,
            False
        )

        ventana.configure(
            bg="#F4F4F4"
        )

        ventana.grab_set()

        tk.Label(
            ventana,
            text="ACTUALIZAR PRODUCTO",
            bg="#F4F4F4",
            fg="#3B2F2F",
            font=("Arial", 18, "bold")
        ).pack(
            pady=20
        )

        campos = {}

        datos = [
            (
                "CÓDIGO",
                "codigo",
                producto_obj.codigo
            ),
            (
                "NOMBRE",
                "nombre",
                producto_obj.nombre
            ),
            (
                "PRECIO",
                "precio",
                producto_obj.precio
            ),
            (
                "CATEGORÍA",
                "categoria",
                producto_obj.categoria
            ),
            (
                "STOCK",
                "stock",
                producto_obj.stock
            )
        ]

        for texto, clave, valor in datos:

            tk.Label(
                ventana,
                text=texto,
                bg="#F4F4F4",
                fg="#333333",
                font=("Arial", 10, "bold")
            ).pack(
                anchor="w",
                padx=40,
                pady=(5, 2)
            )

            entrada = tk.Entry(
                ventana,
                font=("Arial", 11),
                width=35
            )

            entrada.insert(
                0,
                str(valor)
            )

            entrada.pack(
                padx=40,
                pady=(0, 5)
            )

            campos[clave] = entrada

        def guardar():

            try:

                self.servicio.actualizar_producto(
                    codigo,
                    campos["codigo"].get(),
                    campos["nombre"].get(),
                    campos["precio"].get(),
                    campos["categoria"].get(),
                    campos["stock"].get()
                )

                ventana.destroy()

                self.cargar_productos()

                messagebox.showinfo(
                    "Éxito",
                    "Producto actualizado correctamente."
                )

            except ValueError as error:

                messagebox.showerror(
                    "Error",
                    str(error),
                    parent=ventana
                )

        tk.Button(
            ventana,
            text="GUARDAR CAMBIOS",
            command=guardar,
            bg="#F39C12",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=20,
            height=2
        ).pack(
            pady=20
        )

    # ==========================================================
    # ELIMINAR PRODUCTO
    # ==========================================================

    def eliminar_producto(self):

        if not hasattr(
            self,
            "tabla_productos"
        ):

            return

        seleccion = (
            self.tabla_productos.selection()
        )

        if not seleccion:

            messagebox.showwarning(
                "Eliminar",
                "Seleccione un producto de la tabla."
            )

            return

        valores = self.tabla_productos.item(
            seleccion[0],
            "values"
        )

        codigo = valores[0]
        nombre = valores[1]

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Desea eliminar el producto?\n\n"
            f"{nombre}\n"
            f"Código: {codigo}"
        )

        if not confirmar:

            return

        try:

            self.servicio.eliminar_producto(
                codigo
            )

            self.cargar_productos()

            messagebox.showinfo(
                "Éxito",
                "Producto eliminado correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    # ==========================================================
    # VENTAS
    # ==========================================================

    def mostrar_ventas(self):

        self.limpiar_contenido()

        tk.Label(
            self.contenido,
            text="Gestión de Ventas",
            bg="#F4F4F4",
            fg="#3B2F2F",
            font=("Arial", 22, "bold")
        ).pack(
            pady=(25, 15)
        )

        formulario = tk.Frame(
            self.contenido,
            bg="white",
            relief="solid",
            bd=1
        )

        formulario.pack(
            fill="x",
            padx=30,
            pady=10
        )

        tk.Label(
            formulario,
            text="USUARIO / CÉDULA",
            bg="white",
            fg="#3B2F2F",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=0,
            padx=15,
            pady=(15, 5),
            sticky="w"
        )

        self.combo_usuario = ttk.Combobox(
            formulario,
            state="readonly",
            width=35
        )

        self.combo_usuario.grid(
            row=1,
            column=0,
            padx=15,
            pady=(0, 15)
        )

        tk.Label(
            formulario,
            text="PRODUCTO",
            bg="white",
            fg="#3B2F2F",
            font=("Arial", 10, "bold")
        ).grid(
            row=0,
            column=1,
            padx=15,
            pady=(15, 5),
            sticky="w"
        )

        self.combo_producto = ttk.Combobox(
            formulario,
            state="readonly",
            width=45
        )

        self.combo_producto.grid(
            row=1,
            column=1,
            padx=15,
            pady=(0, 15)
        )

        tk.Button(
            formulario,
            text="REGISTRAR VENTA",
            command=self.registrar_venta,
            bg="#52B474",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
            cursor="hand2",
            width=20,
            height=2
        ).grid(
            row=1,
            column=2,
            padx=15,
            pady=(0, 15)
        )

        tabla_frame = tk.Frame(
            self.contenido,
            bg="#F4F4F4"
        )

        tabla_frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
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
            "id": "ID",
            "cedula": "CÉDULA",
            "usuario": "USUARIO",
            "producto": "PRODUCTO",
            "fecha": "FECHA"
        }

        for columna in columnas:

            self.tabla_ventas.heading(
                columna,
                text=encabezados[columna]
            )

        for columna in columnas:

            self.tabla_ventas.column(
                columna,
                anchor="center"
            )

        scrollbar = ttk.Scrollbar(
            tabla_frame,
            orient="vertical",
            command=self.tabla_ventas.yview
        )

        self.tabla_ventas.configure(
            yscrollcommand=scrollbar.set
        )

        self.tabla_ventas.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.cargar_combos_ventas()
        self.actualizar_ventas()

    def cargar_combos_ventas(self):

        usuarios = []

        for usuario in self.servicio.listar_usuarios():

            usuarios.append(
                f"{usuario.identificacion} - "
                f"{usuario.nombre}"
            )

        self.combo_usuario["values"] = usuarios

        productos = []

        for producto in self.servicio.listar_productos():

            if producto.disponible:

                productos.append(
                    f"{producto.codigo} - "
                    f"{producto.nombre} - "
                    f"${producto.precio:.2f} - "
                    f"Stock: {producto.stock}"
                )

        self.combo_producto["values"] = productos

        self.combo_usuario.set("")
        self.combo_producto.set("")

    def registrar_venta(self):

        usuario = self.combo_usuario.get().strip()
        producto = self.combo_producto.get().strip()

        if not usuario:

            messagebox.showwarning(
                "Venta",
                "Seleccione un usuario."
            )

            return

        if not producto:

            messagebox.showwarning(
                "Venta",
                "Seleccione un producto."
            )

            return

        cedula = usuario.split(
            " - "
        )[0]

        codigo = producto.split(
            " - "
        )[0]

        try:

            self.servicio.registrar_venta(
                cedula,
                codigo
            )

            self.actualizar_ventas()
            self.cargar_combos_ventas()

            messagebox.showinfo(
                "Éxito",
                "Venta registrada correctamente."
            )

        except ValueError as error:

            messagebox.showerror(
                "Error",
                str(error)
            )

    def actualizar_ventas(self):

        if not hasattr(
            self,
            "tabla_ventas"
        ):

            return

        if not self.tabla_ventas.winfo_exists():

            return

        for item in self.tabla_ventas.get_children():

            self.tabla_ventas.delete(
                item
            )

        for venta in self.servicio.listar_ventas():

            usuario = self.servicio.buscar_usuario(
                venta.usuario_id
            )

            producto = self.servicio.buscar_producto(
                venta.producto_codigo
            )

            nombre_usuario = (
                usuario.nombre
                if usuario
                else "Usuario eliminado"
            )

            nombre_producto = (
                producto.nombre
                if producto
                else "Producto eliminado"
            )

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

    # ==========================================================
    # BOTONES DE ACCIÓN
    # ==========================================================

    def crear_boton_accion(
        self,
        padre,
        texto,
        color,
        comando,
        columna
    ):

        tk.Button(
            padre,
            text=texto,
            command=comando,
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            font=("Arial", 9, "bold"),
            relief="flat",
            cursor="hand2",
            width=13,
            height=2
        ).grid(
            row=0,
            column=columna,
            padx=5
        )

    # ==========================================================
    # LIMPIAR TABLA
    # ==========================================================

    def limpiar_tabla(self):

        # USUARIOS
        if hasattr(
            self,
            "tabla_usuarios"
        ):

            try:

                if self.tabla_usuarios.winfo_exists():

                    for item in (
                        self.tabla_usuarios.get_children()
                    ):

                        self.tabla_usuarios.delete(
                            item
                        )

                    return

            except tk.TclError:

                pass

        # PRODUCTOS
        if hasattr(
            self,
            "tabla_productos"
        ):

            try:

                if self.tabla_productos.winfo_exists():

                    for item in (
                        self.tabla_productos.get_children()
                    ):

                        self.tabla_productos.delete(
                            item
                        )

                    return

            except tk.TclError:

                pass

        # VENTAS
        if hasattr(
            self,
            "tabla_ventas"
        ):

            try:

                if self.tabla_ventas.winfo_exists():

                    for item in (
                        self.tabla_ventas.get_children()
                    ):

                        self.tabla_ventas.delete(
                            item
                        )

                    return

            except tk.TclError:

                pass