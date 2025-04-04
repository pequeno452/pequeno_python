def calcular_area_quadrado(lado):
    return lado** 2

# Exemplo de uso
lado = float(input("Digite o valor do quadrado: "))
area = calcular_area_quadrado(lado)
dobro_area = area * 2
print("o dobro da área é ", dobro_area)