"""
- Loop for

O loop é uma estrutura de repetição.
E o for é uma dessas estruturas de repetição.

- Em C e Java, o loop for é exercutado da seguinte forma:

for ( int i =0; i < 10: i++){
    //Execução do loop
}

- Já em python, o loop for é executado da seguinte forma:

for item in interavel:
    //Execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

- O que é um valor iterável?
Valores iteráveis são aqueles que podem ser percorridos, ou seja, você pode iterar sobre eles.

- Exemplos de valores iteráveis em Python incluem listas, tuplas, dicionários, conjuntos e strings.

- string
    nome = 'Rafael Romao'

- Lista
    lista = [1, 3, 5, 7, 9]

- Range
    numeros = range(1, 10)

---------------------------------------------------

# Exemplo de for 1 (Iterando sobre uma string)

nome = 'Rafael Romao'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em uma Lista

for letra in nome:
    print(letra)
print('\n')

----------------------------------------------------

#Exemplo de for 2 (Iterando sobre uma lista)

nome = 'Rafael Romao'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for numero in lista:
    print(numero)
print('\n')

----------------------------------------------------

#Exemplo de for 3 (Iterando sobre um Range)
#range(valor_inicial, valor_final)
#obs: o valor_final não é inclusive, ou seja, se for range (1,10), é 1 até (10 -1), no caso, vai imprimir de 1 até o 9.


nome = 'Rafael Romao'
lista = [1, 3, 5, 7, 9]

for numero in range(1, 11):
    print(numero)
print('\n')

----------------------------------------------------

#enumerate:
#((0, 'R'), (1, 'a'), (2, 'f'), (3, 'a'), (4, 'e'), (5, 'l'), (6, ' '), (7, 'R'), (8, 'o'), (9, 'm'), (10, 'a'), (11, 'o'))

nome = 'Rafael Romao'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for indice, letra in enumerate(nome):
    print(nome[indice])
    
for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome): #Quando não precisamos de um valor, podemos descartá-lo utilizando o underline (_)
    print(letra)

----------------------------------------------------

nome = 'Rafael Romao'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for valor in enumerate(nome):
    print(valor)

for valor in enumerate(nome):
    print(valor[0])

for valor in enumerate(nome):
    print(valor[1])

----------------------------------------------------

qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

----------------------------------------------------

qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0

for n in range(1, qtd+1):
    numero = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + numero
print(f'A soma é {soma}')

----------------------------------------------------

nome = 'Rafael Romao'

for letra in nome:
    print(letra, end ='')#Em python o print já vem com um \n (quebra de linha) no final. Se quiser tirar, use o end='' para não pular linha.

----------------------------------------------------

#Exercicio teste: fazendo um desenho com emoji.

#Original = U+1F60D
#Modificado = U0001F60D
emoji = '\U0001F60D'

for num in range(0,11):
    print(f'{emoji *num}')

"""


