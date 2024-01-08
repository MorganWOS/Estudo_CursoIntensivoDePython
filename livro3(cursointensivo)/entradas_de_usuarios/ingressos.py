soma = 0
while True:
    idade = int(input("Informe a idade: "))
    if idade == 0:
        break
    elif idade <= 3:
        continue
    elif idade <= 12:
        soma += 10
    elif idade > 12:
        soma += 15
    elif idade == 0:
        break
print(f'Valor: {soma} $')