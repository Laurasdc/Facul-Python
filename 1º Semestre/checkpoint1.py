'''Laura Souza de Carvalho. RM: 556320'''

ano = int(input("Seja bem-vindo(a) a Vinheria Agnello. Qual é o seu ano de nascimento? "))
if ano >= 2007:
    print("Você não é maior de idade. Portanto, não você não pode comprar bebidas alcoólicas")
else:
    endereco = input("Qual é o seu endereço? ")
    vinho = int(input("Este é o nosso catálogo de vinhos: 1: Vinho tinto - Washington - R$ 38.99; 2: Vinho Tinto - Barcelona - R$27.00; 3: Vinho Branco - Paris - R$44.99; 4: Vinho Branco - SP - R$30.90. Qual vinho você gostaria? "))
    quantidade = int(input("Quantas garrafas deste vinho você gostaria? "))
    vinho1 = 38.9
    vinho2 = 27.0
    vinho3 = 44.9
    vinho4 = 30.9
    if vinho == 1:
        valor = vinho1 * quantidade
    elif vinho == 2:
        valor = vinho2 * quantidade
    elif vinho == 3:
        valor = vinho3 * quantidade
    elif vinho == 4:
        valor = vinho4 * quantidade
    if valor >= 100:
        print("Você não ganhou frete grátis. O frete é de R$15,00.")
    else:
        valor = valor + 15
        print("Parabéns, você ganhou frete grátis.")
    print(f"Obrigado por comprar na Vinheria Agnello, o seu total foi de:R${valor}. O pedido será entregue no endereço: {endereco}.")
