from curso import Curso
from estudiante import Estudiante

curso_uno = Curso("Electrónica Analógica", 1032, "John Wick")
curso_dos = Curso("Inglés", 7433, "Eder Rivera")
curso_tres = Curso("Algebra", 5423, "Fernando Avila")

estudiante_uno = Estudiante("Edson Jared Martínez Gómez", 19, 22121069)
estudiante_dos = Estudiante("Jaime Macías Álvarez", 20, 22121045)

estudiante_uno.agregar_cursos(curso_uno)
estudiante_uno.agregar_cursos(curso_dos)
estudiante_uno.agregar_cursos(curso_tres)

estudiante_dos.agregar_cursos(curso_uno)
estudiante_dos.agregar_cursos(curso_tres)

curso_uno.mostrar_info_curso()
curso_dos.mostrar_info_curso()
curso_tres.mostrar_info_curso()

estudiante_uno.mostrar_informacion()
estudiante_dos.mostrar_informacion()
