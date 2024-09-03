salario = int(input("Qual eh o seu salario? "))
if salario <= 1903.98:
    print("Voce esta isento")

elif salario >= 1903.99 and salario <= 2826.65:
    print("Voce tem um desconto de 7,5%")
    novosalario = int
    novosalario = salario * 0.075
    salario = salario - novosalario
    print(f"Seu novo imposto de renda eh: {salario}")

elif salario >= 2826.66 and salario <= 3751.05:
    print("Voce tem um desconto de 15%")
    novosalario = int
    novosalario = salario * 0.15
    salario = salario - novosalario
    print(f"Seu novo imposto de renda eh: {salario}")

elif salario >= 3751.06 and salario <= 4664.68:
    print("Voce tem um desconto de 22,5%")
    novosalario = int
    novosalario = salario * 0.225
    salario = salario - novosalario
    print(f"Seu novo imposto de renda eh: {salario}")

else:
    print("Voce tem um desconto de 27,5%")
    novosalario = int
    novosalario = salario * 0.275
    salario = salario - novosalario
    print(f"Seu novo imposto de renda eh: {salario}")