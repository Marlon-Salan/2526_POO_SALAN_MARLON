# Programa para calcular el promedio semanal del clima usando POO

class ClimaDiario:
    def __init__(self):
        # Encapsulamos la lista de temperaturas
        self.__temperaturas = []

    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas de los 7 días de la semana:")
        for i in range(7):
            temp = float(input(f"Día {i+1}: "))
            self.__temperaturas.append(temp)

    def calcular_promedio(self):
        return sum(self.__temperaturas) / len(self.__temperaturas)

# Clase hija que demuestra herencia
class ClimaExtendido(ClimaDiario):
    def mostrar_promedio(self):
        promedio = self.calcular_promedio()
        print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

# Programa principal
def main():
    clima = ClimaExtendido()
    clima.ingresar_temperaturas()
    clima.mostrar_promedio()

# Ejecutar el programa
if __name__ == "__main__":
    main()