#Lista III – Estrutura de Dados

#1. Desenvolva um programa que receba do usuário uma lista com 5 números inteiros e substitua todos os valores negativos por zero.

numeros = []
for i in range(5):
  numeros.append(int(input("Digite o número: ")))

for i in range(len(numeros)):
  if numeros[i] < 0:
    numeros[i] = 0
print(numeros)

#2. Desenvolva um programa que receba do usuário uma lista com 5 números inteiros e retorne a soma dos valores positivos e a quantidade de valores negativos na lista.

cont = 0
media = 0
numeros = []
for i in range(5):
  numeros.append(int(input("Digite o número: ")))
for i in range(len(numeros)):
  if numeros[i] < 0:
    cont += 1
  if numeros[i] > 0:
    media += numeros[i]
print("A quantidade de negativos é de: ",cont," e a soma dos positivos foi de ",media)

#3. Elabore um programa que receba do usuário duas listas de 6 posições cada, representando duas notas parciais de um aluno em diferentes disciplinas. O programa deve calcular a média das notas para cada disciplina e informar qual disciplina teve a maior média.

nomes = []
notas = []
notas1 = []
soma = []
for i in range(6):
  nomes.append(input("Digite o nome da matéria: "))
  notas.append(float(input("Digite a primeira nota de "+nomes[i]+": ")))
  notas1.append(float(input("Digite a segunda nota de "+nomes[i]+": ")))
  soma.append(float((notas[i]+notas1[i])/2))

print("Nomes das matérias: ", nomes)
print("Médias das matérias: ", soma)

numero = soma[0]
materia = nomes[0]

for i in range(len(soma)):
  if (soma[i] > numero):
    numero = soma[i]
    materia = nomes[i]

print("A média mais alta foi de",numero,"na matéria de",materia)

#4. Faça um programa que solicite ao usuário que insira uma lista com 4 números inteiros. O programa deve imprimir os valores em ordem crescente.

numeros = []
print("Escreva 4 números inteiros!")
for i in range(4):
  numeros.append(int(input("Digite os números: ")))

for i in range(len(numeros)):
  for j in range(i+1, len(numeros)):
    if numeros[i] >= numeros[j]:
      numeros[i], numeros[j] = numeros[j], numeros[i]

print(numeros)



#5. Faça um programa que leia uma matriz 3x3 de números inteiros e verifique se todos os elementos são pares.

matriz = [[1, 2, 2], [4, 6, 2], [8, 4, 2]]
for i in matriz:
  for j in i:
    if j % 2 != 0:
      print("Tem um número impar")
      break
    else:
      print("Tem um número par!")

#6. Desenvolva um programa que receba do usuário uma matriz 3x3 representando os resultados de três avaliações para três alunos. O programa deve calcular a média de cada aluno e determinar qual aluno obteve a maior média.

notas = []
for i in range(3):
  notas_aluno = []
  for j in range(3):
    nota = float(input("Digite a nota do aluno: "))
    notas_aluno.append(nota)
  notas.append(notas_aluno)

medias = []
for aluno in notas:
  soma = 0
  for nota in aluno:
    soma += nota
    media_aluno = soma /len(aluno)
    medias.append(media_aluno)

maior_media = medias[0]
indice_maior_media = 0

for i in range(1, len(medias)):
  if medias[i] > maior_media:
    maior_media = medias[i]
    indice_maior_media = i

print("O aluno que obteve a maior média foi de: ",maior_media,"pontos")

#7. Elabore um programa que receba do usuário uma matriz 5x5 de números inteiros. O programa deve verificar se existe algum número repetido na matriz e informar a posição e o valor do primeiro número repetido encontrado.

numeros = []
for i in range(5):
  for j in range(5):
    numero = int(input("Digite os números: "))
    numeros.append(numero)

repeticao = 0

repetidos = False
for i in range(len(numeros)):
  for j in range(i+1, len(numeros)):
    if numeros[i] == numeros[j]:
      repetidos = True
      repeticao += 1
      break

if repetidos:
  print("Tem um",repeticao,"repetição(ções)")
else:
  print("Não tem nenhum número repetido")

#8. Escreva um programa que leia uma matriz 3x3 de números inteiros. O programa deve calcular e exibir a soma dos elementos presentes na diagonal principal.

numeros = []
for i in range(3):
  linha = []
  for j in range(3):
    numero = int(input("Digite os números: "))
    linha.append(numero)
  numeros.append(linha)

soma_diagonal = 0
for i in range(3):
  soma_diagonal += numeros[i][j]

print(soma_diagonal)

#9. Faça uma função que receba um número inteiro como argumento e retorne True se o número for par e False se for ímpar.

numero = int(input("Digite um número inteiro: "))

impar = False
par = True

if numero % 2 == 0:
  par = True
  print("O número é par! Logo ele é",par)
else:
  impar = False
  print("O número é ímpar! Logo ele é",impar)

#10.Desenvolva uma função que receba uma lista de palavras como entrada e retorne a quantidade de palavras que começam com a letra 'A'.

palavras = []
lista = 3
for i in range(lista):
  palavras.append(str(input("Digite a palavra: ")))

cont = 0
for palavra in palavras:
  if palavra[0] == "A":
    cont += 1
print(cont)

#11.Elabore uma função que receba uma lista de palavras como parâmetro e retorne uma lista contendo apenas as palavras que possuem mais de três caracteres.


palavras = []
for i in range(3):
  palavras.append(str(input("Digite a palavra: ")))

palavras_caracteres = []
cont = 0

for palavra in palavras:
  if len(palavra) > 3:
    palavras_caracteres.append(palavra)
    cont += 1

print("A quantia de palavra foi de",cont)
print("Sendo elas:",palavras_caracteres)




#12.Desenvolva uma função que aceite duas listas como parâmetros e retorne uma nova lista contendo apenas os elementos comuns entre as duas listas.

palavras = []
palavras1 = []
for i in range(2):
  palavras.append(str(input("Digite a palavra da primeira lista: ")))

palavras1 = []
for j in range(2):
  palavras1.append(str(input("Digite a palavra da segunda lista: ")))

palavras_semelhantes = []
repeticao = 0

for i in range(len(palavras)):
  for j in range(len(palavras1)):
    if palavras[i] == palavras1[j]:
      palavras_semelhantes.append(palavras[i])
      repeticao += 1
      break

print(repeticao, palavras_semelhantes)