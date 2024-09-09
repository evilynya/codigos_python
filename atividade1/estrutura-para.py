'''
Essa estrutura de repetição é o mais comum e qualquer outra linguagem de programção

for (contador = 1; contador<=5; contador++){

}
'''
#1 EXEMPLO
for contador in range(1,5):
    print(contador)

print("-"*30)
#2 EXEMPLO 
for contador in range(1,11,2): # o 3 parâmetro irá aumentar o incremento dos valores que estão sendo exibidos 
    print(contador)

print("-"*30)
#3 EXEMPLO - Números do maior para o menor
for contador in range(10,0,-1):
    print(contador,end=" ") # o comand end, informa como o python irá mostrar o final de uma exibição, por padrão irá dar um enter(\n)

