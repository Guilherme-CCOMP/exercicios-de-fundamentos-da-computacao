'''
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
print('Hello World!')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome = input()
idade = int(input())
print(idade - 2)
print(nome)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome = input()
nome = 'Dra. ' + nome
idade = int(input())
salario = float(input())
print(nome, idade + 1, salario * 4)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome = input()
atributo = input()
acao = input()
print('Um '+nome+' tem '+atributo+' e pode '+acao)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome = input()
atributo1 = input()
atributo2 = input()
acao = input()
print(nome +' '+ acao +' '+ atributo1 +' '+ atributo2)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
refrao = input()
refresh = input()
saida = '{0}\n{0}\n{0}{1}'.format(refrao, refresh)

print(saida)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
# Operadores Lógicos:

x = int(input())
y = int(input())

# Existem estes três: "not"; "and"; "or". Eles funcionam de acordo com a Lógica Booleana {!não me pergunte sua história; pesquise.} ou Boolean Logic, ou seja/isto é, respondem|retornam "True" ou "False" => "Sim" ou "Não".

print(x + y)
print(x - y)
print(y - x)
print(x * y)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# Operadores de Comparação:

print(5 > 2)
print(5 < 2)
print(5 == 2)
print(5 != 2)
print(5 >= 2)
print(5 <= 2)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# Operadores de Atribuição

print(x = 1)
print(x += 1)
print(x -= 1)
print(x *= 1)
print(x /= 1)
print(x %= 1)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# Operadores Aritiméticos:

print(5 + 2)

print(5 - 2)

print(5 * 2)

print(5 / 2)

print(5 ** 2)

print(5 // 2)

print(5 % 2)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
valor1 = int(input())
valor2 = int(input())
print('.\n.\n.')

print(valor1, '+', valor2)
valor1 = valor1 + valor2
print(valor1)

print(valor1, '+=', valor2)
valor1 += valor2
print(valor1)

print(valor1, '-=', valor2)
valor1 -= valor2
print(valor1)

print(valor1, '*=', valor2)
valor1 *= valor2
print(valor1)

print(valor1, '/=', valor2)
valor1 /= valor2
print(valor1)

print(valor1, '//=', valor2)
valor1 //= valor2
print(valor1)

print(valor1, '**=', valor2)
valor1 **= valor2
print(valor1)

print(valor1, '%=', valor2)
valor1 %= valor2
print(valor1)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
numero = int(input())
if numero % 2 == 0:
  print('S')
else:
  print('N')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
x = int(input())
y = int(input())
if x % y == 0:
  print(str(x)+' é múltiplo de '+str(y))
else:
  print('tente de novo')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/

# Cadê a entrada?! Deve ter sido uma tentativa; rodará?

if idade > 60:
  print('Melhor idade!')
  print('Tchau!')
elif idade == 60:
  print('Melhor idade!')
  print('Tchau!')
else:
  print('Tchau!')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
numero = int(input())
numero = numero % 10000
milhar = numero // 1000
numero = numero % 1000
centena = numero // 100
numero = numero % 100
dezena = numero // 10
unidade = numero % 10
print(unidade)
print(dezena * 10 + unidade)
print(centena * 100 + dezena * 10 + unidade)
print(milhar * 1000 + centena * 100 + dezena * 10 + unidade)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
numero = int(input())

if numero >= 60:
  print(numero)
  print('Melhor idade!')

print('Tchau!')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
idade = int(input())

if idade >= 60:
  print('Gratis')
else:
  print('Pago')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
idade = int(input())

if idade >= 60:
  print('Gratis')
elif idade < 6:
  print('Gratis no colo')
else:
  print('Pago')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
a = int(input('Digite o coeficiente a: '))
b = int(input('Digite o coeficiente b: '))
c = int(input('Digite o coeficiente c: '))

delta = b**2 - 4*a*c
baskara = (-b + delta**0.5) / (2*a)
baskara2 = (-b - delta**0.5) / (2*a)
verticex = -b / (2*a)
vericey = -delta / (4*a)

if delta == 0:
  print(1)
elif delta > 0:
  print(2)
else:
  print(0)
# São duas formas de fazer o mesmo exercício?
a = int(input())
b = int(input())
c = int(input())
print(2*a*10**2 + 2*b*10**1 + 2*c*10**0)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
letra = input()
if letra == 'w' or letra == 'W':
  print('UP')
elif letra == 's' or letra == 'S':
  print('DOWN')
elif letra == 'a' or letra == 'A':
  print('LEFT')
elif letra == 'd' or letra == 'D':
  print('RIGHT')
else:
  print('?')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
face1 = input()
face2 = input()
face3 = input()
face4 = input()
face5 = input()
face6 = input()
if face1 == 'P' and face2 == 'P' and face3 == 'P' and face4 == 'P' and face5 == 'P' and face6 == 'P':
  print('Sena!')
else:
  print('Jogue de novo...')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
lado1 = input()
lado2 = input()
lado3 = input()
lado4 = input()

letra = input()

logica1 = lado1 == 'E' and lado2 == 'B' and lado3 == 'L' and lado4 == 'R' and letra == 'w'
logica2 = lado1 == 'T' and lado2 == 'E' and lado3 == 'L' and lado4 == 'R' and letra == 's'
logica3 = lado1 == 'T' and lado2 == 'B' and lado3 == 'E' and lado4 == 'R' and letra == 'a'
logica4 = lado1 == 'T' and lado2 == 'B' and lado3 == 'L' and lado4 == 'E' and letra == 'd'

if logica1 or logica2 or logica3 or logica4:
  print('yes!')
else:
  print('next player...')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
jogadora1 = int(input())
jogadora2 = int(input())
jogadora3 = int(input())
jogadora4 = int(input())

dupla1 = dupla2 = 0

if jogadora1 > jogadora3:
  dupla1 = jogadora1
else:
  dupla1 = jogadora3
if jogadora2 > jogadora4:
  dupla2 = jogadora2
else:
  dupla2 = jogadora4
if dupla1 > dupla2:
  print(dupla1)
elif dupla2 > dupla1:
  print(dupla2)
else:
  print('empate')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
valor1 = int(input())
valor2 = int(input())
operador = input()

if operador == '+':
  print(valor1 + valor2)
if operador == '-':
  print(valor1 - valor2)
if operador == '/':
  print(valor1 / valor2)
if operador == '*':
  print(valor1 * valor2)
if operador == '//':
  print(valor1 // valor2)
if operador == '%':
  print(valor1 % valor2)
if operador == '**':
  print(valor1 ** valor2)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
time1 = int(input())
time2 = int(input())
if (time1 == 25 or time2 == 25) and (time1 - time2 >= 2 or time2 - time1 >= 2):
  print('S')
else:
  print('N')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
time1 = input()
time2 = input()
placar1 = int(input())
placar2 = int(input())
print(time1 +' '+ str(placar1))
print(time2 +' '+ str(placar2))
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
.alnum()
.append()
.capitalize()
.clear()
.copy()
.count()
.digit()
.endswith()
.extend()
.find()
.format()
.index()
.insert()
.is_____()
.len()
.lower()
.pop()
.remove()
.replace()
.reverse()
.sort()
.startswith()
.title()
.type()
.upper()
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
string = input()
palavra1 = input()
palavra2 = input()

print(string)

print(string.title())
print(string.upper())
print(string.lower())

print(string.index(palavra1))
print(string.find(palavra1))
print(string.count(palavra2))
print(string.replace(palavra1, palavra2))

print(string.istitle())
print(string.isupper())
print(string.islower())
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
from math import sqrt

x = input()
y = float(input())
template = '{:.2f}'
numero = sqrt(float(x))
saidax = template.format(numero)
print(saidax)
numero = sqrt(y)
saiday = template.format(numero)
print(saiday)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome1 = input()
nome2 = input()
nome3 = input()
nomes = [nome1, nome2, nome3]
for nome1 in nomes:
  for nome2 in nomes:
    if nome1 != nome2:
      print(nome1+nome2)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
t = [int(i) for i in input().split()]

for i in t:
  l = ''
  if i % 2 == 0:
    for j in range(i):
      l += '*'
    print(l)
  else:
    for j in range(i):
      l += '.'
    print(l)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
information = input()

Título = information.title()
Baixa = information.lower()
Alta = information.upper()

print(Título)
print(Baixa)
print(Alta)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
valor = float(input())
saida = 'Valor: {:.3} \n Valor ao quadrado: {:.3}'.format(valor, valor ** 2)
print(saida)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
fbanco = []
valor = input()
fbanco.insert(0,valor)
valor = input()
fbanco.append(valor)
valor = input()
fbanco.insert(2,valor)
valor = input()
fbanco.append(valor)
print(fbanco)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
lista = list(range(3))
print(lista)
lista = list(range(6))
print(lista)
lista = list(range(9))
print(lista)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
vagas = int(input())
todas = ''

while vagas > 0:
  nome = input()
  if nome == 'especial':
    break
  todas += nome + ' '
  vagas -= 1
else:
  print(todas)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
textoProcurado = input()
textao = input()
ocorrencias = 0

while textao != 'fim':
  ocorrencias = ocorrencias + textao.count(textoProcurado)
  textao = input()
print(ocorrencias)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
Quando = int(input())
Onde = int(input())
Como = int(input())
range(Quando, Onde, Como)
ruby = range(Quando, Onde, Como)
for i in ruby:
  print(i)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
valor = int(input())
for i in range(valor):
  if i % 2 == 0:
    print(i)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
valor = int(input())
soma = 0
for i in range(valor + 1):
  if i % 3 == 0:
    soma = soma + i
print(soma)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
valor1 = int(input())
valor2 = int(input())

soma = 0

for i in range(valor2):
  if i % valor1 == 0:
    soma = soma + i
print(soma)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
template = '{:.2f}'

valor1 = int(input())
valor2 = int(input())

print(valor1 + valor2)
print(valor1 - valor2)
print(valor1 * valor2)
print(template.format(valor1 / valor2))
print(valor1 % valor2)
print(valor1 // valor2)
print(valor1 ** valor2)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
textão = input()
textos = []

while textão != 'F':
  textos.append(textão)
  textão = input()

for texto in textos:
  print(texto)
print('fim')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
palavra = input()

lista = enumerate(palavra)

print(len(palavra))

for indice, letra in lista:
  print(indice, letra)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
T1 = input()
T2 = input()

set1 = [int(i) for i in input().split()]
set2 = [int(i) for i in input().split()]

numsets = len(set2)

SetesTime1 = 0
SetesTime2 = 0

for i in range (numsets):
  if(set1[i] > set2[i]):
    SetesTime1 = SetesTime1 + 1
  else:
    SetesTime2 = SetesTime2 + 1

if SetesTime1 > SetesTime2:
  print(T1,'(total {} sets)'.format(numsets))
elif SetesTime2 > SetesTime1:
  print(T2,'(total {} sets)'.format(numsets))
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
Nome_do_Jogador = input()
lista = input().split()
palavra = 'ok'
for textoDaLista in lista:
  if textoDaLista == 'mico':
    palavra = 'mico!'
print(Nome_do_Jogador,palavra)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
letra = input()

if letra == 'f':
  frequencia = [int(i) for i in input().split()]
  print(frequencia)
elif letra == 'n':
  notas =  [float(i) for i in input().split()]
  print(notas)
elif letra == 's':
  sobrenome = [str(i) for i in input().split()]
  print(sobrenome)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
linha1 = [int(i) for i in input().split()]
linha2 = [int(i) for i in input().split()]
linha3 = [int(i) for i in input().split()]
# dado = [linha1,linha2,linha3]
soma = 0
for i in linha1:
  soma = soma+i
for i in linha2:
  soma = soma+i
for i in linha3:
  soma = soma+i
# eduardo = range(3)
# for i in range(3):
#   soma = soma + linha1[i] + linha2[i] + linha3[i]
# for linhas in dado:
#   for valor in linhas:
#     soma = soma + valor
print(soma)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
linha1 = [int(i) for i in input().split()]
linha2 = [int(i) for i in input().split()]
linha3 = [int(i) for i in input().split()]

linha4 = [int(i) for i in input().split()]
linha5 = [int(i) for i in input().split()]
linha6 = [int(i) for i in input().split()]

dado1 = [linha1,linha2,linha3]
dado2 = [linha4,linha5,linha6]

jogador = 0
jogadora = 0

for linhas in dado1:
  for valor in linhas:
    jogador = jogador + valor

for linhas in dado2:
  for valor in linhas:
    jogadora = jogadora + valor

if jogador > jogadora:
  print(1)
elif jogador < jogadora:
  print(2)
elif jogador == jogadora:
  print('E')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
textao = input()
empty = []
# soma = 0

while textao != 'the end':
  if textao != '':
    #empty.adicionar(textao)
    empty.append(textao)
  textao = input()
# for i in range(len(empty)):
#   if i != 0:
#     soma = soma + empty[i].count(empty[0])
print(len(empty))

lista = [int(i) for i in input().split()]
for i in range(10):
  print(i, lista.count(i))
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
tito = [int(i) for i in input().split()]

menor = min(tito)
maior = max(tito)

x_Mônicos = range(menor,maior+1)
for linkedin in x_Mônicos:
  print(linkedin, tito.count(linkedin))
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
lista = [int(i) for i in input().split()]

lista.sort()

listaUnica = []
soma = 0
for n in lista:
  soma = soma +n
  if listaUnica.count(n) == 0:
    listaUnica.append(n)
for n in listaUnica:
  print(n,lista.count(n))
print(soma)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
time1 = input()
time2 = input()
pontuacao = [int(i) for i in input().split()]
if pontuacao[2] == 1:
  print(time1, pontuacao[0]+1)
  print(time2, pontuacao[1])
else:
  print(time1, pontuacao[0])
  print(time2, pontuacao[1]+1)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
time1 = input()
time2 = input()
placar = input()

if placar == '0':
  print('Início do set')
  print(time1, 0)
  print(time2, 0)
else:
  print(time1, placar.count('1'))
  print(time2, placar.count('2'))
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome = input()
letras = []
for letra in nome:
  if letras.count(letra.upper()) == 0 and letra != ' ':
    letras.append(letra.upper())
letras.sort()
for letra in letras:
  print(letra, nome.count(letra.lower()))
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
equipe = input()
lista_de_nomes = []
while equipe != '.':
  lista_de_nomes.append(equipe)
  equipe = input()
lista_de_nomes.sort(key = str.lower)
print(lista_de_nomes)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
notas = [float(i) for i in input().split()]

notas.sort()
notas.reverse()
print(notas)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
word = input()
word_indexada = enumerate(word)
print(len(word))
for indice, letra in word_indexada:
  print(indice, letra)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome = input()
porcentagem = int(input())
notas = float(input())
if notas >= 5.0 and porcentagem >= 75:
  print(nome, 'aprovada: Parabéns!')
else:
  print(nome, 'não aprovada: inscreva-se na próxima turma!')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
palavra = input()
lista = input().split()
existe = False

for item in lista:
  if item == palavra:
    existe = True
if existe:
  print(palavra,lista.index(palavra));
else:
  print('falta',palavra)
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
entrada = [int(i) for i in input().split()]
minimo = min(entrada)
maximo = max(entrada)
lista = []
soma = 0
print(range(minimo, maximo))
for i in range(minimo, maximo+1):
  print(i, entrada.count(i))
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
linha1 = input()
procurados = input().split()

for palavra in procurados:
  if linha1.find(palavra) >= 0:
    print(palavra, linha1.find(palavra))

procurados = input().split()
numero_de_linhas = int(input())
matriz = []

for i in range(numero_de_linhas):
  linhas = input().split()
  matriz.append(linhas)

for procurado in procurados:
  for lista in matriz:
    for palavra in lista:
      if palavra == procurado:
        print(procurado,matriz.index(lista), lista.index(procurado))
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
vacina =int(input())
if vacina ==2:
  print('falta a terceira dose')
elif vacina ==3:
  print('parabéns, você tomou as três doses!')
else:
  print('faltam a segunda e a terceira')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome = [int(i) for i in input().split()]
nome = [int(i) for i in input().split()]
procurar = int(input())

for entrada in nome:
  if entrada != procurar:
   print(entrada)
  else:
    print(True)

matrix =[]
for i in range(3):
  linha =input().split()
  matrix.append(linha)
vencedor = ''
colunas= [[],[],[]]
for linhas in matrix:
  linha = ''
  for j in range(3):
    linha = linha + linhas[j];
    colunas[j].append(linhas[j])
    if linha == 'OOO':
      vencedor = 'O'
    elif linha == 'XXX':
      vencedor = 'X'

for coluna in colunas:
  colunaT = ''
  for j in range(3):
    colunaT = colunaT + coluna[j]
    if colunaT == 'OOO':
      vencedor = 'O'
    elif colunaT == 'XXX':
      vencedor = 'X'
linha1 = matrix[0][0] + matrix[0][1] + matrix[0][2]
linha2 = matrix[1][0] + matrix[1][1] + matrix[1][2]
linha3 = matrix[2][0] + matrix[2][1] + matrix[2][2]
coluna1 = matrix[0][0] + matrix[1][0] + matrix[2][0]
coluna2 = matrix[0][1] + matrix[1][1] + matrix[2][1]
coluna3 = matrix[0][2] + matrix[1][2] + matrix[2][2]
diagonal1 = matrix[0][0] + matrix[1][1] + matrix[2][2]
diagonal2 = matrix[0][2] + matrix[1][1] + matrix[2][0]
if diagonal1 == 'OOO' or diagonal2 == 'OOO':
  vencedor = 'O'
if diagonal1 == 'XXX' or diagonal2 == 'XXX':
  vencedor = 'X'
if vencedor == 'X' or vencedor =='O':
  print(vencedor)
else:
  print('next!')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
nome = input()
numdeaulas = int(input())
tarefas1 = int(input())
tarefas2 = int(input())
tarefas3 = int(input())
frequencia1 = int(input())
frequencia2 = int(input())
frequencia3 = int(input())
nota = float(input())
if numdeaulas >= 3 and tarefas1 >= 75 and tarefas2 >= 75 and tarefas3 >= 75 and frequencia1 == 1 and frequencia2 == 1 and frequencia3 == 1 and nota >= 5.0:
  print(nome,'aprovada')
else:
  print(nome,'reprovada')
'''
# numeros= [int(i) for i in input().split()]

