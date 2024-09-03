'''
vinho1 = 'Chapinha'
vinho2 = 'Sangue de Boi'
vinho3 = 'Pérgola'
preco1 = 10
preco2 = 20
preco3 = 30
frete = 10
qtd1 = 0
qtd2 = 0
qtd3 = 0
valor_total = 0
opcoes = f"{vinho1}-{preco1}\n{vinho2}-{preco2}\n{vinho3}-{preco3}"
print("Seja bem vindo à Vinheria Agnello!!!!!!")
ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    print("Deve ser um número!")
    ano = input("Diga seu ano de nascimento: ")
ano = int(ano)
idade = 2024 - ano
if idade < 18:
    print("Vo conta p sua mãe!!!!")
else:
    endereco = input("Diga seu endereco: ")
    while True:
        print(f"Essas são as nossas opções de vinhos:\n{opcoes}")
        escolha = input("Qual lhe interessou?\n->")
        while not (escolha == vinho1 or escolha == vinho2 or escolha == vinho3):
            print(f"Opção Inválida!!!! Somente essas:\n{opcoes}")
            escolha = input("Qual lhe interessou?\n->")
        qtd = input(f"Quantas garrafas de {escolha} vc quer?\n->")
        while not qtd.isnumeric():
            print("Deve ser um numero!")
            qtd = input(f"Quantas garrafas de {escolha} vc quer?\n->")
        qtd = int(qtd)
        if escolha == vinho1:
            valor_atual = preco1*qtd
            qtd1 += qtd
        elif escolha == vinho2:
            valor_atual = preco2*qtd
            qtd2 += qtd
        else:
            valor_atual = preco3*qtd
            qtd3 += qtd
        valor_total += valor_atual
        proceder = input("Vc quer comprar mais vinhos? (s/n)\n->")
        while proceder != 's' and proceder != 'n':
            print("Opção inválida!")
            proceder = input("Vc quer comprar mais vinhos? (s/n)\n->")
        if proceder == 'n':
            break
    if valor_total > 500:
        frete = 0
        print("Frete grátis!")
    valor_total += frete
    print(f"Voce gastou R${valor_total:.2f} em"
          f"\n{qtd1} de {vinho1}\n{qtd2} de {vinho2}"
          f"\n{qtd3} de {vinho3}\n e seu pedido será entregue em"
          f"{endereco}")

for char in 'danilo':
    print(char,end = ' ')
    char = 1
    print(char)

#range(10) => range(0,10,1)
for i in range(1,10,2):#start,end,passo
    print(i)

for i in range(10,1,-2):#start,end,passo
    print(i)
senha_cadastrada = '1234'
for i in range(3):
    senha = input("Diga sua senha: ")
    if senha == senha_cadastrada:
        print("Acesso liberado!")
        break
    print(f"Você é hacker??? Vc tem {2-i} tentativas restantes")

if senha != senha_cadastrada:
    print("Acesso Negado hacker")

#some todos os numeros de 1 a 100 usando um for
#peça 10 numeros para o usuario e conte a qtd de pares e impares
#peça 10 numeros para o usuario e faça a soma e a media
#faça a tabuada de todos os numeros de 1 a 10
#encontre a qtd de vogais numa string que o usuario digitou

soma = 0
for i in range(1,101):
    soma += i

par = 0
for i in range(1,11):
    num = input("Diga um numero: ")
    while not num.isnumeric():
        num = input("Diga um numero: ")
    num = int(num)
    if num % 2 == 0:
       par += 1
print(f"{par} pares e {i-par} impares")


soma = 0
for i in range(1,11):
    num = input("Diga um numero: ")
    while not num.isnumeric():
        num = input("Diga um numero: ")
    num = int(num)
    soma += num
print(f"A soma é {soma} e a média é {soma/i}")

for i in range(1,11):
    print(f"Tabuada do {i}:")
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")
    print()
i = 1
while i <= 10:
    print(f"Tabuada do {i}:")
    j = 1
    while j <= 10:
        print(f"{i}*{j}={i*j}")
        j += 1
    i+=1
    print()

vogais = 0
palavra = input("Diga uma palavra: ")
for char in palavra:
    if char == 'a' or char == 'e' or char == 'i' or \
        char == 'o' or char == 'u':
        vogais += 1
print(f"Há {vogais} vogais e {len(palavra) - vogais} consoantes"
      f" na sua palavra")
lista = [1,True,3.2,'danilo',['dfkj',False]]
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")

lista = [False,True,3.2,'danilo',['dfkj',False]]
#print(type(lista))
#print(lista[0])
#print(lista[1])
#print(lista[2])
#print(lista[3])
#print(lista[4])
#print(lista[5])
lista[4] = True
#print(lista)

for elem in lista:
    print(elem,end = ' ')
    elem = 1
    print(elem)
print(lista)

for i in range(len(lista)):
    lista[i] = 1
print(lista)

profs = ['Andre','Lucas Silva','Yan','Danilo','Allen',"Fabio",'Celso']
materias = ['Storytelling','Front','Edge','Python','SW','Javascript','Caluclo']
for i in range(len(profs)):
    print(f"O prof {profs[i]} dá {materias[i]}")
achou = False
for i in range(len(profs)):
    if profs[i] == "Danilo":
        achou = True
        print(f"Achei o {profs[i]} no índice {i}")
        break
if not achou:
    print('Não ta na lista')
'''
profs1 = ['Patricia','Ana','Danilo','Thiago',"Jones",'Yan']
profs2 = ['Andre','Lucas Silva','Yan','Danilo','Allen',"Fabio",'Celso']

for prof1 in profs1:
    for prof2 in profs2:
        if prof1 == prof2:
            print(f"O {prof1} dá aula nas duas turmas")


