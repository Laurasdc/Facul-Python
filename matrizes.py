def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

matriz = [[1,2,3], [4,5,6], [7,8,9], [10,11,12]]
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")
        
print(matriz[0])
print(matriz[1])
print(matriz[2][0])
mostra_matriz(matriz)

