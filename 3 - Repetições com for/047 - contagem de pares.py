#Crie um programa que mostre na tela todos os números pares que estão no intervalo
# entre 1 e 50.
par = 0
for c in range(1,51):
    if c % 2 == 0:
        par = par + c
        print(c)