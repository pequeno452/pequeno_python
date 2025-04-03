def calcular_salario(valor_hora, hora_trabalhadas):
    return valor_hora * hora_trabalhadas

# Exemplo de uso
valor_hora = float(input("Digite quando você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario = calcular_salario((valor_hora, horas_trabalhadas))
print(f"O total do seu salá10rio no mês é R$ {salario:.2f}.")