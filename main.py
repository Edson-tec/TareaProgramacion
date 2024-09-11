from coche import Coche

print("\n")
print("-----Primer Coche-----")
coche_uno = Coche("Nissan", "240Z", 1970)
coche_uno.mostrar_informacion()

print("\n")
print("-----Segundo Coche-----")
coche_dos = Coche("Subaru", "BRZ", 2020)
coche_dos.mostrar_informacion()

print("\n")
print("-----Tercer Coche-----")
coche_tres = Coche("Toyota", "Corolla", 2010)
coche_tres.mostrar_informacion()

print("\n")
print("-----Cuarto Coche-----")
coche_cuatro = Coche("Honda", "civic", 2008)
coche_cuatro.mostrar_informacion()


#calcular la edad de cada coche
año_actual = 2024
print(f"\nEl primer coche tiene {coche_uno.calcular_edad_del_coche(año_actual)} años.")
print(f"\nEl segundo coche tiene {coche_dos.calcular_edad_del_coche(año_actual)} años.")
print(f"\nEl tercer coche tiene {coche_tres.calcular_edad_del_coche(año_actual)} años.")
print(f"\nEl cuarto coche tiene {coche_cuatro.calcular_edad_del_coche(año_actual)} años.")

