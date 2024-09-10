valor_i = int(input("Informe um valor inicial: "))
valor_f = int(input("Informe um valor final: "))

soma = 0 #inicializando a variável

for contador in range(valor_i,valor_f+1):
    soma = soma + contador

print(f"A soma do intervalo de {valor_i} até {valor_f} é {soma}")