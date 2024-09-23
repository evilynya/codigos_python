soma_p = 0
quant_negativos = 0

for i in range(10):
    valor = int(input("Digite um valor inteiro: "))
    if valor > 0:
        soma_p += valor
    elif valor < 0:
        quant_negativos += 1

print("A soma dos números positivos é:", soma_p)
print("A quantidade de valores negativos é:", quant_negativos)


