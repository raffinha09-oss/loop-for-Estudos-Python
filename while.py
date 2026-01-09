"""
Loop while

Forma geral sintaxe do loop usando while

while expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso.

----------------------------------------------------------------------------------

#Exemplo 1 while
numero = 1
while numero < 10:
    print(numero)
    numero = numero + 1

#OBS: Em um loop while, é importante que cuidemos do critério de parada

----------------------------------------------------------------------------------


"""

#Exemplo 2 while

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jessica?')

