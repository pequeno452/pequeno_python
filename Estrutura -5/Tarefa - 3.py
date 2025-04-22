class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade <= 21:
            self.altura += 0.005  # 0.5 cm = 0.005 metros

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, cm):
        self.altura += cm / 100  # converte centímetros para metros

    def __str__(self):
        return (f'Nome: {self.nome}, Idade: {self.idade} anos, '
                f'Peso: {self.peso:.2f} kg, Altura: {self.altura:.2f} m')

p = Pessoa("Ana", 18, 55, 1.60)

print(p)
p.envelhecer()
p.engordar(2)
p.emagrecer(1)
p.crescer(2)

print(p)
