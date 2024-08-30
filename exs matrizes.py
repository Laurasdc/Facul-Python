#Gráfico com matplotlib
'''def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(i+j)
        matriz.append(linha)
    return matriz
matriz = cria_matriz(5,5)
mostra_matriz()
matriz = cria_matriz(100,100)
plt.imshow(matriz, 'Blues_r')
plt.colorbar()
plt.show()'''

#1,2:
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
    return matriz'''

#3- Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da diagonal para 1.
'''def diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][i] = 1
    return
matriz = cria_matriz(10,10)
diagonal(matriz)
mostra_matriz(matriz)'''

#4 -  Faça uma função que recebe uma matriz quadrada como parâmetro e altera todos os elementos da “contra-diagonal” para 1
'''def contra_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1 - i] = 1
matriz = cria_matriz(10,10)
contra_diagonal(matriz)
mostra_matriz(matriz)'''

#5 – Faça uma função que recebe uma matriz quadrada e altera todos os elementos acima/abaixo da diagonal para 1
#Para abaixo da diagonal:
'''def trigonal_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return

def trigonal_inferior(matriz):
    for j in range(len(matriz)):
        for i in range(i):
            matriz[i][j] = 1
    return

matriz = cria_matriz(10,10)
trigonal_inferior(matriz)
mostra_matriz(matriz)'''

# 6 – Faça uma função que recebe uma matriz quadrada e retorne sua transposta
'''def matriz_transporta(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return


matriz = cria_matriz(5,5)
trigonal_inferior(matriz)
matriz_transporta(matriz)
mostra_matriz(matriz)
'''
# 8 - Faça um código que transforma uma matriz quadrada 8x8 em um tabuleiro de xadrez
'''xadrez = cria_matriz(8,8)
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
                xadrez[i][j] = 1'''

#10 - Devido ao covid as cadeiras de cinema tem que ser utilizadas com um espaçamento de uma cadeira desocupada tanto na frente quanto atrás e dos lados. Represente está situação com uma matriz 50x50 em que cada local (i,j) tem nele a palavra “vaga” ou ocupada.
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append("[vaga]")
        matriz.append(linha)
    return matriz


def mostra_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))
    return


def ocupa_cadeiras_com_espacamento(matriz, espacamento):
    n = len(matriz)
    
    for i in range(0, n, espacamento+1):  
        for j in range(0, n, espacamento+1):
            matriz[i][j] = "[ocupada]"

matriz_cinema = cria_matriz(50, 50)

ocupa_cadeiras_com_espacamento(matriz_cinema, espacamento=1)

mostra_matriz(matriz_cinema)


