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

"""

#Exemplo de for 3 (Iterando sobre um Range)

nome = 'Rafael Romao'
lista = [1, 3, 5, 7, 9]

for numero in range(1, 11):
    print(numero)
print('\n')