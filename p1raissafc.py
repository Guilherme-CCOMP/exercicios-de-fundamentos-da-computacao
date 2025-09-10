'''
1. (3,0) Em uma competição de programação, 20 estudantes participaram. Cada estudante tem um número de identificação, um total de problemas resolvidos eo tempo total gasto (em minutos). Crie um algoritmo em Python que:

a. Exiba o número de identificação do estudante que resolveu mais problemas.

b. Exiba o número de identificação do estudante mais eficiente, ou seja, aquele com maior razão de problemas resolvidos por minuto (eficiência problemas/tempo).

c. Se houver empate no número de problemas resolvidos ou na eficiência, qual número de identificação será exibido? Justifique sua resposta com base na sua lógica implementada.

2. (2,0) Escreva um algoritmo em Python que peça dois números inteiros (a e b) ao usuário. O algoritmo deve contar e exibir a quantidade de números entre 1 e 100 (inclusive) que são divisíveis por ambos a e b. Utilize apenas estruturas de repetição e decisão para resolver o problema.

number_a = int(input("Digite um número entre 1 e 100: "))
number_b = int(input("Digite um número entre 1 e 100: "))
divisors = []

for i in range(1, 101):
    if i % number_a == 0 and i % number_b == 0:
        divisors.append(i)

print("Quantidade de divisores: ", len(divisors))

3. (2,0) Escreva um algoritmo em Python que leia uma palavra fornecida pelo usuário. Em seguida, o programa deve exibir o primeiro e o último caractere dessa palavra e, por fim, concatenar o primeiro com o último caractere, exibindo a palavra resultante.



4. (2,0) Escreva um algoritmo em Python que solicite ao usuário que insira uma palavra. O programa deve contar quantas letras minúsculas existem na palavra e exibir essa contagem. Obedeça às seguintes regras:

a. A contagem deve considerar apenas letras minúsculas do alfabeto ('a' a 'z').
b. Não é permitido o uso de count().

    word = input('Digite uma palavra: ')
    minusculas = 0
    maiusculas = 0

    for i in word:
        if i.islower():
            minusculas += 1
        else:
            maiusculas += 1

    print(f'Há {minusculas} letras minúsculas e {maiusculas} maiúscula.')

5. (1,0) Escreva um programa em Python que imprima todos os números múltiplos de 5 entre 1 e 105.

for i in range(1, 106):
    calculo = i * 5
    print(calculo)



'''
while True:

    numbers = [abs(int(i)) for i in input("Digite um número entre 1 e 100: ").split(',')]
    divisors = []
    undivisors = []

    for i in numbers:
        for j in range(1, 101):
            if i % j == 0:
                divisors.append(i)
            else:
                undivisors.append(i)

    print(f"Divisores conjuntos de {numbers}: {divisors}.")
    print("Quantidade de divisores: ", len(divisors))
    #print("Não divisores: ", undivisors)
    #print("Quantidade de não divisores: ", len(undivisors))

    answer = input('Deseja continuar (sim para continuar/yes for continue)')
    if answer.lower()[0] != 's' or 'y':
        break
