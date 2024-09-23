temp = []
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho","Julho",
 "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

print("Digite a temperatura média de cada mês: ")

for item in range(12):
    temp = float(input(f"{meses[item]}: "))
    temp2.append(temp)

total_temperatura = 0

for temp in temp2:
    total_temperatura += temp
    media = total_temperatura /len(temp2)

print(f"A média anual das temperatuas é: {media:.2f}")
print("Temperaturas acima da média")
