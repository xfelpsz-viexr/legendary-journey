# variáveis
sit1 = "Aprovado"
sit2 = "Reprovado"
nota1 = int(8 + 6)
nota2 = int(9 + 4)
nota3 = int(7 + 7)
contnota1 = float(nota1 / 2)
contnota2 = float(nota2 / 2)
contnota3 = float(nota3 / 2)

# código
while True:
    aluno = input("Digite seu nome: ")

# para Maria
    if "Maria" in aluno:
        print(f"Olá, {aluno}!")
        consulta = input("Deseja consultar sua nota? (s/n): ")
        if "s" in consulta:
            print(f"Sua nota é: {contnota1}")
            if contnota1 >= 7:
                print(sit1)
            else:
                print(sit2)
        elif "n" in consulta:
            print("Tudo bem, até mais!")
            break

# para João
    elif "João" in aluno:
        print(f"Olá, {aluno}!")
        consulta = input("Deseja consultar sua nota? (s/n): ")
        if "s" in consulta:
            print(f"Sua nota é: {contnota2}")
            if contnota2 >= 7:
                print(sit1)
            else:
                print(sit2)
        elif "n" in consulta:
            print("Tudo bem, até mais!")
            break

# para Carlos
    elif "Carlos" in aluno:
        print(f"Olá, {aluno}!")
        consulta = input("Deseja consultar sua nota? (s/n): ")
        if "s" in consulta:
            print(f"Sua nota é: {contnota3}")
            if contnota3 >= 7:
                print(sit1)
            else:
                print(sit2)
        elif "n" in consulta:
            print("Tudo bem, até mais!")
            break

    # caso o nome digitado não exista
    else:
        print("Aluno não encontrado.")

# continuar pesquisa
    continuar = input('Deseja pesquisar outro nome? (s/n): ')
    if continuar != 's':
        print('Tudo bem, até mais!')
        break