#1- Função que recebe uma lista de números e retorna a soma dos números

'''def lista(lista_elemento):
    total = 0
    for i in lista_elemento:
        total += i
    return total
nums = [5, 433, 98, 65, 34, 562, 3]
soma = lista(nums)
print(soma)
'''

#2 - Função que recebe uma lista de números e retorna uma lista somente com os pares

'''def filtro_pares(lista):
    pares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
    return pares
lista = [32, 43, 2, 4, 8, 10]
soma_lista = filtro_pares(lista)
print(soma_lista)'''

#3 - Função que recebe uma string e conta a qtd vogais

'''def filtro_vogais(palavra):
    qtd_vogais = 0
    vogais = ['a', 'e', 'i', 'o', 'u']
    for char in palavra:
        if char in vogais:
            qtd_vogais += 1
    return qtd_vogais
palavra = 'laura'
qtd_vogais = filtro_vogais(palavra)
print(f"A palavra {palavra} tem {qtd_vogais} vogais")'''

#Função que obrigue um usuário a dar uma resposta que exista
def forcar_opcao(msg, msg_erro, lista_opcoes):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        escolha = input(msg)
    return escolha
vinhos = ['vinho1', 'vinho2', 'vinho3', 'vinho4']
erro = '\n'.join(vinhos)
opcao = forcar_opcao("Diga seu vinho favorito: ", f"Somente:\n{erro}", vinhos )
opcoes = ['continuar', 'não']
erro = '\n'.join(opcoes)
continuar_ou_nao = forcar_opcao("Você deseja continuar ou não?\n-->", opcoes)
