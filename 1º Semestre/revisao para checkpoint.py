'''Primeiro exercicio:
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
if a==b:
    print('N pode ser os mesmos numeros')
elif a > b:
    print(a)

else:
    print(b)

Segundo exercicio:

ano = int(input("Digite o ano que voce nasceu"))

if ano <= 2005:
    print("Voce eh obrigado a votar")

elif ano <= 2008:
    print("Voce tem o voto optativo")

else:
    print("Voce nao pode votar")

Terceiro exercicio:

senha = int(input("Qual eh a senha? "))

if senha == 1234:
    print("ACESSO PERMITIDO ")

else:
    print("ACESSO NEGADO ")

Quarto exercicio:

macas = int(input("Quantas macas voce comprou? "))

if macas >= 12:
    valor = macas * 0.25
    print(f"O novo valor eh: {valor}")
else:
    valor = macas * 0.30
    print(f"O novo valor eh: {valor}")

Quinto exercicio:

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
if a > c and a > b:
    aux = a
    a = c
    c = aux
elif b > c:
    aux = b
    b = c
    c = aux
if a > b:
    aux = a
    a = b
    b = aux

print(a,b,c)

Exercicio 6:

sexo = int(input("Qual eh o seu genero? 1- feminino; 2- masculino "))
altura = float(input("Qual eh a sua altura? "))
if sexo == 1:
    peso = (62.1 * altura) - 44.7
else:
    peso = (72.7 * altura) - 58
print(f"Seu peso ideal é {peso:.2f}")

Exercicio 7 e 8:

lados = int(input("Quantos lados tem o seu poligono?"))
if lados < 3:
    print(f"Não é um polígono")
elif lados > 5:
    print("Não identificado")
else:
    medida = int(input("Diga a medida do lado: "))
    if lados == 3:
        forma = "Triângulo"
    elif lados == 4:
        forma = "Quadrado"
    else:
        forma = "Pentágono"
    perimetro = lados * medida
    print(f"Você escolheu um {forma} de perímetro {perimetro}")

Exercicio 9:
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(maior)

// outra forma exercício 9
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)

Exercicio 10:
a = int(input("Digite a medida do primeiro lado: "))
b = int(input("Digite a medida do segundo lado: "))
c = int(input("Digite a medida do terceiro lado: "))
if a == b and c == a :
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")'''

Exercicio 11:
a = int(input("Digite o primeiro angulo: "))
b = int(input("Digite o segundo angulo: "))
c = int(input("Digite o terceiro angulo: "))

if a == 90 or b == 90 or c == 90:
    print("Triângulo retângulo")
elif a < 90 and b < 90 and c < 90:
    print("Triângulo acutângulo")
else:
    print("Triângulo obtusângulo")


