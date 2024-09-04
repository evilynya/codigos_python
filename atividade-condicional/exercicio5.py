carro = int(input("Informe o tipo de carro(1,2,3): "))
percurso = float(input("Digite a distância a percorrer em Km: "))

if carro == 1:
    consumo = percurso/8 
    print(f"A previsão de consumo é de {consumo: .2f} litros por Km")

elif carro == 2:
    consumo = percurso/9
    print(f"A previsão de consumo é de {consumo: .2f} litros por Km")

elif carro == 3:
    consumo = percurso/12
    print(f"A previsão de consumo é de {consumo: .2f} litros por Km") 

else:
    print(f"Alguma informação está incorreta, digite novamente")
    
