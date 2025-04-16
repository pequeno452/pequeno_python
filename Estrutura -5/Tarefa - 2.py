class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def mudar_valor_lado(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def retornar_valor_lado(self):
        return self.tamanho

    def calcular_area(self):
        return self.tamanho ** 2

# Criando um quadrado com lado 4
q = Quadrado(4)

# Mostrando o valor do lado
print("Lado:", q.retornar_valor_lado())

# Calculando a área
print("Área:", q.calcular_area())

# Mudando o valor do lado para 6
q.mudar_valor_lado(6)

# Mostrando novamente
print("Novo lado:", q.retornar_valor_lado())
print("Nova área:", q.calcular_area())
