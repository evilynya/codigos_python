jogo = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

while True:
    computador = random.randint(1,3)
    usuario = int(input("Escolha: 1(pedra), 2(papel), 3(tesoura): "))

    print(f"Computador escolheu: {jogo[computador]}")
    print(f"Você escolheu: {jogo[usuario]}")

    if usuario == computador:
        resultado = "Empate"
    
    elif(usuario == 1 and computador ==3) or (usuario == 2 and computador == 1) or (usuario == 3 and computador ==2):
        resultado = "Você ganhou"
    
    else:
        resultado = "Você perdeu"
    
    print(resultado)