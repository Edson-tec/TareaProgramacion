class Estudiante:
    nombre = ""
    edad = 0
    id_estudiante = 0
    cursos = []

    def __init__(self, nombre, edad, id_estudiante):       

        self.nombre = nombre
        self.edad = edad    
        self.id_estudiante = id_estudiante  
        self.cursos = []     
    
    def agregar_cursos(self, curso):
        self.cursos.append(curso)

    def mostrar_informacion(self):
        print("\nEstudiante: ", self.nombre)
        print("Edad: ", self.edad)
        print("Numero de Control: ", self.id_estudiante)
        print("Cursando: " )

        for curso in self.cursos:
            print("*", curso.nombre_curso,"*")         