"""
Exercícios - Loops for/while com break e range

----------------------------------------------------------------

# Exercicio 1:
# Usando um for, imprima os números de 1 a 10

for numero in range(1,11):
    print(numero)

----------------------------------------------------------------

# Exercicio 2:
#Usando um while, imprima os números de 1 a 10.

numero = 1

while numero <=10:
    print(numero)
    numero = numero + 1

----------------------------------------------------------------

#Exercicio 3:

#Imprima todos os números pares de 0 a 20 usando for e range.

for numero in range(0,21,2):
    print(numero)

----------------------------------------------------------------

#Exercicio 4:
#Imprima todos os números ímpares de 1 a 20 usando while.

numero = 1
while numero < 20:
    print(numero)
    numero = numero + 2

----------------------------------------------------------------

#Exercicio 5:
#Peça ao usuário um número e imprima a tabuada desse número (1 a 10) usando for.

valor = int(input('Digite um número para ver a tabuada: '))

for numero in range(1,11):
    resultado = valor * numero
    print(f'{valor} x {numero} = {resultado}')

----------------------------------------------------------------

#Exercicio 6: 
#Use um for para somar todos os números de 1 a 100 e mostre o resultado.


soma = 0

for num in range(1,101):
    soma = soma + num
    print(soma)

----------------------------------------------------------------

#Exercicio 7:
#Peça ao usuário vários números usando while. 
#O programa deve parar quando o usuário digitar 0 e mostrar a soma dos números digitados.

soma = 0
numero = int(input('Digite um número (Digite 0 para parar): '))
while numero != 0:  
    soma = soma + numero
    numero = int(input('Digite um número (Digite 0 para parar): '))
print(f'A soma de todos os numeros é -> {soma}')

----------------------------------------------------------------

#Exercicio 8:

#Imprima os números de 10 até 1, em ordem decrescente, usando for.

for numero in range(10,0,-1):
    print(numero)

----------------------------------------------------------------

#Exercicio 9:
#Use for e range para imprimir os números de 0 a 50, mas interrompa o loop quando o número for 25.

for numero in range(0,51):
    if numero == 25:
        break
    print(numero)

----------------------------------------------------------------

#Exercicio 10:
#Peça ao usuário um número e verifique se ele é primo (use for).

numero = int(input('Digite um número para verificar se é primo: '))

if numero <= 1:
    print('O numero não é primo.')
else:
    for i in range(2, numero):
        if numero % i == 0:
            print('O número não é primo.')
            break
    else:
        print('O número é primo.')

----------------------------------------------------------------

#Exercicio 11:

#Crie um programa que peça números ao usuário indefinidamente.
#Quando o usuário digitar um número negativo, o programa deve parar usando break.


numero = int(input('Digite um número (Digite 0 para parar): '))
while numero >= 0:  
         numero = int(input('Digite um número (Digite 0 para parar): '))
print('Programa encerrado por número negativo.')

#Versão com break

while True:
        numero = int(input('Digite um número (Digite um número negativo para parar): '))
        if numero < 0:
                break
print('Programa encerrado por número negativo.')

----------------------------------------------------------------

#Exercicio 12:
#Use um for para percorrer números de 1 a 100.
#Quando encontrar o primeiro múltiplo de 7, pare o loop com break.

for numero in range(1,100):
    if numero % 7 == 0:
        print(f'Primeiro múltiplo de 7 é {numero}')
        break
        
----------------------------------------------------------------

#Exercicio 13:
#Peça ao usuário para digitar uma senha. Use um loop while para continuar pedindo a senha até que o usuário digite a senha correta (por exemplo, "python123").

tentativa = 0
senha = 1234
acertou = False

while tentativa < 3:
    senha1 = int(input('Digite a senha: '))
    if senha1 == senha:
        acertou = True
        break
    else:
        tentativa = tentativa + 1
if acertou:
    print('Senha correta! Acesso permitido.')
else:
    print('Numero maximo de tentativas atingida')

----------------------------------------------------------------
"""

#Exercicio 14:
#Peça ao usuário um número e mostre todos os divisores desse número usando for.


#Exercicio 15:
#Peça ao usuário um número e calcule o fatorial dele usando while.

#Exercicio 16:
#Use for para imprimir o seguinte padrão:
#*
#**
#***
#****
#*****

#Exercicio 17:
#Use dois loops (for dentro de for) para imprimir a tabuada de 1 a 5.

#Exercicio 18:
#Peça números ao usuário até que ele digite "sair".
#No final, mostre quantos números foram digitados.

#Exercicio 19:
#Crie um jogo de adivinhação:

#O número secreto é 7

#O usuário tenta adivinhar

#O programa só para quando ele acertar (use while e break)

#Exercicio 20:
#Peça um número ao usuário e mostre a sequência de Fibonacci até esse número usando for.


    

