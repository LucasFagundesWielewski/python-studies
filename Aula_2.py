#Lista II – Estrutura de dados

#1. Escreva um programa que, por meio de um loop, gere a tabuada de multiplicação de um número escolhido pelo usuário até 10.

print("Programa de Tábuada")
numero = int(input("Escolha um número: "))
for tabuada in range(1,10+1):
  multiplicacao = tabuada * numero
  print(multiplicacao)

#2. Escreva um programa que receba números do usuário até que seja digitado um número negativo. Ao final, imprima a soma e a média dos números positivos inseridos.

print("Média dos números")
soma = 0
contador = 0
num = int(input("Digite um número: "))
while (num >= 0):
  soma = soma + num
  contador = contador + 1
  num = int(input("Digite um número: "))
print("A soma de todos os números é de: ", soma)
media = soma/contador
print("A média é de: ",media)
print("Final")


#3. Crie um programa que simule uma máquina de venda automática. O usuário deve inserir dinheiro até atingir o valor necessário para comprar um item. Após cada inserção, informe quanto falta para atingir o valor total.

print("Máquina de venda automática")
valorFinal = 100
num = float(input("Digite um valor: "))
soma = 0
distancia = 0
troco = 0
while (valorFinal > soma):
  soma = soma + num
  if (soma < valorFinal):
    distancia = valorFinal - soma
  print("Falta", distancia)
  troco = soma - valorFinal
  num = int(input("Digite um valor: "))
print("Você terá R$ ",troco," de troco")
print("Final")

#4. Desenvolva um programa que simule o lançamento de um dado 20 vezes. Conte e imprima a quantidade de vezes que cada número de 1 a 6 foi obtido.

from random import randint
roladas = 20
contador = 0
numero1 = 0
numero2 = 0
numero3 = 0
numero4 = 0
numero5 = 0
numero6 = 0
for contador in range(roladas):
  numero_sorteado = randint(1,6)
  print(numero_sorteado)
  if numero_sorteado == 1:
    numero1 += 1
  elif numero_sorteado == 2:
    numero2 += 1
  elif numero_sorteado == 3:
    numero3 += 1
  elif numero_sorteado == 4:
    numero4 += 1
  elif numero_sorteado == 5:
    numero5 += 1
  elif numero_sorteado == 6:
    numero6 += 1
print("O número 1 foi sorteado ",numero1," vezes")
print("O número 2 foi sorteado ",numero2," vezes")
print("O número 3 foi sorteado ",numero3," vezes")
print("O número 4 foi sorteado ",numero4," vezes")
print("O número 5 foi sorteado ",numero5," vezes")
print("O número 6 foi sorteado ",numero6," vezes")
print("Final")

#5. Crie um programa que, utilizando um loop, solicite ao usuário que insira números até que a soma dos números inseridos seja maior que 100. Ao final, imprima a quantidade de números digitados.

valorFinal = 100
numero = float(input("Digite um valor: "))
soma = 0
distancia = 0
troco = 0
cont = 0
while (valorFinal > soma):
  soma = soma + numero
  if (soma < valorFinal):
    distancia = valorFinal - soma
  print("Falta", distancia)
  numero = float(input("Digite um valor: "))
  cont = cont + 1
print("O programa foi rodado: ",cont)
print("Final")

#6. Desenvolva um programa que receba uma palavra do usuário e utilize um loop for para contar e imprimir a quantidade de vogais na palavra.

palavra = input("Digite uma palavra: ")
cont = 0
i = 0
vogais = ["a","e","i","o","u","A","E","I","O","U"]
for i in range(len(palavra)):
  if palavra[i] in vogais:
    cont += 1
print(cont)

#7. Desenvolva um programa que, por meio de um loop, simule uma batalha entre dois personagens. Cada personagem possui pontos de vida (HP) e causam danos ao adversário. O programa deve determinar o vencedor com base nos pontos de vida restantes.

from random import randint

player1 = input("Digite o nome do jogador 1: ")
player2 = input("Digite o nome do jogador 2: ")
player1_life = 100;
player2_life = 100;

while player1_life > 0 and player2_life > 0:
  player1_attack = randint(1,25)
  player2_attack = randint(1,25)

  player1_life -= player2_attack
  player2_life -= player1_attack

  print("Dano de",player1 , player1_attack)
  print("Vida sobrando de:", player2 , player2_life)
  print("Dano de",player2 , player2_attack)
  print("Vida sobrando de:", player1 , player1_life)

if (player1_life > player2_life):
  print("O jogador(a):",player1,"Venceu!")
elif (player1_life > player2_life):
  print("O jogador(a):",player2,"Venceu!")
else:
  print("O jogo empatou")

print("Final")


#8. Escreva um programa que solicita ao usuário um número e verifica se ele é um número perfeito. Um número perfeito é aquele cuja soma de seus divisores (excluindo ele mesmo) é igual ao próprio número. Exemplo: 28 é um número perfeito (1 + 2 + 4 + 7 + 14 = 28).

numero = int(input("Digite um número inteiro positivo: "))
if numero <= 0:
  print("Por favor, digite um número inteiro positivo.")
else:
  soma_divisores = 0

for i in range(1, numero):
  if numero % i == 0:
    soma_divisores += i

if soma_divisores == numero:
  print(f"{numero} é um número perfeito!")
else:
  print(f"{numero} não é um número perfeito.")