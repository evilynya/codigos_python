while True:
    login1 = input("Informe seu login: ")
    senha1 = input("Informe sua senha: ")

    if login1 != senha1 :
        while True:
            login2 = input("Informe login da pessoa 2: ")
            senha2 = input("Informe senha da pessoa 2: ")

            if login2 != login1 and senha2 != senha1:
                break
            else:
                print("O login e a senha iguais ou loguin1 é igual login2. Tente novamente.")
        
        break
    else:
        print("loguin1 e senha1 são iguais")
            

        


