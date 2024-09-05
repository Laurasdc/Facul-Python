# 1 – Faça uma função que printa uma matriz da maneira convencional, ou seja, uma linha abaixo da outra:
'''def imprimir_matriz(matriz):
  for i in matriz:
    for j in i:
      print(j, end=" ")
    print()

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

imprimir_matriz(matriz)'''

# 2 - Faça uma função que recebe de parâmetros as dimensões (linhas e colunas) e retorna uma matriz preenchida de zeros com essas dimensões:
'''def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

matriz = cria_matriz(3,3)
mostra_matriz(matriz)'''

# 3 - Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da diagonal para 1:
'''def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return


matriz = cria_matriz(5,5)
diagonal(matriz)
mostra_matriz(matriz)'''

# 4 - Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da “contra-diagonal” para 1:
'''def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def contra_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1 - i] = 1
    return

matriz = cria_matriz(5,5)
contra_diagonal(matriz)
mostra_matriz(matriz)   '''     

# 5 - Faça uma função que recebe uma matriz quadrada e altera todos os elementos acima/abaixo da diagonal para 1:
'''def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

#Abaixo da diagonal:
def triognal_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return''

matriz = cria_matriz(5, 5)
triognal_inferior(matriz)
mostra_matriz(matriz)

#Acima da diagonal:
def triognal_superior(matriz):
    for j in range(len(matriz)):
        for i in range(j):
            matriz[i][j] = 1
    return

matriz = cria_matriz(5, 5)
triognal_superior(matriz)
mostra_matriz(matriz)'''

# 6 - Faça uma função que recebe uma matriz quadrada e retorne sua transposta: 
'''def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

    
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

    
def triognal_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return

    
def transporta(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return

    
matriz = cria_matriz(10,10)
triognal_inferior(matriz)
mostra_matriz(matriz)'''

# 8 - Faça um código que transforma uma matriz quadrada 8x8 em um tabuleiro de xadrez:
'''def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

    
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz


xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[i])):
        if i % 2 == 0:
            if j % 2 == 0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
        else:
            if j % 2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1

mostra_matriz(xadrez)'''

# 10 - Devido ao covid as cadeiras de cinema tem que ser utilizadas com um espaçamento de uma cadeira desocupada tanto na frente quanto atrás e dos lados. Represente está situação com uma matriz 50x50 em que cada local (i,j) tem nele a palavra “vaga” ou ocupada:
'''def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append("vaga")
        matriz.append(linha)
    return matriz


def mostra_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))
    return


def ocupa_cadeiras(matriz,espacamento):
    n = len(matriz)
    for i in range(0, n, espacamento+1):  
        for j in range(0, n, espacamento+1):
            matriz[i][j] = "ocupada"


matriz_cinema = cria_matriz(50, 50)
ocupa_cadeiras(matriz_cinema, espacamento=1)
mostra_matriz(matriz_cinema)'''

#Matrizes com caso do vinho:
def forca_num(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('Digite um numero. \n')               
    return num

def somarLista(lista):
    soma = 0
    for elemento in lista:
        soma += elemento
    return soma

def forcaEscolha(lista, msg):
    erro = ', '.join(lista)
    while True:
        elemento = input(msg)
        if elemento in lista:
            break
        else:
            print(f'\n > Digite uma opcao valida: {erro}. \n')   
    return elemento

def buscaIndice(elemento, lista):
    for i in range(len(lista)):
        if lista[i] == elemento:  
            return i

def maiorValor(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
            i_maior = i
    return i_maior

def menorValor(lista):
    menor = lista[0]
    i_menor = 0
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            i_menor = i
    return i_menor
        
def mostraCatalogo(vinhos, precos):
    print('\n > Aqui estao nossas opcoes de vinhos: \n')
    for i in range(len(vinhos)):
        print(f'| {vinhos[i]} | valor da garrafa: R${precos[i]:.2f} |')
    print('\n')

def mostrarResultado(vinhos, precos, precos_vinhos, qtd):
    print('\n > Obrigado por comprar na Vinheria Agnello. \n > Confirme as informacoes de sua compra: \n')
    for i in range(len(vinhos)):
        print(f'Quantidade de garrafas de {vinhos[i]}: {qtd[i]}')
    for i in range(len(vinhos)):
        print(f'Preco de {vinhos[i]}: {qtd[i]} x R${precos[i]:.2f} = R${precos_vinhos[i]:.2f}')
    print(f'Quantidade de garrafas totais: {qtd_total} \n'
          f'Preco sem frete: R${preco_total:.2f}')
    if preco_total >= 500:
        print('Frete: GRATIS!!!')
    else:
        print(f'Frete (10%): R${frete:.2f}')
    print(f'Preco total: R${preco_frete:.2f} \n'
          f'Endereco de entrega: {endereco} \n')

def mostrarPrateleira(prateleira):
    print("\n > Estado atual da prateleira:")
    for linha in prateleira:
        print(" | ".join(linha))
    print("\n")

print('\n > Seja Bem Vindo(a) a Vinheria Agnello!!! \n')

ano_atual = 2024
ano = forca_num('Digite o ano em que voce nasceu: ')
idade = ano_atual - ano

if idade >= 18:
    endereco = input('Digite o seu endereco: ')
    prateleira = [["[ ]" for _ in range(3)] for _ in range(3)] 
    lista_vinhos = ['top', 'massa', 'legal']
    lista_precos = [30, 50, 60]
    precos_vinhos = [0, 0, 0]
    lista_qtd = [0, 0, 0]
    opcoes = ['sim', 'nao']   
    
    while True:
        mostraCatalogo(lista_vinhos, lista_precos)
        escolha = forcaEscolha(lista_vinhos, 'Digite o nome do vinho que deseja comprar: ')
        i = buscaIndice(escolha, lista_vinhos)
        qtd = forca_num(f'Digite a quantidade de garrafas que voce quer do vinho {escolha}: ')
        lista_qtd[i] += qtd
        precos_vinhos[i] += lista_precos[i] * qtd
        mostrarPrateleira(prateleira)
        for _ in range(qtd):
            while True:
                linha = forca_num("Digite a linha da prateleira (0-2): ")
                coluna = forca_num("Digite a coluna da prateleira (0-2): ")
                if prateleira[linha][coluna] == "[ ]":
                    prateleira[linha][coluna] = escolha
                    break
                else:
                    print("Este espaco ja esta ocupado. Escolha outro.")
        mostrarPrateleira(prateleira)
        continuar = forcaEscolha(opcoes, 'Deseja continuar comprando? (sim ou nao): ')
        if continuar == 'nao':
            break
    
    i_maior = maiorValor(lista_precos)
    i_menor = menorValor(lista_precos)

    qtd_total = somarLista(lista_qtd)
    preco_total = somarLista(precos_vinhos)
    
    frete = 10/100
    frete *= preco_total

    if preco_total >= 500:
        frete = 0

    preco_frete = preco_total + frete
    
    mostrarResultado(lista_vinhos, lista_precos, precos_vinhos, lista_qtd)
    
else:
    print('\n > Voce deve ser maior de idade para comprar bebidas alcoolicas!!! \n')
