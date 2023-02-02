def mediaNota():

    nota1 = float(input('Digite nota 1: '))
    nota2 = float(input('Digite nota 2: '))
    nota3 = float(input('Digite nota 3: '))
    nota4 = float(input('Digite nota 4: '))

    soma = nota1 + nota2 + nota3 + nota4 
    media = 4
    total = soma / media

    print(f'A média das notas é: {total:.1f}' )

mediaNota()
