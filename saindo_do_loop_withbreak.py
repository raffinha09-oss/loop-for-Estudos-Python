"""
Saindo de loops com break

Funicona da mesma forma que nas linguagens C ou Java
 - Funcionalidade: Usamos o break para sairmos de loops de maneira projetada.
"""

#Exemplo 1 - usando for

for numero in range(1,11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sair do loop')


#Exemplo 2 - usando while

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
