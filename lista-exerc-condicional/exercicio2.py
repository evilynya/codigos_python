salario = float(input("Informe seu salário: "))

if salario < 600:
    aumento = salario*0.30
    novo_salario = salario + aumento
    print(f"O seu salário foi reajustado para {novo_salario: .2f}")

else:
    print(f"Você não tem direito a um reajuste.")

