media_1 = float(input('Entre com a nota da primeira unidade: '))
media_2 = float(input('Entre com a nota da segunda unidade: '))
media_3 = float(input('Entre com a nota da terceira unidade: '))

nota_final = (media_1 + media_2 + media_3) / 3

print(f'Nota final: {nota_final}')
if nota_final < 6.0:
    print('Reprovado')
else:
    print('Aprovado')
