while True:
    nome = input("Digite um nome (nome e sobrenome): ")
    if len(nome) > 15:
        print("Nome aceito!")
        break
    else:
        print("O nome deve ter mais de 15 letras. Tente novamente.")


#função len: aplicada a um string, retorna o número de caracteres no string (o comprimento).
