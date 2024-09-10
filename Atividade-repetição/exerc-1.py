soma = 0

for contador in range(50,71):
    if contador % 2 == 0:
        soma = soma + contador 
        total_pares = total_pares + 1

print("A soma de todos os pares é {soma} e a média é {soma / total_pares }")