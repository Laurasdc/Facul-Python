#1
'''while True:
    num = input("Diga um numero entre 1 e 10: ")
    if num.isnumeric():
        num = int(num)
        if num > 0 and num <= 10:
            print(f"Vc digitou o numero {num}. Tmj mlk")
            break
        else:
            print("Vc n digitou um numero valido. Digite novamente: ")
    else:
        print("Vc nem digitou um numero cara. Digite novamente: ")
'''

#2
'''a)
nome = input("Qual eh o seu nome")
while len(nome) < 3:
    print("Deve ter no mínimo 3 caracteres")
    nome = input("Qual eh o seu nome: ")'''

'''b)
while True:
    idade = input("Qual eh a sua idade? : ")
    if idade.isnumeric():
        idade = int(idade)
        if idade >= 0 and idade <= 150:
            print(f"Vc tem {idade} anos. Tmj mlk")
            break
        else:
            print("Vc ou eh velho demais ou n nasceu ainda. Digite a sua idade novamente: ")
    else:
        print("Vc nem digitou um numero cara. Digite novamente: ")'''

'''c)
while True:
    salario = input("Qual eh o seu salario? ")
    if salario.isnumeric():
        salario = int(salario)
        if salario > 0:
            print(f"O seu salario eh: {salario}")
            break
        else:
            print("Vc n digitou um valor maior que 0. Digite novamente: ")
    else:
        print("Vc nem digitou um numero vei. Digite dnv: ")'''

'''d)
sexo = input("Qual é o seu gênero: f ou m? ")
while not (sexo == 'f' or sexo == 'm'):
    sexo = input("Qual é o seu gênero: f ou m? ")
print("Ola femea ou macho.")'''

'''e)
ec = input("Diga seu estado civil (s,c,v,d): ")
while ec != 's' and ec != 'c' and ec != 'v' and ec != 'd':
    ec = input("Diga seu estado civil (s,c,v,d): ")'''

#3
#Populacao inicial
'''populacao_a = 80000
populacao_b= 200000

#taxa de crescimento anual
taxa_a = 0.03  # 3%
taxa_b = 0.015  # 1.5%

# Contador de anos
anos = 0

# Loop while para calcular o número de anos necessários
while populacao_a < populacao_b:
    # Calcula o crescimento anual das populações
    populacao_a += populacao_a * taxa_a
    populacao_b += populacao_b * taxa_b
    # Incrementa o contador de anos
    anos += 1
    
# Imprime o resultado
print(f"Serão necessários {anos} anos para que a população do país A ultrapasse ou se iguale à população do país B.")'''

#4
'''soma = 0
qtd = 0
while qtd < 5:
    numero = input(f"Diga o {qtd+1}º numero\n--> ")
    while not numero.isnumeric():
       numero = input(f"Diga o {qtd+1}º numero\n--> ")
    numero = int(numero)
    soma += numero
    qtd+=1
media = soma/qtd
print(f"A soma é = {soma} e a média é = {media} ")'''

#5
'''# Solicita ao usuário que digite um número e o converte em um inteiro.
a = int(input("Diga um numero: "))
# Solicita ao usuário que digite outro número e o converte em um inteiro.
b = int(input("Diga outro numero: "))

# Se o primeiro número (a) for maior que o segundo (b), eles trocam de valores.
if a > b:
    aux = a
    a = b
    b = aux

# Enquanto 'a' for menor que 'b', imprime os números de 'a' até 'b - 1'.
while a < b:
    print(a, end=' ')
    a += 1

# Se 'b' for menor que 'a', imprime os números de 'b' até 'a - 1'.
while b < a:
    print(b)
    b += 1
'''

#6
'''senha = input("Insira a sua senha: ")
usuario = input("Diga seu nome de usuario: ")
while senha == usuario:
    print("A senha e o nome de usuario n podem ser iguais. ")
    senha = input("Insira a sua senha: ")
    usuario = input("Diga seu nome de usuario: ")
print(f"Liberado o acesso, {usuario}.")'''

