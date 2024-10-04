from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from semestre.semestre import Semestre
from datetime import datetime
from carrera.carrera import Carrera
from grupos.grupo import Grupo


class Menu:
    escuela = Escuela()
    usuario_estudiante = str = "Juan123"
    contraseña_estudiante = str = "12345*"

    usuario_maestro = str = "Juan123"
    contraseña_maestro = str = "12345*"

    def login(self):
        intentos_usuario = 0
        while intentos_usuario < 5:
            print("\n***BIENVENIDO***")
            print("Inicia sesión para continuar")

            nombre_usuario = input("Ingresa tu nombre de usuario: ")
            contraseña_usuario = input("Ingresa tu contraseña de usuario: ")

            if nombre_usuario == self.usuario_estudiante:
                if contraseña_usuario == self.contraseña_estudiante:
                    self.mostrar_menu_estudiante()
                    intentos_usuario = 0
            elif nombre_usuario == self.usuario_maestro:
                if contraseña_usuario == self.contraseña_maestro:
                    self.mostrar_menu_maestro()
                    intentos_usuario = 0

            if nombre_usuario == self.usuario_estudiante and contraseña_usuario == self.contraseña_estudiante:
                self.mostrar_menu()

            else:
                self.mostrar_intento_sesion_fallido()

        print("Maximo de intentos de inicio de sesion alcanzados. Bye bye")
    


    def mostrar_intento_sesion_fallido(self):
        intentos_usuario = 0
        print("Usuario o contraseña incorrectos. Intenta de nuevo")
        return intentos_usuario + 1


    def mostrar_menu_estudiante(self):
        pass


    def mostrar_menu_maestro(self):
        opcion = 0
        while opcion != 5:
            print("\n***MINDBOX***")
            print("1. Ver horarios")
            print("1. Ver grupos")
            print("1. Ver materias")
            print("1. Ver alumnos")
            print("5. Salir")

            opcion = int(input("Ingresa una opción"))

    def mostrar_menu(self):
        while True:
            print("\n** MINDBOX **")
            print("1. Registar estudiante")
            print("2. Registar maestro")
            print("3. Registar materia")
            print("4. Registar grupo")
            print("5. Registar horario")
            print("6. Mostrar Estudiantes")
            print("7. Mostrar Maestros") #Tarea
            print("8. Mostrar Materias") #Tarea
            print("9. Mostrar Grupos")
            print("10. Eliminar Estudiante")
            print("11. Eliminar Maestro")#Tarea
            print("12. Eliminar Materia")#Tarea
            print("13. Registrar Carrera")
            print("14. Registrar Semestre")
            print("15. Mostrar Carreras")
            print("16. Mostrar Semestres")
            print("17. Salir")
    
            opcion = input("Ingresa una opción para continuar: ")

            if opcion == "1":
                print("\n Seleccionaste la opcion para registrar un estudiante")

                numero_control = self.escuela.generar_numero_control()
                print(numero_control)


                nombre = input("ingresa el nombre del estudiante: ")
                apellido = input("ingresa el apellido del estudiante: ") 
                contraseña = input("Ingresa la contraseña: ")
                curp = input("ingresa la curp del estudiante: ")
                año = int(input("ingrese el año de nacimiento del estudiante: "))
                mes = int(input("ingrese el mes de nacimiento del estudiante: "))
                dia = int(input("ingrese el dia de nacimiento del estudiante: "))
                fecha_nacimiento = datetime(año, mes, dia)

                estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, contraseña=contraseña, curp=curp, fecha_nacimiento=fecha_nacimiento)


                self.escuela.registrar_estudiante(estudiante)
                print(f"Estudiante {nombre} {apellido} registrado exitosamente.\n")

            if opcion == "2":
                print("\n Seleccionaste la opcion para registrar un maestro")

                nombre_maestro = input("Ingresa el nombre del maestro: ")
                apellido = input("Ingresa el apellido del maestro: ") 
                contraseña = input("Ingresa la contraseña: ")
                rfc = input("Ingresa el RFC del maestro: ")
                sueldo = float(input("Ingresa el sueldo del maestro: "))
                año = int(input("Ingresa el año de nacimiento del maestro: "))
                mes = int(input("Ingresa el mes de nacimiento del maestro: "))
                dia = int(input("Ingresa el día de nacimiento del maestro: "))
                fecha_nacimiento = datetime(año, mes, dia)

                numero_control_maestro = self.escuela.generar_numero_control_maestro(nombre_maestro, rfc, año)
                print(f"Número de control del Maestro: {numero_control_maestro}")

                maestro = Maestro(nombre_maestro=nombre_maestro, apellido=apellido, contraseña=contraseña, rfc=rfc, fecha_nacimiento=fecha_nacimiento, numero_control=numero_control_maestro, sueldo=sueldo)

                self.escuela.registrar_maestro(maestro)
                print(f"Maestro {nombre_maestro} {apellido} registrado exitosamente.\n")



            if opcion == "3":
                print("\n Seleccionaste la opcion para registrar una materia")

                nombre_materia = input("Ingresa el nombre de la materia: ")
                descripcion = input("Ingresa la descripcion de la materia: ") 
                semestre = int(input("Ingresa el semestre de la materia: "))
                creditos = int(input("Ingresa los creditos de la materia: "))

                numero_control_materia = self.escuela.generar_numero_control_materia(nombre_materia, semestre, creditos)
                print(f"\nNúmero de control de la materia: {numero_control_materia}")

                materia = Materia(numero_control=numero_control_materia, nombre_materia=nombre_materia, descripcion=descripcion, semestre=semestre, creditos=creditos)

                self.escuela.registrar_materia(materia)
                print(f"Materia {nombre_materia} registrada exitosamente.\n")

            if opcion == "4":

                print("\n Seleccionaste la opcion para registrar un nuevo grupo")

                tipo = input("Ingresa el tipo de grupo (A/B)")
                id_semestre = input("ingresa el ID del semestre al que pertenece el grupo")

                grupo = Grupo(tipo=tipo, id_semestre=id_semestre)

                self.escuela.registrar_grupo(grupo=grupo)

            if opcion == "5":
                pass
            if opcion == "6":
                self.escuela.listar_estudiantes()

            if opcion == "7":
                self.escuela.listar_maestros()

            if opcion == "8":
                self.escuela.listar_materias()

            if opcion == "9":
                self.escuela.listar_grupos()

            if opcion == "10":
                print("\nSeleccionaste la opcion para eliminar un estudiante")

                numero_control = input("Ingresa el numero de control del estudiante")

                self.escuela.eliminar_estudiante(numero_control=numero_control)

            if opcion == "11":
                print("\nSeleccionaste la opcion para eliminar un maestro")

                numero_control = input("Ingresa el numero de control del maestro")

                self.escuela.eliminar_maestro(numero_control=numero_control)

            if opcion == "12":
                print("\nSeleccionaste la opcion para eliminar una materia")

                numero_control = input("Ingresa el numero de control de la materia que quieres eliminar: ")

                self.escuela.eliminar_materia(numero_control=numero_control)

            if opcion == "13":
                print("\nSeleccionaste la opcion para Registrar una Carrera")

                nombre = input("Ingresa el nombre de la carrera: ")

                carrera = Carrera(nombre=nombre)

                self.escuela.registrar_carrera(carrera)

            if opcion == "14":
                print("\nSeleccionaste la opcion para Registrar un Semestre")

                numero = input("Ingresa el numero del semestre: ")
                id_carrera = input("Ingresa el ID de la carrera: ")

                semestre = Semestre(numero=numero, id_carrera=id_carrera)

                self.escuela.registrar_semestre(semestre=semestre)

            if opcion == "15":
                self.escuela.listar_carreras()
            
            if opcion == "16":
                self.escuela.listar_semestres()

            if opcion == "17":
                print("Hasta Luego")
                break