# for numero in numeros:
#   if numero %3==0:

#     print(numero)
#   else:
#     print(numeros.index(numero),'resto',numero%3)
# nomes= input().split()
# print(nomes)
# for i in nomes:
#   print(len(i))

# documento, comprovante, nome =input().split()
# documento =int(documento)
# comprovante =int(comprovante)
# if documento ==1 and comprovante ==1:
#   print('vamos analisar')
# else:
#   print('indeferida')
# candidatas =int(input())
# positiva =0
# negativa =0
# for i in range(candidatas):
#   nome=input()
#   if nome[0] == '+':
#     positiva = positiva+1
#   elif nome[0] == '-':
#     negativa = negativa+1
# print(negativa,'indeferidas por falta de documentação')
# print(positiva,'analisar documentação e priorizar')
# nomes =input().split()
# conjucoes=input().split()
# verbos =input().split()
# for nome in nomes:
#   for conjucao in conjucoes:
#     for verbo in verbos:
#       print(nome,conjucao,verbo)
# aluna =int(input())
# soma_tarefa=0
# soma_prova=0
# for i in range(aluna):
#   tarefa, prova =input().split()
#   tarefa = int(tarefa)
#   prova = float(prova)
#   soma_tarefa=soma_tarefa+tarefa
#   soma_prova=soma_prova+prova
# print(soma_tarefa/aluna)
# print(soma_prova/aluna)
#lista_pratos=input().split()
#pratos_limpo=lista_pratos.count('L')
#lista=[]
#for prato in lista_pratos:
  #if prato !='L':
   # lista.append(prato)
