salario = float(input("Digite o salário atual: R$"))
anos = int(input("Informe o número de anos de serviços: "))

if anos <= 5:
    bonus = salario * 0.05

elif anos <= 10:
    bonus = salario * 0.10

else:
    bonus = salario * 0.15

bonus = salario + anos 
salario_fim = salario + bonus

print(f"Bônus: R$ {bonus:.2f}")
print(f"Salário final com bônus: R$ {salario_fim: .2f}")