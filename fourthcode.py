# variáveis
sit1 = 'Aprovado.'
sit2 = 'Reprovado.'
codigo_registro = 404

access = input('Digite seu o código de acesso: ')
if "404" in access:
    print('Seja bem-vindo!')
else:
    print('Acesso negado.')

while True: 

    aluno = input('Digite o nome do aluno: ')
    calculo = input(f'Deseja calcular a nota final de {aluno}? (s/n): ')

    if calculo == 'n':
        print('Tudo bem!')
        break

    elif calculo == 's':
        nota_aluno = print('Digite a nota do aluno:')
        nota1 = int(input('Nota 1trim: '))
        nota2 = int(input('Nota 2trim: '))
        nota3 = int(input('Nota 3trim: '))
        resultado = nota1 + nota2 + nota3
        print(f'A nota final de {aluno} é: {resultado}')
        if resultado >= 180:
            print(f'A situação de {aluno} é: {sit1}')
        else:
            print(f'A situação de {aluno} é: {sit2}')

    refazer_calculo = input('Deseja consultar outra nota? (s/n): ')
    if refazer_calculo == 's':
        ()
    elif refazer_calculo == 'n':
        print('Tudo bem!')
        print('Consulta finalizada.')
        break