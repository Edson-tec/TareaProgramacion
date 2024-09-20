from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        # L - 2024 - 09 - longitud lista estudiantes + 1 + random(0, 10000)
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 10000)}"
        return numero_control
    

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_maestro(self, nombre_maestro: str, rfc: str, año_nacimiento: int):
        # M-{año de nacimiento}-{dia actual}-{numero aleatorio entre 500 y 5000}-{las primeras 2 letras de su nombre}-{las ultimas 2 letras de su RFC}-{la longitud de la lista de los profesores más uno}
        numero_control = f"M{año_nacimiento}{datetime.now().day}{randint(500, 5000)}{nombre_maestro[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestros) + 1}"
        return numero_control
        