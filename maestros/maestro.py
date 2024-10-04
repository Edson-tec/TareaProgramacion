from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Maestro(Usuario):

    fecha_nacimiento: datetime
    rfc: str 
    sueldo: float

    def __init__(self, numero_control: str, nombre: str, apellido: str, fecha_nacimiento: datetime, rfc: str, sueldo:float, contraseña: str):
        super.__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Rol.MAESTRO)
        self.fecha_nacimiento = fecha_nacimiento
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"\n-Numero de control: {self.numero_control}, nombre completo: {nombre_completo}, rfc: {self.rfc}, fecha de nacimineto: {self.fecha_nacimiento}, sueldo: {self.sueldo}"      
        return info  