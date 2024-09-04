#1 a) - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. 
'''while True:
    nota = input("Diga sua nota: ")
    if nota.isnumeric():
        nota = int(nota)
        if nota > 0 and nota <= 10:
                break
        else:
            print("Você não digitou um número entre 0 e 10")
    else:
        print("Você não digitou um número!")

#1 b) - Faça um programa que leia e valide as seguintes informações: a. Nome: maior que 3 caracteres; b. Idade: entre 0 e 150; c. Salário: maior que zero; d. Sexo: 'f' ou 'm'; e. Estado Civil: 's', 'c', 'v', 'd';
nome = input("Digite o seu nome:")
while len(nome) < 3:
    print("O nome deve ter pelo menos 3 letras")
    nome = input("Qual é o seu nome")

#1 c)
while True:
    idade = input("Digite a sua idade? ")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade <= 150:
            print("Você está com a idade correta")
            break
        else:
            print("Você não tem uma idade válida")
    else:
        print("Não é um número!")

#1 d)
sexo = input("Qual é o seu sexo? f ou m ")
while sexo != 'f' or sexo != 'm':
    print("Digite f ou m. Qual é o seu sexo? ")

#1 e)
estado_civil = input("Qual é o seu estado civil: 's', 'c', 'v', 'd'")
while not (estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd'):
    estado_civil = input("Qual é o seu estado civil: 's', 'c', 'v', 'd'")

#3 Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
pais_a = 80000
pais_b = 200000
anos = 0
while pais_a <= pais_b:
    pais_a *= 1.03
    pais_b *= 1.15
    anos += 1
print(f"Vai ser preciso {anos} anos")

#4 - Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
qtd_num = 0
while qtd_num < 5:
    num = input(f"Digite o {qtd_num+1} numero:\n")
    while not num.isnumeric():
        num = input(f"Digite o {qtd_num+1} numero:\n")
    num = int(num)
    soma += num
    qtd_num += 1
media = soma/qtd_num
print(f"A soma eh = {soma} e a media eh {media}")

#5 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
a = input("Diga um número: ")
while not a.isnumeric():
    a = input("Diga um número: ")
a = int(a)

b =input("Diga outro número: ")
while not b.isnumeric():
    b = input("Diga outro número: ")
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a <= b:
    print(a)
    a += 1

#6 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
nome_usuario = input("Digite o seu nome: ")
senha = input("Digite uma senha: ")
while senha == nome_usuario:
    print("O nome de usuario e a senha nao podem ser as mesmas")
    nome_usuario = input("Digite o seu nome:\n")
    senha = input("Digite uma senha:\n")

#7 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
num = 1
while num <= 10:
    print(f"Tabuada do {num}: ")
    mult = 1
    while mult <= 10:
        print(f"{mult}*{num} = {num*mult}")
        mult += 1
    num += 1
    print()

#8 - A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
a = 1
b = 1
qtd = 10
i = 0
while i < qtd:
    c = a + b
    print(c, end = '')
    a = b
    b = c
    i += 1

#9 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.
i = 0
qtd_pares = 0
while i < 10:
    num = input(f"Digite o {i+1} numero: ")
    while not num.isnumeric():
        num = input(f"Digite o {i+1} numero: ")
        continue
    num = int(num)
    if num % 2 == 0:
        qtd_pares += 1
    i += 1
impares = i - qtd_pares
print(f"Vc digitou {qtd_pares} pares e {impares} impares")

#10 - Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
num = input("Diga um número: ")
while not num.isnumeric():
    num = input("Diga um número: ")
num = int(num)
fatorial = num
fatorial_string = f"{num}! = {num}"
while num > 1:
    num -= 1
    fatorial *= num
    fatorial_string += f"*{num}"
fatorial_string += f" = {fatorial}"
print(fatorial_string)'''

