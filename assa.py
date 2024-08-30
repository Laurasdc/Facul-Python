from time import time
import matplotlib.pyplot as plt
def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return
def cria_matriz(linhas,colunas):
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
def contra_diagonal_ruim(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i + j == len(matriz) - 1:
                matriz[i][i] = 1
    return
def contra_diagonal(matriz):
    for i in range(len(matriz)):
        matriz[i][len(matriz) - 1 - i] = 1
    return
def triognal_inferior(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            matriz[i][j] = 1
    return
def triognal_superior(matriz):
    for j in range(len(matriz)):
        for i in range(j):
            matriz[i][j] = 1
    return
def transpor(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return
'''matriz = cria_matriz(5,5)
triognal_superior(matriz)
mostra_matriz(matriz)
print()
transpor(matriz)
mostra_matriz(matriz)'''

xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[i])):
        if i%2 ==0:
            if j%2 == 0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0
        else:
            if j%2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
xadrez = cria_matriz(8, 8)
for i in range(len(xadrez)):
    for j in range(len(xadrez[i])):
        if (i+j)%2 ==0:
            xadrez[i][j] = 1
mostra_matriz(xadrez)
plt.imshow(xadrez)
plt.show()