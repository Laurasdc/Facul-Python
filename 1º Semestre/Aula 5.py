'''#Exercício 1
num_a = int(input("Diga um numero: "))
num_b = int(input("Diga um numero: "))
if num_a > num_b:
    print(num_a)
else:
    print(num_b)
#Exercício 2
ano = int(input("Diga seu ano de nascimento: "))
idade = 2024 - ano
if idade >= 18:
    print("Obrigatório votar")
elif idade >= 16:
    print("Opcional")
else:
    print("Não precisa votar")

#Exercício 3
senha_cadastrada = 1234
senha = int(input('Diga sua senha: '))
if senha == senha_cadastrada:
    print("Acesso Permitido")
else:
    print("Acesso Negado")

senha_cadastrada = "1234"
senha = input('Diga sua senha: ')
if senha == senha_cadastrada:
    print("Acesso Permitido")
else:
    print("Acesso Negado")

#Exercício 4
preco = 0.3
qtd = int(input("Diga a qtd de maçãs: "))
if qtd >= 12:
    preco = 0.25
valor = preco*qtd
print(f"Vc gastou R${valor} em {qtd} maçãs!")

#Exercício 6
sexo = input("Diga seu sexo \n1- feminino\n2- masculino : ")
altura = float(input("Diga sua altura: "))
if sexo == '1':
    peso = (62.1*altura) - 44.7
else:
    peso = (72.7*altura) - 58
print(f"Seu peso ideal é de {peso:.2f}")
#Exercício 7
lados = int(input("Diga o numero de lados: "))
medida = int(input("Diga a medida do lado: "))
if lados == 3:
    forma = "Triangulo"
    perimetro = 3*lados
elif lados == 4:
    forma = "Quadrado"
    perimetro = 4*lados
else:
    forma = "Pentágono"
    perimetro = 5*lados
print(f"Voce escolheu um {forma} de perímetro {perimetro}")

lados = int(input("Diga o numero de lados: "))
forma = ''
if lados < 3:
    print(f"Não é um polígono")
elif lados == 3:
    forma = "Triangulo"
elif lados == 4:
    forma = "Quadrado"
elif lados == 5:
    forma = "Pentágono"
else:
    print("Não identificado")
if forma:
    medida = int(input("Diga a medida do lado: "))
    perimetro = lados*medida
    print(f"Voce escolheu um {forma} de perímetro {perimetro}")

lados = int(input("Diga o numero de lados: "))
if lados < 3:
    print(f"Não é um polígono")
elif lados > 5:
    print("Não identificado")
else:
    medida = int(input("Diga a medida do lado: "))
    if lados == 3:
        forma = "Triangulo"
    elif lados == 4:
        forma = "Quadrado"
    else:
        forma = "Pentágono"
    perimetro = lados*medida
    print(f"Voce escolheu um {forma} de perímetro {perimetro}")
#Exercício 10
lado1 = int(input("Dia o primeiro lado: "))
lado2 = int(input("Dia o segundo lado: "))
lado3 = int(input("Dia o terceiro lado: "))

if lado1 == lado2 and lado3 == lado1:
    print("Equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles")
else:
    print("Escaleno")

ang1 = int(input("Dia o primeiro angulo: "))
ang2 = int(input("Dia o segundo angulo: "))
ang3 = int(input("Dia o terceiro angulo: "))

if ang1 == 90 or ang2 == 90 or ang3 == 90:
    print("Retângulo")
elif ang1 > 90 or ang2 > 90 or ang3 > 90:
    print("Obtuso")
else:
    print("Agudo")

#exercício 9
a = int(input("Diga um numero: "))
b = int(input("Diga outro numero: "))
c = int(input("Diga outro numero: "))

maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print(maior)

if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

a = int(input("Diga um numero: "))
b = int(input("Diga outro numero: "))
c = int(input("Diga outro numero: "))
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
meio = a + b + c - menor - maior
print(menor,meio,maior)

a = int(input("Diga um numero: "))
b = int(input("Diga outro numero: "))
c = int(input("Diga outro numero: "))
if a > c  and a > b:
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

v = int(input("Diga a velocidade: "))
if v <= 100:
    print("Isento")
else:
    if v <= 120:
        multa = 0.2*v
    elif v <= 150:
        multa = 0.2*120 + 0.3*v
    else:
        multa = 0.2*120 + 0.3*150 + 0.4*v
    print(f"Sua multa sera de R${multa:.2f}")
'''
par = 0
num = int(input("Diga um numero :"))
if num %2 ==0:
    par = par + 1
num = int(input("Diga um numero :"))
if num %2 ==0:
    par = par + 1
num = int(input("Diga um numero :"))
if num %2 ==0:
    par = par + 1
num = int(input("Diga um numero :"))
if num %2 ==0:
    par = par + 1
num = int(input("Diga um numero :"))
if num %2 ==0:
    par = par + 1
impar = 5 - par
print(f"{par} pares e {impar} impares")





