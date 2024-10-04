from datetime import datetime
from usuario.usuario import Usuario
from usuario.utils.roles import Rol

class Coordinador(Usuario):

    sueldo: float
    rfc: str 
    años_antiguedad: int

    def __init__(self, numero_control: str, nombre: str, apellido: str, rfc: str, sueldo:float, años_antiguedad: int, contraseña: str):
        super.__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, rol=Rol.COORDINADOR)
        self.sueldo = sueldo
        self.rfc = rfc
        self.años_antiguedad = años_antiguedad
        

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"\n-Numero de control: {self.numero_control}, nombre completo: {nombre_completo}, rfc: {self.rfc}, años de antiguedad: {self.años_antiguedad}, sueldo: {self.sueldo}"      
        return info  