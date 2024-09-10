idade = int(input("Informe a idade: "))

if idade < 12:
    print(f"A idade {idade} é categoria criança")

elif 12 <= idade < 18:
    print(f"A idade {idade} é categoria adolescente")

elif 18 <= idade < 60:
    print(f"A idade {idade} é categoria adulto")

else: 
    print(f"A idade {idade} é categoria idoso")
