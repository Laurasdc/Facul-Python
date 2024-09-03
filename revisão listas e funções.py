#1 - Escreva uma função que recebe uma lista de números e retorna a soma de todos os elementos da lista:
'''def soma_elementos():
    soma = 0
    for num in numeros:
        soma += num
    return soma

def soma_elementos_indice(numeros):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]
        return soma

def forca_opcao(lista_opcoes, msg):
    possibilidades = '\n'.join(lista_opcoes)
    possibilidades = '\n' +possibilidades+'\n->'
    opcao = input(f"{msg+possibilidades}")
    while opcao not in lista_opcoes:
        print(f"Opção inválida! Somente essas:{possibilidades}")
        opcao = input(msg)
    return opcao

vinhos = ['Sangue de boi,' 'Pérgola', 'Chapinha', 'Cantinho do Vale']
escolha_vinho = forca_opcao("Qual vinho vc escolhe?\n", vinhos)
print(f"Você escolheu o {escolha_vinho}")

#2 - Crie uma função que recebe uma lista de números e retorna o maior elemento da lista:
#Meu jeito:
def verificacaonumero(msg):
    verificacao = input(msg)
    while not verificacao.isnumeric():
        verificacao = input(msg)
    return int(verificacao)

def maior_num(lista_num):
    maior = lista_num[0]
    for numero in lista_num:
        if numero > maior:
            maior = numero
    return maior

numeros = [verificacaonumero("Digite um número: ") for _ in range(5)]
print("Maior número da lista é:", maior_num(numeros))

#Jeito do professor:
def acha_maior_indice(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista))
        if lista[i] > maior:
            indice_maior = i
            maior = lista[indice_maior]
    return indice_maior
precos = [3,7,5,1]
carros = ['marea', 'celtinha brabo', 'gol', 'uno']
indice_mais_caro = achar_maior_indice(precos)
print(f"O carro mais caro é o {carros[indice_mais_caro]} e custa {precos[indice_mais_caro]}")

#3 - Faça uma função que recebe uma lista de strings e retorna uma nova lista contendo apenas as strings que começam com a letra 'a'
def comeca_com_a(lista):
    palavras_que_comecam_a = []
    for palavra in lista:
        if palavra[0] in ['a', 'A']:
            palavras_que_comecam_a.append(palavra)
    return palavras_que_comecam_a

minha_lista = ["amigo", "banana", "Abacaxi", "casa", "Arroz"]
strings_com_a = comeca_com_a(minha_lista)
print(strings_com_a)

# 4 - Escreva uma função que recebe uma lista de números e retorna uma nova lista contendo apenas os números pares 
def filtro_pares(lista):
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

def verificacaonumero(msg):
    verificacao = input(msg)
    while not verificacao.isnumeric():
        verificacao = input(msg)
    return int(verificacao)

numeros = [verificacaonumero("Digite um número: ") for _ in range(5)]
print("Os numeros pares sao: ", filtro_pares(numeros))

#5 - Crie uma função que recebe uma lista de palavras e retorna o número de letras em cada palavra como uma nova lista.
def filtro_letras(lista):
    lista_palavras = []
    for palavra in lista:
        lista_palavras.append(len(palavra))
    return lista_palavras

def obter_palavras_do_usuario():
    entrada = input("Digite as palavras separadas por vírgulas: ")
    palavras = entrada.split(",")
    return palavras

palavras_do_usuario = obter_palavras_do_usuario()
comprimentos = filtro_letras(palavras_do_usuario)
print("Comprimentos das palavras:", comprimentos)

#6 - Faça uma função que recebe duas listas e retorna uma lista contendo os elementos comuns entre as duas listas
#forma 1:
lista1 = ['a', 'b', 'c', 'd']
lista2 = ['f', 'a', 'g', 'k','c']
def interseccao(lista1,lista2):
    comuns = []
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2:
                comuns.append(elem1)
                break
    return comuns

#forma 2:
def interseccao(lista1,lista2):
    comuns = []
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            elem1 = lista1[i]
            elem2 = lista2[j]
            if elem1 == elem2:
                comuns.append(elem1)
                break
    return comuns

#forma3:
def interseccao(lista1,lista2):
    comuns = []
    for elem1 in lista1:
        if elem1 in lista2:
            comuns.append(elem1)
            break
    return comuns'''

#7 - Escreva uma função que recebe uma lista de números e retorna True se a lista estiver em ordem crescente e False caso contrário
def verifica_ordem_crescente(lista):
    for i in range(len(lista) - 1):
        if lista[i] >= lista[i + 1]:
            return False
    return True

numeros = [1, 3, 5, 7, 9]
resultado = verifica_ordem_crescente(numeros)
print(f"A lista está em ordem crescente? {resultado}")

#8 - Crie uma função que recebe uma lista de números e retorna uma nova lista com os elementos em ordem inversa
def inverter(lista):
    ultimo = len(lista) - 1
    for i in range(len(lista)//2):
        aux = lista[i]
        lista[i] = lista[ultimo - i]
        lista[ultimo - i] = aux
    return

numeros = [10,20,30,40,50,60,70,80,90]
inverter(numeros)
print(numeros)

#9 - Faça uma função que recebe uma lista de strings e retorna uma nova lista contendo as mesmas strings, mas em ordem alfabética:
def ordenar_lista_strings(lista):
    return sorted(lista)

strings = ["banana", "maçã", "laranja", "abacaxi"]
lista_ordenada = ordenar_lista_strings(strings)
print(lista_ordenada)

#10- Escreva uma função que recebe uma lista de números e retorna a média aritmética dos elementos da lista
def verificacaonumero(msg):
    verificacao = input(msg)
    while not verificacao.isnumeric():
        print("Entrada inválida. Por favor, digite um número válido.")
        verificacao = input(msg)
    return int(verificacao)

def calcular_media():
    lista_numeros = []
    while True:
        numeros = input("Digite um número (ou 'fim' para terminar): ")
        if numeros.lower() == 'fim':
            break
        numero = verificacaonumero("Digite um número: ")
        lista_numeros.append(numero)
    if len(lista_numeros) == 0:
        print("Nenhum número foi digitado.")
        return 0
    soma = sum(lista_numeros)
    media = soma / len(lista_numeros)
    return media

media = calcular_media()
print("A média dos números digitados é:", media)



