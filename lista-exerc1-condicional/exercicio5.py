hora_trabalho = float(input("Informe a quantidade de horas trabalhadas: "))
salario_hora = float(input("Informe o valor por hora trabalhada em R$: "))

if hora_trabalho > 40:
    bonus_salario = salario_hora * 1.5
    print(f"O pagamento do funcinário será de R$ {bonus_salario:.2f} por hora extra")

else:
    print(f"Não houve alteração no valor do salário")

