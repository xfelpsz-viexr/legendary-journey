sit1 = "Aprovado"
sit2 = "Reprovado"
nota1 = int(8 + 6)
nota2 = int(9 + 4)
contnota1 = int(nota1 / 2)
contnota2 = int(nota2 / 2)
cond1 = contnota1 >= 7
cond2 = contnota1 < 7
cond3 = contnota2 >= 7
cond4 = contnota2 < 7

nome1 = f"Maria, nota: {contnota1}"
print(nome1)
#nota1  
if contnota1 >= 7:
    print(sit1)
else:
    print(sit2)
if cond1:
    print("Parabéns!")
if cond2:
    print("Estude mais!")

nome2 = f"João, nota: {contnota2}"
print(nome2)
#nota2
if contnota2 >= 7:
    print(sit1)
else:
    print(sit2)
if cond3:
    print("Parabéns!")
if cond4:
    print("Estude mais!")