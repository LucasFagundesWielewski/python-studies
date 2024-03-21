#*Lista I – Estrutura de dados *

# 1 - Desenvolva um programa que solicite ao usuário a quantidade de galões de combustível que deseja abastecer e converta esse valor para litros. Considere que 1 galão é aproximadamente 3,78541 litros. Imprima o resultado na tela.

print("Qual a quantidade de galões de combustível que deseja abastecer?")
combustivel = int(input("Digite a quantia de galões: "))
soma = combustivel * 3,78541
print("Você tem ", soma ," litros!")

# 2 -Crie um programa que receba três notas de um aluno e calcule a média ponderada. Considere que as notas têm pesos diferentes: a primeira nota tem peso 2, a segunda nota tem peso 3 e a terceira nota tem peso 5.

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
equacao = (nota1 * 0.2) + (nota2 * 0.3) + (nota3 * 0.5)
print(equacao)

# 3 - Desenvolva um programa que receba três números do usuário e determine qual é o maior deles.

numero1 = float(input("Digite o numero 1: "))
numero2 = float(input("Digite o numero 2: "))
numero3 = float(input("Digite o numero 3: "))
if numero1 > numero2 and numero1 > numero3:
  print("O número maior é o: ", numero1)
elif numero2 > numero1 and numero2 > numero3:
  print("O número maior é o: ", numero2)
elif numero3 > numero2 and numero3 > numero1:
  print("O número maior é o: ", numero3);
else:
  print("Valor inválido!")

# 4 - Escreva um programa que recebe como entrada o salário base de um funcionário e o número de horas extras trabalhadas. Calcule o salário total, considerando que cada hora extra é paga com um acréscimo de 50% sobre o valor da hora normal. Imprima o salário total na tela.

salario = float(input("Salário base de um funcionário: "))
extras = float(input("Horas extras: "))
soma = (salario + ((extras* (salario/190)) * 1.5))
print(soma)

# 5 - Desenvolva um programa que simula uma loja online. Solicite ao usuário o nome, o preço e a quantidade de um produto que ele deseja comprar. Calcule o valor total da compra e aplique um desconto de 10% se a quantidade comprada for maior que 10 unidades. Imprima o valor final a ser pago.

nome = input("Digite o seu nome: ")
preco = float(input("Digite o preço: "))
quantia = int(input("Digite a quantidade do produto: "))
if quantia > 10:
  soma = float( quantia * preco )
  desconto = (soma * 0.1)
  resultado = soma - desconto
  print("A compra de ",nome, "será de R$", resultado, "com o desconto de ", desconto )
else:
  soma = quantia * preco

# 6 - Faça um programa que simule uma calculadora de financiamento de veículos. Solicite ao usuário o valor do veículo, a quantidade de parcelas desejada e a taxa de juros mensal. Calcule e imprima o valor total a ser pago, considerando o financiamento.
  
valorDoVeiculo = float(input("Digite o valor do veículo: "))
quantidadeDeParcelas = float(input("Quantia de parcelas: "))
juroMensal = float(input("Digite a taxa de juros mensal: "))
valorParcelas = (valorDoVeiculo/quantidadeDeParcelas)
juros = (valorParcelas * (juroMensal / 100))
jurosFinais = valorDoVeiculo + (juros * quantidadeDeParcelas)
print("O valor final é de: ", jurosFinais)
