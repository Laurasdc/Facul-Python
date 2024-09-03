'''numero = int(input("digite um número: "))
numero2 = int(input("digite um número: "))
if numero > numero2:
    print(f"O maior número é: {numero}")
else:
    print(f"O maior número é: {numero2}")

ano=int(input("Em que ano você nasceu? "))
if ano<=2005:
    print("Você é obrigado a votar")
elif ano <= 2008:
    print("É opcional você votar")
else:
    print("Você não pode votar")

senha=int(input("Digite uma senha: "))
if senha == 1234:
    print("Acesso Válido")
else:
    print("Acesso Negado"

maca=int(input("Quantas maçãs você vai comprar?"))
if maca < 12:
    valor = 0.3
else:
    maca >= 12
    valor = 0.25
desconto=valor*maca
print(f'Você vai pagar:{desconto}')

sexo= int(input("Qual o seu genero? Se for feminino: 1, se for masculino:2:  "))
altura= float(input("Qual sua altura? "))
if sexo == 1:
    imc= (62.1*altura ) - 44.7
else:
    imc= (72.7*altura ) - 58
print(f"Seu peso ideal é {imc:.2f}")

poligono =i nt(input("Quantos lados tem o seu poligono?"))
if poligono <3:
    print("Não é um poligono")
elif poligono > 5:
    print("Poligono não identificado")
medida = int(input("Quantos centimetros tem o lado do seu poligono?"))
if poligono == 3:
    perimetro= medida * 3
    print(f"O seu poligono é um TRIÂNGULO e o perimetro é {perimetro}")
elif poligono == 4:
    perimetro = medida * 4
    print(f"O seu poligono é um QUADRADO e o perimetro é {perimetro}")
else:
    perimetro = medida * 5
    print(f"O seu poligono é um PENTÁGONO e o perimetro é {perimetro}")

a=int(input("Digite um número: "))
b=int(input("Digite outro número: "))
c=int(input("Digite mais um número: "))
if a>b and a>c:
    print(f"{a} é maior")
elif b>c:
    print(f"{b} é o maior")
else:
    print(f"{c} é o maior")

aux=0
a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))
c = int(input("Digite mais um número: "))
if a>b:
    aux=a
    a=b
    b=aux
if a>c:
    aux=a
    a=c
    c=aux
if b>c:
    aux=b
    b=c
    c=aux
print("Valores em ordem crescente: ",a,b,c )

a = int(input("Digite a medida do primeiro lado: "))
b = int(input("Digite a medida do segundo lado: "))
c = int(input("Digite a medida do terceiro lado: "))

if a == b == c:
    print("Esse triangulo eh Equilátero")
elif a == b or a == c or b == c:
    print("Esse triangulo eh Isósceles")
else:
    print("Esse triangulo eh Escaleno")'''

a = int(input("Digite o primeiro angulo: "))
b = int(input("Digite o segundo angulo: "))
c = int(input("Digite o terceiro angulo: "))

if a == 90 or b == 90 or c == 90:
    print("Triângulo retângulo")
elif a < 90 and b < 90 and c < 90:
    print("Triângulo acutângulo")
else:
    print("Triângulo obtusângulo")
