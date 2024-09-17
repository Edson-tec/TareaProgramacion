"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente import Paciente
from medico import Medico
from hospital import Hospital

hospital = Hospital()

paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero") # 5
paciente_dos = Paciente("Jonathan", 2017, 70, 1.90, "Avenida Madero") # 5
paciente_tres = Paciente("Jaime", 2000, 72, 1.92, "Avenida Revolución")

medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo") # 8
medico_dos = Medico("Jesus", 1991, "AD92JKLDFSJ", "Acueducto")

hospital.registrar_paciente(paciente=paciente)
hospital.registrar_paciente(paciente=paciente_dos)
hospital.registrar_paciente(paciente=paciente_tres)

hospital.registrar_medico(medico=medico)
hospital.registrar_medico(medico=medico_dos)

hospital.mostrar_pacientes()
hospital.mostrar_medicos()

hospital.mostrar_pacientes_menores()
hospital.mostrar_pacientes_mayores()

id_paciente_eliminar = int(input("Ingresa el id del paciente que deseas eliminar: "))
id_medico_eliminar = int(input("Ingresa el id del medico que deseas eliminar: "))

hospital.eliminar_paciente(id_paciente_eliminar)
hospital.eliminar_medico(id_medico_eliminar)

hospital.mostrar_pacientes()
hospital.mostrar_medicos()

#hospital.registrar_consulta(id_paciente=1, id_medico=1)
