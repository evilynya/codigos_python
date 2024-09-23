contador_impar = 0

while True:
    valor = int(input("Digite um valor numérico (digite 0 para parar): "))
    if valor == 0:
        break
    elif valor % 2 != 0:
        contador_impar += 1

print(f"Os números ímpares são: {contador_impar}")

