# Solicita ao usuario que digite uma letra
letra = input("Digite o sexo (f ou m): ").lower()


# Verificaa letra digitada e exibi o resultado
if letra == "f":
    print("Feminino")
elif letra =="m":
    print("Masculino")
else:
    print("Sexo inválido")
