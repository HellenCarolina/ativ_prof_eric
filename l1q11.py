""" Faça um programa que peça 2 números inteiros e um númro real.
    calcule e mostre:
    ° o produto do dobro do primreiro com metade do segundo.
    ° a soma do triplo do primeiro com o terceiro.
    ° o terceiro elevado ao cubo."""

#entrada
numero_1 = int (input('Digite o 1° numero inteiro:'))
numero_2 = int (input('Digite o 2° numero inteiro:'))
numero_real = float (input('Digite um numero real'))

#processamento
calculo_1 = numero_1 * 2 * numero_2 / 2
caculo_2 = 3 *numero_1 + numero_real 
calculo_3 = numero_real * numero_real * numero_real

#saída 
print ('o produto do dobro do primreiro com metade do segundo: {}'. format (calculo_1))
print (' a soma so triplo do primeiro com o terceiro: {}'. format (caculo_2))
print ('o terceiro rlrvado ao cubo: {}'. format (calculo_3))