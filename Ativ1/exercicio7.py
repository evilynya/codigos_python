distancia = float(input("Informe a distância em Km: "))
tempo = float(input("Informe o tempo em minutos: "))

velocidade = (distancia*1000)/(tempo*60)

print(f"A velocidade do projétil é {velocidade: .2f}")


