"""
Ranges

- Presicamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória, mas sim de maneira especificada.

Formas gerias:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo forma 1 -> Forma mais simples de fazer o range

for num in range(11):
    print(num)

--------------------------------------------------------------------------

# Exemplo forma 2

#range(valor_de_inicio, valor_de_parada)
#OBS: valor_de_parada não inclusive (inicio especificado pelo usuário e passo de 1 em 1)

for num in range(1, 11):
    print(num)

--------------------------------------------------------------------------

# Exemplo forma 3

#range(valor_de_inicio, valor_de_parada, passo)

# OBS: valor_de_inicio não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

for num in range(5,55+1,5):
    print(num)

--------------------------------------------------------------------------

# Exemplo forma 4

#range (valor_de_inicio, valor_de_parada, passo)
#OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário, podendo ser negativo)

for num in range(10,0-1,-2):
    print(num)

--------------------------------------------------------------------------

"""

