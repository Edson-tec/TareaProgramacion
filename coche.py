class Coche:

    marca = ""
    modelo = ""
    año = 0

    #Metodo Constructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

         # Mostrar Informacion 
    def mostrar_informacion(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.año)

        #Para calcular edad
    def calcular_edad_del_coche(self, año_actual):
        return año_actual - self.año



