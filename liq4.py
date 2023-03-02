#faça um programa que peça 4 notas bimestrais e mostre a média.
# somar as 4 notaspor 4
#entrda das notas

nota_1 = float (input ('Digite sua primeira nota:'))
nota_2 = float (input ('Digite sua segunta nota: '))
nota_3 = float (input ('Digite sua terçeira nota:'))
nota_4 = float (input ('Digite sua quarta nota:  '))
nota_5 = float (input ('Digite sua quinta nota:  '))
nota_6 = float (input ('Digite sua sexta nota:   '))
nota_7 = float (input ('Digite sua setima nota:  '))
nota_8 = float (input ('Digite sua oitava nota:  '))

media_1bimestre = (nota_1 + nota_2)/2
media_2bimestre = (nota_3 + nota_4)/2
media_3bimestre = (nota_5 + nota_6)/2
media_4bimestre = (nota_7 + nota_8)/2

print ('Sua nota no primeiro bimestre é: ', media_1bimestre)
print ('Sua nota no segundo bimestre é: ', media_2bimestre )
print ('Sua nota no terçeiro bimestre é: ', media_3bimestre)
print ('Sua notano quarto bimestre é: ', media_4bimestre)

#outra forma
nota1= float(input( 'Digite sua primeira nota '))
nota2= float (input('digite sua segunda nota'))
nota3= float (input('Digite sua trçeira nota'))
nota4= float(input('Digite sua quarta nota '))

#calculo da media
media = (nota1 + nota2 + nota3 + nota4) / 4

#exibir o resultado
print('A media das {} {} {} {} notas e { :.2f}' (nota1,nota2,nota3,nota4, media))
