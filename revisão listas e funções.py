#1 - Escreva uma função que recebe uma lista de números e retorna a soma de todos os elementos da lista:
'''def soma_lista():
    numeros = []
    quantidade = int(input("Quantos números você deseja somar? "))
    for _ in range(quantidade):
        numero = float(input("Digite um número: "))
        numeros.append(numero)
    return sum(numeros)
resultado = soma_lista()
print(f"A soma dos números na lista é: {resultado}")


#2 - Crie uma função que recebe uma lista de números e retorna o maior elemento da lista:
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

#3 - Faça uma função que recebe uma lista de strings e retorna uma nova lista contendo apenas as strings que começam com a letra 'a'
def comeca_com_a(palavra, prefixo):
    return palavra[:len(prefixo)] == prefixo

def filtrar_strings_iniciadas_com_a(lista):
    resultado = []
    for palavra in lista:
        if comeca_com_a(palavra, 'a') or comeca_com_a(palavra, 'A'):
            resultado.append(palavra)
    return resultado

minha_lista = ["amigo", "banana", "Abacaxi", "casa", "Arroz"]
strings_com_a = filtrar_strings_iniciadas_com_a(minha_lista)
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
def elementos_comuns(lista1, lista2):
    resultado = [palavra for palavra in lista1 if palavra in lista2]
    return resultado

lista1 = input("Digite as palavras da primeira lista (separadas por espaço): ").split()
lista2 = input("Digite as palavras da segunda lista (separadas por espaço): ").split()
resultado_in = elementos_comuns(lista1, lista2)
print("Elementos comuns usando 'in':", resultado_in)

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
def inverter_lista_reverse(lista):
    lista.reverse()
    return lista

numeros = [1, 2, 3, 4, 5]
lista_invertida = inverter_lista_reverse(numeros)
print(lista_invertida)

#9 - Faça uma função que recebe uma lista de strings e retorna uma nova lista contendo as mesmas strings, mas em ordem alfabética:
def ordenar_lista_strings(lista):
    return sorted(lista)

strings = ["banana", "maçã", "laranja", "abacaxi"]
lista_ordenada = ordenar_lista_strings(strings)
print(lista_ordenada)'''

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



