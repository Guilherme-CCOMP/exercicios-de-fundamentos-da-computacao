'''
# E) Resolva algum problema de combinatória com PY
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

print("--- Exercício 1: Tabuada ---")
try:
    n_tabuada = int(input('De qual número deseja exibir a tabuada? '))
    
    print(f"\nExibindo a tabuada de MULTIPLICAÇÃO do {n_tabuada}:")
    for i in range(1, 11):
        print(f'{n_tabuada} x {i} = {n_tabuada * i}')
    print("")

except ValueError:
    print("Entrada inválida.\n")


# 2: Peça um número N e mostre todos os pares de 1 a N, com a quantidade total.

print("--- Exercício 2: Números Pares até N ---")
try:
    n_pares = int(input('Digite um número: '))
    pares = []
    for i in range(2, n_pares + 1, 2):
        pares.append(i)
    print(f'Foram encontrados {len(pares)} números pares. São eles: {pares}\n')
except ValueError:
    print("Entrada inválida.\n")


# 3: Solicite um número N e exiba uma contagem regressiva até 1.

print("--- Exercício 3: Contagem Regressiva ---")
try:
    n_regressivo = int(input('Digite um número para a contagem regressiva: '))
    print("Iniciando contagem:")
    for i in range(n_regressivo, 0, -1):
        print(i)
    print("Contagem finalizada.\n")
except ValueError:
    print("Entrada inválida.\n")


# EXERCÍCIO 5: Escreva um algoritmo que retorne os N primeiros números primos.

print("--- Exercício 5: N Primeiros Números Primos ---")
def e_primo(num):
    if num <= 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

try:
    n_primos = int(input('Quantos números primos você deseja encontrar? '))
    total_primos = []
    numero_atual = 2
    while len(total_primos) < n_primos:
        if e_primo(numero_atual):
            total_primos.append(numero_atual)
        numero_atual += 1
    print(f'Os {n_primos} primeiros primos são: {total_primos}\n')
except ValueError:
    print("Entrada inválida.\n")

# -----------------------------------------------------------------------------------
# EXERCÍCIO 6: Leia um número inteiro e conte quantos divisores ele possui.
# -----------------------------------------------------------------------------------
print("--- Exercício 6: Contagem de Divisores ---")
try:
    n_divisores = int(input('Digite um número para contar seus divisores: '))
    divisores = []
    for i in range(1, n_divisores + 1):
        if n_divisores % i == 0:
            divisores.append(i)
    print(f'O número {n_divisores} possui {len(divisores)} divisores. São eles: {divisores}\n')
except ValueError:
    print("Entrada inválida.\n")

# -----------------------------------------------------------------------------------
# EXERCÍCIO 7: Leia um inteiro n e mostre todos os pares de n até 2 em ordem decrescente.
# -----------------------------------------------------------------------------------
print("--- Exercício 7: Pares em Ordem Decrescente ---")
try:
    n_pares_dec = int(input('Digite um número: '))
    pares_dec = []
    inicio = n_pares_dec if n_pares_dec % 2 == 0 else n_pares_dec - 1
    for i in range(inicio, 1, -2):
        pares_dec.append(i)
    print(f'Foram encontrados {len(pares_dec)} pares em ordem decrescente. São eles: {pares_dec}\n')
except ValueError:
    print("Entrada inválida.\n")

'''
from datetime import date
import math


while True:

    
    
    nao_primos = []
    primos = []
    print(date.today())
    numbers = [abs(int(i)) for i in input('Digite os números que deseja saber se são primos: ').split(',')]

    for i in numbers:
        if i <= 1:
           nao_primos.append(i)
        else:
            for n in range(2, int(math.sqrt(i))+1):
                if i%n == 0:
                    nao_primos.append(i)
                    break
            else:
                primos.append(i)

    primos.sort()
    nao_primos.sort()
    print(f'Os primos são: {list(dict.fromkeys(primos))}\nOs não-primos são: {list(dict.fromkeys(nao_primos))}')

    answer = input("Deseja continuar (s/n)? ")
    if answer.lower() != 's' and answer.lower() != 'y':
        break

    n = int(input("Forneca um numero: "))
    divisors = []

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)

    if len(divisors) == 0:
        print(f"{n} e primo!")
    else:
        print(f"{n} nao e primo!")

primos_ate_100 = {
        "primos_ate_7": (2, 3, 5, 7),
        "primos_final_1": (11, 31, 41, 61, 71),
        "primos_final_3": (13, 23, 43, 53, 73, 83),
        "primos_final_7": (17, 37, 47, 67, 97),
        "primos_final_9": (19, 29, 59, 79, 89),
    }

def crivo_eratostenes(limite):
    # 1. Cria uma lista de booleanos e assume que todos os números são primos.
    # A lista tem tamanho 'limite + 1' para incluir o número 'limite'.
    is_prime = [True] * (limite + 1)
    
    # 2. 0 e 1 não são números primos.
    is_prime[0] = is_prime[1] = False

    # 3. Começa a iteração de 2 até a raiz quadrada do limite.
    # Isso porque se um número n é composto, ele tem um fator primo menor ou igual à sua raiz quadrada.
    p = 2
    while (p * p <= limite):
        # Se is_prime[p] é True, então p é um número primo.
        if (is_prime[p] == True):
            # 4. Marca todos os múltiplos de p como não primos, começando de p*p.
            for i in range(p * p, limite + 1, p):
                is_prime[i] = False
        p += 1

    # 5. Coleta todos os números primos (índices onde is_prime é True).
    primos = [i for i, prime in enumerate(is_prime) if prime]
    return primos

# Exemplo de uso:
limite_superior = 50
lista_de_primos = crivo_eratostenes(limite_superior)
print(f"Números primos até {limite_superior}: {lista_de_primos}")


def e_primo(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

def convercao_binario(decimal):
    restos = []
    while decimal % 2 != 0:
        int(decimal) = decimal % 2
        restos.insert(0, decimal)
    numero_binario = "".join(str(r) for r in restos)
    return numero_binario

def convercao_decimal(binario):
    restos = []
    while binario % 2 != 0:
        int(binario) = binario % 2
        restos.insert(0, binario)
    numero_binario = "".join(str(r) for r in restos)
    return numero_binario

def convercao_binario_decimal(numeros[0], numeros[1]):
    restos = []
    while decimal % 2 != 0:
        int(decimal) = decimal % 2
        restos.insert(0, decimal)
    numero_binario = "".join(str(r) for r in restos)
    return numero_binario

def convercao_decimal_binario(numeros[0], numeros[1]):
    restos = []
    while decimal % 2 != 0:
        int(decimal) = decimal % 2
        restos.insert(0, decimal)
    numero_binario = "".join(str(r) for r in restos)
    return numero_binario

escolha = input('''O que deseja fazer:\n
                Converter número decimal para binário (1);\n
                O contrário (2)')\n
                Ou os dois de uma vez (3)? ''')

if escolha == 1:
    decimal = float(input('Digite um número: '))
    print(convercao_binario(decimal))
elif escolha == 2:
    binario = float(input('Digite um número: '))
    print(convercao_binario(binario))
else:
    escolha_ordem = input('''Em qual ordem:\n
                            Decimal, binário (1);\n
                            O contrário (2)? ''')
    if escolha_ordem == 1:
        numeros = float(input('Digite um número: '))
        print(convercao_decimal_binario(binario))
    else:
        numeros = float(input('Digite um número: '))
        print(convercao_binario_decimal(binario))