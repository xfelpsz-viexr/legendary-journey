while True:
    sit1 = 'Aprovado'
    sit2 = 'Reprovado'
    nota1 = int(input('Digite sua nota do 1trim: '))
    nota2 = int(input('Digite sua nota do 2trim: '))
    nota3 = int(input('Digite sua nota do 3trim: '))
    resultado = nota1 + nota2 + nota3
    print(resultado)
    if resultado < 180:
        print(sit2)
    else:
        print(sit1)
    continuar = input('Deseja realizar outra conta? (s/n): ')
    if continuar != 's':
        print('Tudo bem!')
        break