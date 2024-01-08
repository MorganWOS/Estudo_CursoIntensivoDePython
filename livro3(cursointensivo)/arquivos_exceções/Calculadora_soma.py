while True:
    try:
        val1 = int(input("Primeiro valor: "))
        val2 = int(input("Segundo valor: "))

    except ValueError:
        print('Não foi colocado um numero!!')
    else:
        print(val1 + val2)  
        break