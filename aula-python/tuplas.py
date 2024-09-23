# trabalhando com tuplas 

objetos = ('Lápis', 'Borracha', 'Caderno')

print(type(objetos)) #a função type() irá exibir o tipo de variável 'objetos', nesse caso irá aparecer 'tuple'

print(objetos)
print(objetos[1]) #estamosz exibindo apenas um item, que está na posição 1 

#exibindo todos os dados da tupla 
print('-'*50)

for item in range(0,3):
    print(objetos[item])

#exibindo todos os dados sem a função range 
print('-'*50)

for item in objetos:
    print(item)

#tentando mudar o conteúdo da tupla 
print('-'*50)

objetos[0] = "caneta"  #irá ocorrer um erro pois os valores de uma tupla são imutáveis
print(objetos)
