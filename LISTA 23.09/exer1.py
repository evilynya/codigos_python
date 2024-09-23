velocidade = float(input("Qual a velocidade do veículo registrada?"))
limite = float(input("Qual foi o limite de velocidade da via?"))

if velocidade <= limite:
    print(f"Sem multa")

else:
    excesso = velocidade - limite 
    if excesso <= 10:
        print(f"Multa: R$50,00")
    
    elif excesso <=20:
        print(f"Multa: R$100,00")
    
    else:
        print(f"Multa: R$200,00")