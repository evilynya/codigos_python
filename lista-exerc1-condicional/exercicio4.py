salario = float(input("Digite o salário do funcionário em R$: "))

if salario <= 1900:
    print(f"Funcionário isento de pagar imposto")

elif 1901 <= salario <= 2000:
    imposto = salario * 0.75

elif 2001 <= salario <= 3700:
    imposto = salario * 0.15

else:
    imposto = salario * 0.225

print(f"O salário do funcionário é {salario} e ele irá pagar {imposto} de imposto")