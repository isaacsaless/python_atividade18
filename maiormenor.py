# Exercício Python 18: Escreva um programa que leia dois números
# inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

print("Descubra se um número é maior, menor ou se eles são iguais")

num1 = int(input("Digite o 1° número: "))
num2 = int(input("Digite o 2° número: "))

if num1 > num2:
    print("O primeiro valor é maior.")
elif num2 > num1:
    print("O segundo valor é maior.")
else:
    print("Não existe valor maior, os dois são iguais.")