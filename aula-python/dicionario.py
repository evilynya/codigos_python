pessoa = ["Maria", "48", "Rua 10"]
print(pessoa)

#iniciando com dicionário 
dados_pessoais = {
    'Nome' : 'João',
    'Idade':23, 
    'Endereço': 'Avenida 4'
}

print(dados_pessoais)

#exibindo as chaves utilizando o comando keys()
print(dados_pessoais.keys())

#exibindo os valores utilizando o comando values() 
print(dados_pessoais.values())

#exibindo tanto a chave quanto o valor com o comando items()
print(dados_pessoais.items())

#exibindo o dicionário 
for chave, valor in dados_pessoais.items():
    print(f"{chave} : {valor}")

#realizando operações com dicionário
#adicionando dados do dicionário 
#forma 1 
dados_pessoais["Peso"] = 68
print(dados_pessoais)

#forma 2 - usando o comando update()
dados_pessoais.update({"Profissão" : "Engenheiro"})
print(dados_pessoais)

#remover dados do dicionário
#forma 1 - usando pop
dados_pessoais.pop("Endereço") #preciso passar a chave para poder excluir o registro 
print(dados_pessoais)

#forma 2 - usando del()
del(dados_pessoais["Endereço"])
print(dados_pessoais)