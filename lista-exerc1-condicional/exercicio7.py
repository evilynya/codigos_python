nota = float(input("Informe a nota final do aluno: "))
frequencia = float(input("Informe a frequência do aluno em %: "))

if nota >= 7 and frequencia >= 75:
    print(f"O aluno está aprovado")

else:
    print(f"O aluno está reprovado")