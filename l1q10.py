#Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus fahrenhrit.
#°f = (9 *°c)/s + 32 
#entrada
temperatura_celsius = float (input ('Digite a temperatura de celsius: '))



#processamento
temperatura_fahrenhrit = (9 * temperatura_celsius)/5 + 32



#saída 
print('A temperatura{:.1f}°C é igual a {:.1f}°f' . format (temperatura_celsius,temperatura_fahrenhrit))