#7
'''Solicita ao usuário que insira o número para o qual deseja gerar a tabuada
numero = int(input("Digite o número para gerar a tabuada (1 a 10): "))

# Verifica se o número está no intervalo correto
if 1 <= numero <= 10:
    i = 1
    print(f"Tabuada do {numero}")
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1
else:
    print("Número inválido. Por favor, digite um número entre 1 e 10.")'''

#8
'''a = 1
b = 1
qtd = 10
i = 0
while i < qtd:
    c = a + b
    print(c, end = ' ')
    a = b
    b = c
    i += 1'''

#9
'''# Inicializa contadores para números pares e ímpares
cont_pares = 0
cont_impares = 0

# Inicializa o contador de números
contador = 0

# Loop para pedir 10 números
while contador < 10:
    numero = int(input(f"Digite o número {contador + 1}/10: "))

    # Verifica se o número é par ou ímpar e atualiza os contadores
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

    # Incrementa o contador de números
    contador += 1

# Mostra os resultados
print(f"Quantidade de números pares: {cont_pares}")
print(f"Quantidade de números ímpares: {cont_impares}")'''

#10
'''num = input("Diga um número: ")
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

#11
'''# Solicita ao usuário que digite um número
num = input("Digite um número: ")

# Verifica se a entrada é numérica
while not num.isnumeric():
    num = input("Digite um número: ")

# Converte a entrada para um número inteiro
num = int(num)

# Verifica se o número é primo
if num > 1:
    # Assume que o número é primo até que se prove o contrário
    eh_primo = True

    # Verifica se há algum divisor do número entre 2 e num - 1
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1

    # Imprime o resultado
    if eh_primo:
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")
else:
    print(f"{num} não é um número primo.")'''

#12
'''# Solicita ao usuário o número de notas
quantidade_notas = int(input("Quantas notas você deseja calcular a média? "))

# Inicializa a soma das notas e o contador
soma_notas = 0
contador = 0

# Loop para coletar as notas e calcular a soma
while contador < quantidade_notas:
    nota = float(input(f"Digite a nota {contador + 1}: "))
    soma_notas += nota
    contador += 1

# Calcula a média aritmética
media = soma_notas / quantidade_notas

# Mostra a média
print(f"A média aritmética das notas é: {media:.2f}")'''

#13
'''final = 2000
salario = 1000
taxa = 0.015
partida = 1995
while partida < final:
    salario *= (1+taxa)
    taxa *= 2
    partida += 1
print(f"{salario:.2f}")'''

#14
'''primeiro = 0
segundo = 0
terceiro = 0
quarto = 0
while True:
    num = int(input("Diga um numero:"))
    if num < 0:
        break
    if num <= 25:
        primeiro += 1
    elif num <= 50:
        segundo += 1
    elif num <= 75:
        terceiro += 1
    elif num <= 100:
        quarto += 1'''


#15
joao = 0
jose = 0
joana = 0
jorel = 0
nulo = 0
branco = 0
i = 0
while True:
    num = input("Diga seu voto:\n 1 - João\n2 - José \n3 - Jorel\n4 - Joana "
                "\n5 - Nulo\n 6 - Branco\n 0 - sair ")
    while num != '0' and num != '1' and num != '2' and num != '3' \
            and num != '4' and num != '5' and num != '6':
        num = input("Diga seu voto:\n 1 - João\n2 - José \n3 - Jorel\n4 - Joana "
                    "\n5 - Nulo\n 6 - Branco\n 0 - sair ")
    if num == '0':
        break
    elif num == '1':
        joao +=1
    elif num == '2':
        jose +=1
    elif num == '3':
        jorel +=1
    elif num == '4':
        joana +=1
    elif num == '5':
        nulo +=1
    elif num == '6':
        branco +=1
    i += 1
print(f"João : {joao}\nJosé : {jose}\nJorel : {jorel}\nJoana : {joana}"
      f"\nNulos : {nulo/i:.2f}%\nBrancos : {branco/i:.2f}%")


