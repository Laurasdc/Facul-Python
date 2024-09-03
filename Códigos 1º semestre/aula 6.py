'''qtd_pares = 0
num = it(input("Diga um numero: "))
if num%2 == 0:
    qtd_pares = qtd_pares + 1

num = int(input("Diga um numero: "))
if num%2 == 0:
    qtd_pares = qtd_pares + 1

num = int(input("Diga um numero: "))
if num%2 == 0:
    qtd_pares = qtd_pares + 1

num = int(input("Diga um numero: "))
if num%2 == 0:
    qtd_pares = qtd_pares + 1

num = int(input("Diga um numero: "))
if num%2 == 0:
    qtd_pares = qtd_pares + 1
print(f"Você digitou {qtd_pares} pares")

qtd_pares = 0
contador = 0
while contador < 5:
    num = int(input("Diga um numero: "))
    if num%2 == 0:
        qtd_pares = qtd_pares + 1
    contador = contador + 1
print(f"Você digitou {qtd_pares} pares")


senhacorreta = 1234
tentativa = int(input("Digite a senha: "))
while tentativa != senhacorreta:
    tentativa = int(input("Digite novamente: "))
print("Acesso Liberado")


tentativas = input("Digite a senha: ")
senhacorreta = '1234'
contador = 1
while tentativas != senhacorreta and contador < 3:
    print(f"Vc é um hacker? só mais {3- contador} tentativas")
    tentativas = input("Digite novamente: ")
    contador += 1
if tentativas == senhacorreta:
    print("Acesso liberado")
else:
    print("Sai hacker")'''

i = 0
soma = 0
while i < 100:
    i += 1
    soma += i
print(soma)
