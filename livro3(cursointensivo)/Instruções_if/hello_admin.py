nomes_ususarios = ['Wesley', 'Morgan', 'Arthur', "Elizabeth", 'Admin']
if nomes_ususarios:
    for nome in nomes_ususarios:
        if nome == 'Admin':
            print("Ola administrador!!!. Gostaria de ver um relatorio ?")
        else:
            print("Bem vindo {}!!!" .format(nome))
else:
    print("Precisa de usuarios")
