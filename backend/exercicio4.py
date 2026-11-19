nome = input('qual o nome do aluno: ')
nota1 = float(input('qual a primeira nota: '))
nota2 = float(input('qual a segunda nota: '))
nota3 = float(input('qual a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3
aval=''
if media == 10: 
    aval = 'excelente'

elif 7 <= media <= 9:
    aval = 'muito bom'

elif (media >= 5) and (media <= 7):
    aval = 'regular'

else:
    aval = 'ruim'

print('\n'*3)
print('-------------------------------------')
print(f'nome do aluno: {nome}\n')
print(f'primeira nota: {nota1}\n')
print(f'segunda nota: {nota2}\n')
print(f'terceira nota: {nota3}\n\n')
print(f'media: {media}\n')
print(f'avaliaçao: {aval}\n')
print('-------------------------------------')