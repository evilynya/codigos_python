animais = ['cachorro', 'gato', 'ovelha']
print(type(animais)) #exibindo o tipo de variável 

print(animais)

print('-'*50)
#estamos exibindo todos os itens da lista 'animais'
for elementos in animais:
    print(elementos)

#1 etapa: atualização de dados
print('-'*50)
animais[0] = "Coelho"
print(animais)

#2 etapa: inserir itens da lista 
print('-'*50)

#forma 1 - usando append 
animais.append("cavalo") #irá inserir um novo item no final da lista
print(animais)

#forma 2 - usando insert
animais.insert(1,"Pássaro")
print(animais)

# 3 etapa - excluir itens na lista 
print('-'*50)

#forma 1 - usando pop()
animais.pop() #irá excluir sempre o último item 
print(animais)

#forma 2 - usando pop() com índice 
animais.pop(0) #aqui iremos escolher qual índice de lista será excluído
print(animais)

#forma 3 - usando remove 
animais.remove("ovelha") #irá remover o item pelo seu conteudo
print(animais)