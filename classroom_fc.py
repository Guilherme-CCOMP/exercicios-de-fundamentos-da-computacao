'''
Exercícios de hoje 08/09:
# 1)
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

'''

while True:

    num_neutro = 0
    for i in range(1, 6):
        n = [list(int(input('Digite um número: ')))]
    for i in n:
        if i > num_neutro:
            num_maior = i
        elif i < num_neutro:
            num_menor = i
        if num_maior < num_menor:
            num_menor, num_maior = num_maior, num_menor
        

    print(f'Maior: {num_maior}; Menor: {num_menor}.')

    resposta = input('\nDeseja continuar? ')
    if resposta.lower != 's' or resposta.lower != 's':
        break
