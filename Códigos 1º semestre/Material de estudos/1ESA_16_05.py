def checa_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num

def soma_numeros(a,b):
    return a+b

def soma_elementos_range(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma

def soma_elementos(lista):
    soma = 0
    for elem in lista:
        soma += elem
    return soma

def media_lista(lista):
    soma = soma_elementos(lista)
    media = soma/len(lista)
    return media

def filtro_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares

def meu_in(lista_elementos,elemento):
    for i in range(len(lista_elementos)):
        if lista_elementos[i] == elemento:
            return True
    return False

def conta_vogais(palavra):
    vogais = ['a','e','i','o','u']
    qtd_vogais = 0
    for char in palavra:
        if char in vogais:#if meu_in(vogais,char):
            qtd_vogais += 1
    return qtd_vogais


def forca_opcao(msg,msg_erro,lista_opcoes):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        print(msg_erro)
        escolha = input(msg)
    return escolha

def acha_maior(numeros):
    indice_maior = 0
    maior = numeros[indice_maior]
    for i in range(len(numeros)):
        #print(f"Vou testar se {numeros[i]} > {maior}")
        if numeros[i] > maior:
            #print(f"Deu certo, então vou trocar {maior} por {numeros[i]}")
            maior = numeros[i]
            indice_maior = i
    return indice_maior

def busca_indice(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
precos = [10,20,1000000,50,5]
carros = ['up','uno','celta','gol','kombi']
erro ='\n'.join(carros)
escolha_carro = forca_opcao("Diga o carro: ",erro,carros)
local_carro = busca_indice(carros,escolha_carro)
print(f"O carro {carros[local_carro]} custa {precos[local_carro]}")
local_mais_caro = acha_maior(precos)
print(f"O carro mais caro é o {carros[local_mais_caro]}"
      f" e custa {precos[local_mais_caro]}")
vinhos = ['Sangue de Boi','Pérgola','Chapinha']
erro = '\n'.join(vinhos)
opcao = forca_opcao("Diga seu vinho favorito: ",
                    f"Somente:\n{erro}",vinhos)
opcoes = ['continuar','não']
erro = '\n'.join(opcoes)
continuar_ou_nao = forca_opcao("Voce deseja continuar ou nao?\n->",
                    f"Somente:\n{erro}",opcoes)
palavra = 'pastel'
qtd_vogais = conta_vogais(palavra)
print(f"A palavra {palavra} tem {qtd_vogais} vogais")

lista = [3,1,2,5,4,6,7]
soma_lista = soma_elementos(lista)
print(soma_lista)
par = filtro_pares(lista)
print(par)

lista = [54,7,23,546,234,56,23,56423,4,9,56,89]
buscar = 546
tá_ou_num_tá = meu_in(buscar,lista)
print(tá_ou_num_tá)
professores = ['Danilo','André','Allen','Lucas','Yan','Fabio','Celso']
prof = 'Rafael'
profs_tá_ou_num_tá = meu_in(professores,prof)
print(profs_tá_ou_num_tá)
print(meu_in([1,24,4,546,43],45))
num1 = 2
num2 = 3
soma = soma_numeros(num1,num2)
print(soma)
ano = checa_numero("Diga seu ano de nascimento: ")
print(ano)
qtd = checa_numero("Diga a qtd de garrafas: ")
print(qtd)

