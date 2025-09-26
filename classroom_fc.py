'''
#          ARQUIVO CONSOLIDADO - FUNDAMENTOS DA COMPUTAÇÃO 2025.2
#       Este arquivo contém os exercícios organizados por data de aula.

#                        AULA DE 25 DE AGOSTO DE 2025

# 1: Avaliação da nota (Aprovado, Recuperação, Reprovado).

    try:
        nota = float(input("Digite sua nota (não tenha vergonha, não fica gravado depois :): "))
        if nota < 0 or nota > 10:
            print("Nota inválida. Digite um valor entre 0 e 10.")
        elif nota < 4:
            print("Reprovado.\n")
        elif 4 <= nota < 7.1:
            print("Recuperação!\n")
        else:
            print("Aprovado!\n")
    except ValueError:
        print("Entrada inválida.\n")

# 2: Peça dois números inteiros e determine qual é o maior.

    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))
        if n1 > n2:
            print(f"O maior número é {n1}\n")
        elif n2 > n1:
            print(f"O maior número é {n2}\n")
        else:
            print(f"Os números são iguais!\n")
    except ValueError:
        print("Entrada inválida.\n")

# 3: Verifique se o dinheiro é suficiente para a compra de um produto.

    try:
        preco = float(input("Digite o preço do produto: "))
        valor_disponivel = float(input("Digite o valor disponível: "))
        if valor_disponivel >= preco:
            print(f'Boas compras! Seu troco será de R$ {valor_disponivel - preco:.2f}.\n')
        else:
            print(f'Dinheiro insuficiente! Faltam R$ {preco - valor_disponivel:.2f} para a compra.\n')
    except ValueError:
        print("Entrada inválida.\n")

# 4: Leia uma idade e imprima a situação (Bebê, Criança, etc).

    try:
        ano_atual = date.today().year
        nascimento = int(input('Digite seu ano de nascimento: '))
        idade = ano_atual - nascimento
        print(f"Quem nasceu em {nascimento} tem (ou fará) {idade} anos em {ano_atual}.")
        if idade <= 0:print('Erro!')
        elif 0 < idade <= 3:print('Situação: Bebê!\n')
        elif idade <= 11:print('Situação: Criança!\n')
        elif idade <= 17:print('Situação: Adolescente!\n')
        elif idade <= 30:print('Situação: Jovem!\n')
        elif idade <= 64:print('Situação: Adulto!\n')
        else:            print('Situação: Idoso!\n')
    except ValueError:
        print("Entrada inválida.\n")

# 5: Peça ao usuário um número e diga se ele é par ou ímpar.



# 6: Peça um número e diga se ele é positivo, negativo ou zero.



# 7: Leia um número, verifique se ele é divisível por 5, 3 ou pelos dois ao mesmo tempo e retorne se o número é divisível por ambos, apenas por um deles ou por nenhum.



#                        AULA DE 29 DE AGOSTO DE 2025

# 10 - Peça ao usuário três números representando os comprimentos dos lados de um triângulo: a, b e c. Verifique se eles podem formar um triângulo (a soma de dois lados deve ser maior que o terceiro para todos os casos). Se for um triângulo válido, informe também o tipo:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes

#                      AULA DE 08 DE SETEMBRO DE 2025



#                      AULA DE 08 DE SETEMBRO DE 2025

# 1) Peça ao usuário um número e exiba a tabuada desse número de 1 a 10.

n = int(input('De qual número deseja exibir a tabuada? '))

    for i in range(1, 11):
        print(f'{i} + {n} = {i + n}\n')


# 2)
    n = int(input('Digite um número: '))
    pares = list([])

    if n%2==0:
        for i in range(2, n+1, 2):
            pares.append(i)
    else:
        for i in range(2, n, 2):
            pares.append(i)
            
    print(f'Foram encontrados {len(pares)}, são eles: {pares}')

# 3)
    n = int(input('Digite um número: '))
    ns = list([])v

    for i in range(n, 0, -1):
        print(f'{i}\n')
        ns.append(i)
    
    print(f'São {len(ns)} números.') 

# 4)


# 5)
    n = int(input('Digite um número: '))
    total_primos = list([])
    n_atual = 2

    while len(total_primos) < n:

        if e_primo(n_atual):
            total_primos.append(n_atual)
        n_atual +=1
    
    print(f'Os primos são {total_primos}')

# 6)
    n = int(input('Digite um número: '))
    divisores = list([])

    for i in range(1, n+1):
        if n%i==0:
            divisores.append(i)

    print(f'São {len(divisores)} divisores.')

# 7)
    n = int(input('Digite um número: '))
    pares = list([])

    if n%2==0:
        for i in range(n+1, 2, 2):
            pares.append(i)
    else:
        for i in range(n, 2, 2):
            pares.append(i)

    print(f'Foram encontrados {len(pares)}, são eles: {pares}')

#                        AULA DE 12 DE SETEMBRO DE 2025

# 1: Leia 5 números inteiros (usando um loop for) e mostre qual é o maior e qual é o menor.

try:
    primeiro_numero = int(input('Digite o 1º número: '))
    maior = menor = primeiro_numero

    # O loop executa 4 vezes para ler os números restantes.
    for i in range(4):
        numero_atual = int(input(f'Digite o {i+2}º número: '))
        if numero_atual > maior:
            maior = numero_atual
        if numero_atual < menor:
            menor = numero_atual

    if maior == menor:
        print('Todos os números digitados são iguais!\n')
    else:
        print(f'Maior número: {maior}; Menor número: {menor}.\n')
except ValueError:
    print("Entrada inválida. Por favor, digite apenas números inteiros.\n")


# EXERCÍCIO 2: Leia um número inteiro positivo n e faça uma contagem regressiva até 0.
# Para números maiores que 10, imprima "Contagem longa!". Para 0 ou negativos, mostre "Número inválido".
# 

# 3: Leia 10 números e mostre a soma dos positivos, negativos e zeros.









#: Conversões de Temperatura (Celsius -> Fahrenheit/Kelvin)

try:
    celsius = float(input('Digite uma temperatura em Celsius: '))
    fahrenheit = (9 * celsius / 5) + 32
    kelvin = celsius + 273.15
    print(f'{celsius}ºC equivalem a {fahrenheit:.2f}ºF e {kelvin:.2f}K\n')
except ValueError:
    print("Entrada inválida.\n")


try:
    a = float(input('Digite o coeficiente a: '))
    b = float(input('Digite o coeficiente b: '))
    c = float(input('Digite o coeficiente c: '))
    if a == 0:
        print("Não é uma equação de segundo grau.\n")
    else:
        delta = (b**2 - 4*a*c)
        if delta < 0:
            print("A equação não possui raízes reais.\n")
        else:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            print(f'As raízes da equação são: X1 = {x1:.2f} e X2 = {x2:.2f}.\n')
except ValueError:
    print("Entrada inválida.\n")

#: Conversão Decimal para Binário

try:
    decimal = int(input('Digite o número decimal (inteiro) que deseja converter: '))
    if decimal == 0:
        binario = '0'
    else:
        binario = ''
        quociente = abs(decimal)
        while quociente > 0:
            resto = quociente % 2
            binario = str(resto) + binario
            quociente = quociente // 2
        if decimal < 0:
             binario = "-" + binario
    print(f'O número {decimal} em binário é: {binario}.\n')
except ValueError:
    print("Entrada inválida.\n")

# 1ª Aula de Fundamentos da Computação

# A) Celsius -> Fahrenheit (-> Kelvin de bônus)

celsius = int(input('Digite uma temperatura em Celsius: '))

fahrenheit = (9 * celsius/5) + 32
kelvin = celsius + 273.15

print(f'{celsius}ºC equivalem a {fahrenheit}ºF e {kelvin}K')

# B) Ler dois valores inteiros, trocar valores e exibir antes e depois

var1 = int(input("Digite um valor: "))
var2 = int(input("Digite mais um valor: "))

print(f'1º número: {var1}; 2º número: {var2}')
var1, var2 = var2, var1
print(f'1º número trocado: {var2}; 2º número trocado: {var1}')

# C) Ler o valor do tempo em segundos e imprimir no formato hora, minuto, segundos

second = float(input('Digite a quantidade de segundos a ser convertida: '))
hour = second / 3600
minute = second / 60

print(f'{hour:.2f} horas, {minute:.2f} minutos e {second:.2f} segundos.')

# D) Calcula as raízes de uma equação do 2º grau (e vértice de bônus)

a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

delta = (b**2 - 4*a*c)
x1 = (-b + delta**0.5) / (2*a)
x2 = (-b - delta**0.5) / (2*a)
vertex_x = -b / (2*a)
vertex_y = -delta / (4*a)

print(f'As raízes da equação são: X1 = {x1:.2f} e X2 = {x2:.2f}.')

if a < 0:
    print(f'O ponto máximo da equação é dado por: ({vertex_x}, {vertex_y}).')
else:
    print(f'O ponto mínimo da equação é dado por: ({vertex_x}, {vertex_y}).')



while True:
    array = []

    initial_term = int(input("Digite um termo da progressão: "))
    final_term = int(input("Digite outro termo da progressão: "))
    reason = int(input("Digite a razão da progressão: "))
    gerneral_term = initial_term * (reason ** (initial_term - 1))

    for i in range(initial_term, final_term, general_term):
        general_term = initial_term * (reason ** (i - 1))
        array.append(general_term)

    print(f"A progressão geométrica é {array}.")

    answer = input("Deseja continuar (s/n)? ")

    if answer.lower() != 's':
        break

2ª Aula de Fundamentos da Computação

    raio = float(input('Digite o raio da esfera: '))

    volume = (4/3) * math.pi * raio ** 3

    print(f'O volume da esfera é: {volume:.2f}')



    raio = float(input('Digite o raio da circunferência: '))

    area = math.pi * raio

    print(f'A área é: {area:.2f}')



    massa = float(input('Digite seu peso em quilogramas: '))
    altura = float(input('Digite sua altura em metros: '))

    imc =  massa / altura ** 2

    print(f'Seu Índice de Massa Corporal é: {imc:.2f}')



    salario_bruto = float(input('Digite seu salario bruto: '))
    desconto_inss, desconto_ir = 0.10, 0.15

    salario_liquido = salario_bruto * (1 - desconto_inss) * (1 - desconto_ir)

    print(f'Seu salário líquido é {salario_liquido:.2f}')



    densidade = float(input('Digite a densidade do fluído: '))
    gravidade = float(input('Digite a aceleração da gravidade: '))
    profundidade = float(input('Digite a profundidade: '))

    pressao = densidade * gravidade * profundidade

    print(f'A pressão é: {pressao:.2f} atms.')



    capital_inicial = float(input('Digite o valor inicial: '))
    taxa = float(input('Digite o valor da taxa de juros: '))
    tempo = float(input('Digite a duração do investimento: '))

    montante = capital_inicial * (1 + taxa * tempo)

    print(f'O montante é: {volume:.2f}')



    massa = float(input('Digite a massa: '))
    calor = float(input('Digite o calor específico: '))
    temperatura = float(input('Digite a variação da temperatura: '))
    potencia = float(input('Digite a potência: '))

    tempo = (massa * calor * temperatura) / potencia

    print(f'O tempo necessário para aquecimento/cozimento é: {tempo:.2f}.')



    ponto_x = [float(coord) for coord in input('Digite as coordenadas do 1º ponto (x, y): ').split(',')]
    ponto_y = [float(coord) for coord in input('Digite as coordenadas do 2º ponto (x, y): ').split(',')]

    x1, y1 = ponto_x
    x2, y2 = ponto_y

    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print(f'A distância entre eles é {distancia:.2f}.')

# ) O usuário insere os lados a, b, c de um triângulo, e o programa calcula:

    lados = [float(coord) for coord in input('Digite o comprimento dos lados do triângulo: ').split(',')]

    a, b, c = lados
    perimetro = a + b + c
    s = semiperimetro = (perimetro)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))

    print(f'A área e o perímetro do triângulo são: {area:.2f} e {perimetro:.2f}.')

# ) O usuário insere a massa m e a velocidade v de um objeto, e o programa calcula a energia cinética Ec usando:

    massa_e_velocidade = [float(coord) for coord in input('Digite a massa e a velocidade para o cálculo da energia cinética: ').split(',')]

    massa, velocidade = massa_e_velocidade
    energia_cinetica = 0.5 * massa * velocidade**2

    print(f'A energia cinética é: {energia_cinetica}')

# ) O usuário insere um valor em reais R e as taxas de câmbio para dólar cd e euro ce, e o programa calcula os valores convertidos:
Dólar = R · cd, Euro = R · ce

    reais = float(input('Quanto você quer trocar? '))
    taxa_dolar = float(input(f'Digite a taxa de câmbio para converter os R$ {reais} em dólar: '))
    taxa_euro = float(input(f'Digite a taxa de câmbio para converter os R$ {reais} em euros: '))

    dolar = reais * taxa_dolar
    euro = reais * taxa_euro

    print(f'Os valores correspondentes a R$ {reais:.2f} em dólar e euro são: ${dolar:.2f} e € {euro:.2f}.')


    n = int(input("Forneca um numero: "))
    divisors = 0

    for i in range(1, n+1):
        if 3%i == 0 or 5%i == 0:
            divisors += i

    print(divisors)

    resposta = input('Deseja continuar? ')
    if resposta != 's':
        break


    


    primeiro_numero = int(input('Digite um número: '))
    maior = menor = primeiro_numero

    for _ in range(4):
        numero_atual = int(input('Digite um número: '))
        if numero_atual > maior:
            maior = numero_atual
        if numero_atual < menor:
            menor = numero_atual

    if maior == menor:
        print('Os números são iguais!')
    else:
        print(f'Maior: {maior}; Menor: {menor}.')

    decimal = float(input('Digite o decimal que deseja converter para binário: '))
    binario = ''
    quociente = decimal

    if decimal == 0:
        binario = '0'
    else:
        while quociente > 0:
            resto = int(decimal % 2)
            binario += str(resto)
            quociente = decimal // 2
        
    print(f'O número {decimal} em binário é: {binario}.')
'''
while True:

    

    resposta = input('Deseja continuar? ').lower()
    if resposta not in ('s', 'y'):
        break