#lista.reverse()

#restante = len(lista) - pratos_limpo
#for i in range(restante):
 # print(lista[i])

#print(restante)
"""
time1 =input()
time2 =input()
pontos = input()
total = []
while pontos != 'fim':
  total.append(pontos)
  pontos = input()

# imprimir {nome do time}, {"pontos set1" "pontos set2" ...} ({Total de pontos})
saida_time1 = ''
saida_time2 = ''
total1= 0
total2= 0
idx = len(total) - 1
i = 0
for ponto in total:
  pontos_time_1 = ponto.count('1')
  pontos_time_2 = ponto.count('2')
  total1 += pontos_time_1
  total2 += pontos_time_2
  if idx != i:
    saida_time1 += str(pontos_time_1) + ' '
    saida_time2 +=str(pontos_time_2) + ' '
  else:
    saida_time1 += str(pontos_time_1)
    saida_time2 +=str(pontos_time_2)
  i+=1

print(time1, saida_time1,'(',total1,')')
print(time2, saida_time2,'(',total2,')')
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
time1=0
time2=0
max = 25
pegar_pontos= True

while pegar_pontos:
  time1_nao_venceu = True
  time2_nao_venceu = True
  numero=input()
  if numero == '1':
    time1 +=1
  elif numero == '2':
    time2 +=1
  diferenca = abs(time1 -time2)
  if time1 >= max and time1>time2 and diferenca > 1:
    time1_nao_venceu = False
  if time2 >= max and time2>time1 and diferenca > 1:
    time2_nao_venceu = False
  # time1_nao_venceu = time1 < max or diferenca == 1
  # time2_nao_venceu = time2 < max or diferenca == 1
  pegar_pontos =  (time1_nao_venceu and time2_nao_venceu)
print(time1,'X',time2)
"""

palavra = input()
lista = [palavra(i) for i in input().append()]
while palavra != '.':
  letra = input()
  letra.append(lista)

if letra == palavra:
  print(True)
else:
  print(False)
