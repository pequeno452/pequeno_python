class Quadrado:
    def __init__(self, tamanho_lado):
        self.tamanho_lado = tamanho_lado

    def mudarLado(self, novo_tamanho):
        self.tamanho_lado = novo_tamanho

    def retornarLado(self):
        return self.tamanho_lado

    def calcularArea(self):
        return self.tamanho_lado ** 2

# Criando um quadrado com lado 5
meu_quadrado = Quadrado(5)

# Retornando o valor do lado
print("Lado:", meu_quadrado.retornarLado())  # Saída: 5

# Calculando a área
print("Área:", meu_quadrado.calcularArea())  # Saída: 25

# Mudando o valor do lado
meu_quadrado.mudarLado(8)

# Verificando as mudanças
print("Novo lado:", meu_quadrado.retornarLado())  # Saída: 8
print("Nova área:", meu_quadrado.calcularArea())  # Saída: 64
