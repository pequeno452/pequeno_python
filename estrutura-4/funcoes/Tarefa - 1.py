def imprimir_padrao(n):
    for i in range(1, n + 1):
        print((str(i) + '') * i)
# Exemplo de uso:
n = int(input("Digite o valor de n: "))
imprimir_padrao(n)