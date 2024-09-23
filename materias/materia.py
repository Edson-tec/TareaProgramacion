class Materia:
    
    numero_control: str
    nombre_materia: str
    descripcion: str
    semestre: int
    creditos: int

    def __init__(self, numero_control: str, nombre_materia: str, descripcion: str, semestre: int, creditos: int):
        self.numero_control = numero_control
        self.nombre_materia = nombre_materia
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos