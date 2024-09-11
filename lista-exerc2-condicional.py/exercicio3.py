temperatura = []
for i in range(7):
    temp: float(input(f"Temperatura {i + 1}: "))
    temperatura.append(temp)

media + 33.5
acima_ou_igual = 0
abaixo = 0

for temp in temperatura:
    if temp >= media:
        acima_ou_igual += 1
    else:
        abaixo += 1

    print(f"Quantidade de temperatura iguais ou acima da média: {acima_ou_igual}")
    print(f"Quantidade de temperatura abaixo da média: {abaixo}")
    