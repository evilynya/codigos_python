lista1 = []
lista2 = []
i = 0

while i < 5:
    valor1 = int(input(f"Digite o {i + 1}º valor da primeira lista: "))
    lista1.append(valor1)
    valor2 = int(input(f"Digite o {i + 1}º valor da segunda lista: "))
    lista2.append(valor2)
    i += 1
    
    lista_soma = []
    for i in range(len(lista1)):
        lista_soma.append(lista1[i] + lista2[i])
    
    print(f"Lista 1: {lista1}")
    print(f"Lista 2: {lista2}")
    print(f"Soma das listas: {lista_soma}")

