import math
from traceback import print_tb


def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

# Exemplo de uso
raio = float(input("Digite o raio do circulo: "))
calcular_area_circulo(raio)
print(f"A área do circulo com raio {raio} é {}")