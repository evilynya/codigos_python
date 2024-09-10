numero = int(input("Digite um número entre 0 e 100"))

if 0 <= numero <= 25:
    print(f"O número está entre a faixa de 0 a 25")

elif 26 <= numero <= 50:
    print(f"O número está entre a faixa de 26 a 50")

if 51 <= numero <= 75:
    print(f"O número está entre a faixa de 51 a 75")

if 76 <= numero <= 100:
    print(f"O número está entre a faixa de 76 a 100")

else:
    print(f"Número inválido, digite novamente: ")
   