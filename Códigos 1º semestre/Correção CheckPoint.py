'''
Gabarito
print("Seja bem vindo à Vinheria Agnello!!!")
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade < 18:
    print("Que feio!!!!!!!! Exclamation marks!!!")
else:
    endereco = input("Diga seu endereço: ")
    vinho1 = 'Chapinha'
    vinho2 = 'Sangue de Boi'
    vinho3 = 'Levanta Defunto'
    preco1 = 10
    preco2 = 20
    preco3 = 30
    frete = 10
    print(f"Essas são as nossas opções de vinhos:\n{vinho1}:R${preco1:.2f}"
          f"\n{vinho2}:R${preco2:.2f}\n{vinho3}:R${preco3:.2f}")
    escolha = input("Diga o nome do vinho de sua preferência: ")
    if escolha == vinho1:
        preco = preco1
    elif escolha == vinho2:
        preco = preco2
    else:
        preco = preco3
    qtd = int(input(f"Quantas garrafas de {escolha} você vai levar?\n->"))
    valor = qtd*preco
    if valor < 100:
        valor += frete
    else:
        print("Frete grátis!!!!")
    print(f"Voce gastou R${valor:.2f} em {qtd} garrafas de {escolha} que serão entregues"
          f"em {endereco}")

1- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.

while True:
    num = input("Diga um valor entre 0 e 10:\n->")
    if num.isnumeric():
        print(type(num),num)
        num = int(num)
        print(type(num),num)
        if num > 0 and num < 10:
            break
        else:
            print("Você não digitou algo entre 0 e 10")
    else:
        print("Você não digitou um número!")

num = input("Diga um numero: ")
while not num.isnumeric():
    num = input("Diga um numero: ")

while True:
    num = input("Diga um numero: ")
    if num.isnumeric():
        break
2- Faça um programa que leia e valide as seguintes informações:
a. Nome: maior que 3 caracteres;
b. Idade: entre 0 e 150;
c. Salário: maior que zero;
d. Sexo: 'f' ou 'm';
e. Estado Civil: 's', 'c', 'v', 'd';

nome = input("Diga seu nome:\n->")
while len(nome) < 3:
    print("O nome deve ter no mínimo 3 caracteres!")
    nome = input("Diga seu nome:\n->")

while True:
    nome = input("Diga seu nome:\n->")
    if len(nome) >= 3:
        break
    print("O nome deve ter no mínimo 3 caracteres!")

while True:
    idade = input("Diga um valor (idade) entre 0 e 150:\n->")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        print("Você não digitou algo entre 0 e 150")
    else:
        print("Você não digitou um número!")

while True:
    salario = input("Diga seu salario:\n->")
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
            break

sx = input("Diga f ou m:\n->")
while sx != 'f' and sx != 'm':
    sx = input("Diga f ou m:\n->")

sx = input("Diga f ou m:\n->")
while not (sx == 'f' or sx == 'm'):
    sx = input("Diga f ou m:\n->")
ec = input("Diga seu estado civil (s,c,v,d):\n->")
while not (ec == 's' or ec == 'c' or ec == 'v' or ec == 'd'):
    ec = input("Diga seu estado civil (s,c,v,d):\n->")
print(f"Seu nome é {nome}, sua idade é {idade}, "
      f"seu salário é {salario}\n você é {sx} e seu estado civil é {ec}")
a = 80
b = 200
anos = 0
while a < b:
    #a = a + 0.03*a
    a *= 1.03
    b *= 1.015
    anos += 1
print(anos)

soma = 0
qtd = 0
while qtd < 5:
    num = input(f"Diga o {qtd+1}º numero\n->")
    while not num.isnumeric():
        print("Voce nao digitou um numero")
        num = input(f"Diga o {qtd+1}º numero\n->")
    num = int(num)
    soma += num
    qtd+=1
media = soma/qtd

a = input("Diga um numero: ")
while not a.isnumeric():
    a = input("Diga um numero: ")
a = int(a)
b = input("Diga um numero: ")
while not b.isnumeric():
    b = input("Diga um numero: ")
b = int(b)

if b < a:
    aux = a
    a = b
    b = aux

while a<=b:
    print(a)
    a += 1

senha = input("Diga sua senha\n->")
usuario = input("Diga seu usuario\n->")
while usuario == senha:
    print("N pode ser igual")
    usuario = input("Diga seu usuario\n->")
    senha = input("Diga sua senha\n->")

num = 1
while num <=10:
    print(f"Tabuada do {num}")
    print(i)
    i = 1
    while True:
        print(f"{num}*{i} = {num*i}")
        i+=1
        if i == 10:
        break
    num += 1
    print()

a = 1
b = 1
print(a,end = ' ')
print(b,end = ' ')
qtd = 200
i = 2
while i < qtd:
    c = a + b
    print(c/b)
    a = b
    b = c
    i += 1

qtd = 0
pares = 0
impares = 0
while qtd < 10:
    num = input(f"Diga o {qtd+1}º numero: ")
    if not num.isnumeric():
        num = input(f"Diga o {qtd+1}º numero: ")
        continue
    num = int(num)
    if num % 2 ==0:
        pares += 1
        qtd += 1
        continue
    impares += 1
    qtd += 1
impares = qtd - pares

num = input("Diga um numero: ")
while not num.isnumeric():
    num = input("Diga um numero: ")
num = int(num)
fatorial = num
fatorial_string = f"{num}! = {num}"
while num > 1:
    num -= 1
    fatorial *= num
    fatorial_string += f"*{num}"
fatorial_string += f" = {fatorial}"
print(fatorial_string)
'''
i = 2
num = 37
while i < num**0.5:
    print(f"{num}%{i} = {num%i}")
    if num%i == 0:
        print(f"{num} não é primo!")
        break
    i += 1
if i >= num**0.5:
    print("é primo")









