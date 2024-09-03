ano = input("Seja bem-vindo(a) à Vinheria Agnello. Qual é o seu ano de nascimento? ")
while not ano.isnumeric():
    ano = input("Qual é o seu ano de nascimento? ")
ano = int(ano)

if ano >= 2007:
    print("Você não é maior de idade. Portanto, não pode comprar bebidas alcoólicas.")
else:
    endereco = input("Qual é o seu endereço? ")

    vinho1 = "Vinho tinto NY"
    vinho2 = "Vinho tinto Errejota"
    vinho3 = "Vinho branco Vienna"
    vinho4 = "Vinho branco São Francisco"

    valor1 = 60.0
    valor2 = 48.0
    valor3 = 120.89
    valor4 = 88.5

    frete = 20
    valortotal = 0

    qtd_vinho1 = 0
    qtd_vinho2 = 0
    qtd_vinho3 = 0
    qtd_vinho4 = 0

    print(f"Este é o nosso catálogo de vinhos:\n 1: {vinho1} --> R${valor1}\n 2: {vinho2} --> R${valor2}\n "
          f"3: {vinho3} --> R${valor3}\n 4: {vinho4} --> R${valor4}\n ")

    while True:
        vinho_escolhido = int(input("Qual vinho você deseja? Digite o número referente ao vinho: "))
        qtd = int(input("Quantas garrafas você gostaria? "))

        if vinho_escolhido == 1:
            nome_vinho = vinho1
            valor = valor1
            qtd_vinho1 += qtd
        elif vinho_escolhido == 2:
            nome_vinho = vinho2
            valor = valor2
            qtd_vinho2 += qtd
        elif vinho_escolhido == 3:
            nome_vinho = vinho3
            valor = valor3
            qtd_vinho3 += qtd
        else:
            nome_vinho = vinho4
            valor = valor4
            qtd_vinho4 += qtd

        valortotal += valor * qtd

        escolha = input("Quer adicionar mais vinhos?\nDigite 'sim' para adicionar mais ou 'não' para finalizar o pedido: ")
        if escolha.lower() != 'sim':
            break

    valortotal_final = valortotal + frete if valortotal < 500 else valortotal
    print(f"Muito obrigado por comprar na Vinheria Agnello! Você selecionou:\n"
          f"{qtd_vinho1} de {vinho1}\n"
          f"{qtd_vinho2} de {vinho2}\n"
          f"{qtd_vinho3} de {vinho3}\n"
          f"{qtd_vinho4} de {vinho4}\n"
          f"O valor total é: R${valortotal_final} e será entregue no endereço: {endereco}")
