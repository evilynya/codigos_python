lista = []
i = 0
  
while i < 7:
    valor = int(input(f"Digite o {i + 1}º valor: "))
    lista.append(valor)
    i += 1
    quant_impar = 0
    for numero in lista:
        if numero % 2 != 0:
            quant_impar += 1
    
    print(f"A quantidade de números ímpares é: {quant_impar}")

