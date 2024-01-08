pessoa1 = {
    'nome' : 'wesley',
    'idade' : '19', 
    'sobrenome' : 'silva', 
    'cidade' : 'sao paulo'
    }
pessoa2 = {
    'nome' : 'arthur', 
    'idade' : '38',
    'sobrenome' : 'morgan',
    'cidade' : 'guarma'
}
pessoa3 = {
    'nome' : 'peter',
    'idade' : '21',
    'sobrenome' : 'parker',
    'cidade' : 'new york'
}


people = [pessoa1, pessoa2, pessoa3]
for x in people:
    for k, v in x.items():
        print(k, v.title())
    print()


for i in pessoa1:
    print(pessoa1[i].title())
print()


num_favoritos = {
    'wesley' : 2,
    'morgan' : 4,
    'arthur' : 15,
    'carol' : 2,
    'elizabeth' : 29
}
for i in num_favoritos:
    print(i.title(), '\n numero favorito: ', num_favoritos[i])