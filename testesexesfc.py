'''
while True:
    try:
        initial_term = int(input("Digite o termo inicial da PG: "))
        reason = int(input("Digite a razão da PG: "))
        num_terms = int(input("Digite quantos termos devem ser gerados: "))

        if num_terms <= 0:
            print("O número de termos deve ser positivo.")
            continue

        progression = []

        # O loop usa 'i' para representar a posição (começando do 0).
        for i in range(num_terms):
            # Calcula o termo da posição 'i' diretamente com a fórmula.
            # O expoente é 'i' porque o range começa em 0 (para i=0, razao**0=1).
            term = initial_term * (reason ** i)
            progression.append(term)

        print(f"\nA progressão geométrica é: {progression}\n")

    except ValueError:
        print("Erro: Por favor, digite apenas números inteiros válidos.")

    answer = input("Deseja continuar (s/n)? ")
    if answer.lower() != 's':
        break

pontos_xy = [float(coord) for coord in input('Digite as coordenadas dos pontos x1, y1, x2, y2 (sem parênteses): ').split(',')]

    x1, y1, x2, y2 = pontos_xy

    distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print(f'A distância entre eles é {distancia:.2f}.')

7

n= [input('Digite um número: ')】
print(f'Seu número tem {len(n)}.')

8

n= int(input('Digite um número: '))
squares = list([])

for i in range(1, n+1):
  squares.append(i**2)

print(squares)

9

n= int(input('Digite um número: '))
impares = list([])

if n%2==0:
  for i in range(n-1, 1, -1)
    impares.append(i)
else:
  for i in range(1, n, -1)
    impares.append(i)

print(impares)

10

while True:

  n= int(input('Digite um número: '))

  if n%2==0:
    soma

  print(soma)

  if n == 0:
    break

'''
import math

while answer.lower() != 's' and answer.lower() != 'y':

    soma = 0
    while n == 0:

        n= int(input('Digite um número: '))

        if n%2==0:
            soma

        print(soma)

    answer = input('Deseja continuar (S/N ou Y/N)? ')
