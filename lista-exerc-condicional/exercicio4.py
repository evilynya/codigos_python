altura = float(input("Digite sua altura(em metros): "))
sexo = input("Digite seu sexo(M para masculino ou F para feminino): ")

if sexo == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é {peso_ideal}")

elif sexo == "M":
    peso_ideal = (72.7 * altura) - 58
    print(f"O seu peso ideal é {peso_ideal}")

else:
    print(f"Dados inválidos, digite novamente")

