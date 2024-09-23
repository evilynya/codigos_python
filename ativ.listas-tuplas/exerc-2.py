lista = []

while len(lista) < 10:
    while True:
        numero = int(input(f"Digite o {len(lista) + 1}º número inteiro: "))
        lista.append(numero)
        break
        print("Entrada inválida. Por favor, insira um número inteiro.")

    posicao = []
    for i in range(len(lista)):
        if lista[i] == 10:
            posicao.append(i)

    if posicao:
        print(f"O número 10 apareceu nas posições: {posicao}")
    else:
        print("O número 10 não foi encontrado na lista.")

