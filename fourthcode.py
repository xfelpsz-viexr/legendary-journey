# variáveis
sit1 = 'Aprovado.'
sit2 = 'Reprovado.'
codigo_registro = 404

while True:

    access = input('Digite seu o código de acesso: ')
    if "404" in access:
        print('Seja bem-vindo!')
    else:
        print('Acesso negado.')
        break

    aluno = input('Digite o nome do aluno: ')
    calculo = input(f'Deseja calcular a nota final de {aluno}? (s/n): ')

    if calculo == 'n' or calculo == 'N':
        print('Tudo bem!')
        print('Consulta finalizada.')
        break

    elif calculo == 's' or calculo == 'S':
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
    
    else:
        print('Comando não reconhecido.')
        break

    refazer_calculo = input('Deseja consultar outra nota? (s/n): ')
    if refazer_calculo == 's' or refazer_calculo == 'S':
        ()
    elif refazer_calculo == 'n' or refazer_calculo == 'N':
        print('Tudo bem!')
        print('Consulta finalizada.')
        break
    else:
        print('Comando não reconhecido.')
        break