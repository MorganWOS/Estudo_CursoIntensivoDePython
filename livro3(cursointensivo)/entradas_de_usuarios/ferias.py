people = {}
while True:
    name = input("Nome: ")
    viagem = input("Local de ferias: ")
    people[name] = viagem

    b = input("Continuar pesquisa?(s/n): ")
    if b == 'n':
        break


for x, y in people.items():
    print(x, ':', y, '\n')