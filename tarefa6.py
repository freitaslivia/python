n = input("Horas trabalhadas no mês: ")
v = input("Valor da hora trabalhada:")
p = input("Percentual de desconto: ")

horas_trabalhadas = int(n)
valor_da_hora = float(v)
percentual_de_desconto = float(p)

if horas_trabalhadas <= 0 or valor_da_hora <= 0 or percentual_de_desconto < 0:
    print("Os valores informados são inválidos.")
elif percentual_de_desconto > 100:
    print("O percentual de desconto não pode ser maior que 100%.")
else:
    salario_bruto = horas_trabalhadas * valor_da_hora
    total_desconto = (percentual_de_desconto * salario_bruto) / 100
    salario_liquido = salario_bruto - total_desconto
    print("Salário Bruto: R$ %.2f" % salario_bruto)
    print("Total de Desconto: R$ %.2f" % total_desconto)
    print("Salário Líquido: R$ %.2f" % salario_liquido)