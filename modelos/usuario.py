class Usuario:

    def __init__(self, identificacion, nombre, usuario, contrasena):
        self.identificacion = identificacion
        self.nombre = nombre
        self.usuario = usuario
        self.contrasena = contrasena

    def convertir_a_diccionario(self):
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "usuario": self.usuario,
            "contraseña": self.contrasena
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            identificacion=datos["identificacion"],
            nombre=datos["nombre"],
            usuario=datos["usuario"],
            contrasena=datos["contraseña"]
        )