# Solicita as quatro notas bimestrais ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota:"))
nota3= float(input("Digite a terceira nota:"))
nota4= float(input("Digite a quarta nota: "))

# Calcula a média
media = (nota1 + nota2 + nota3 + nota4) / 4

# Exibe o resultado
print(f"A média das notas é: {media: .2f}")


