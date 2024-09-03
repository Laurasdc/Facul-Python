def notnumero(msg):
    verificacao = input(msg)
    while not verificacao.isnumeric():
        verificacao = input(msg)
    return int(verificacao)

def catalogo(vinhos, valores):
    print("Este é o catálogo de vinhos:")
    for i in range(len(vinhos)):
        print(f"{vinhos[i]} - R${valores[i]}")

def forcar(msg, opcoes):
    forcarescolha = input(msg)
    while forcarescolha not in opcoes:
        forcarescolha = input(msg)
    return forcarescolha

vinhos = ["vinho tinto ny", "vinho tinto errejota", "vinho branco vienna", "vinho branco são francisco"]
valores = [60, 48, 120, 88] 
frete = 20

ano = notnumero("Seja bem-vindo(a) à Vinheria Agnello. Qual é o seu ano de nascimento? ")
if ano >= 2007:
    print("Você não é maior de idade. Portanto, não pode comprar bebidas alcoólicas.")
else:
    endereco = input("Qual é o seu endereço? ")
    valortotal = 0  
    vinhos_escolhidos = [] 
    while True:
        catalogo(vinhos, valores)
        escolhavinho = forcar("Qual vinho você deseja? ", vinhos)
        for i in range(len(vinhos)):
            if escolhavinho == vinhos[i]:
                qtdvinhos = notnumero(f"Quantas garrafas de {vinhos[i]} você gostaria? ")  
                valortotal += valores[i] * qtdvinhos  
                vinhos_escolhidos.append((vinhos[i], qtdvinhos)) 
        if input("Quer adicionar mais vinhos? Digite sim ou nao: ") == 'nao':
            break
    valortotal_final = valortotal + frete if valortotal < 500 else valortotal
    print(f"O valor total é: R${valortotal_final:.2f} e será entregue no endereço: {endereco}")
print("\nVinhos escolhidos:")
for vinho, qtd in vinhos_escolhidos:
    print(f"{vinho} --> Quantidade: {qtd} garrafas")
