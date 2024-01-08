lista_convidados = ['Cristiano Ronaldo', 'Peter Parker', 'Bruce Wayne']
for i in lista_convidados:
    print("Você esta convidado, {}" .format(i))
print('Peter Parker não podera comparecer :(')
lista_convidados.remove('Peter Parker')
lista_convidados.append('Matue')
for i in lista_convidados: #chamando os convidados de novo
    print("Você esta convidado, {}" .format(i))
print('Encontrei o Michael Jackson, a Ananda e o Messi!!!')
lista_convidados.insert(0, 'Michael Jackson')
lista_convidados.insert(4, 'Anada')
lista_convidados.append('Messi')
for i in lista_convidados: #chamando de novo
    print("Você esta convidado, {}" .format(i))
lista_desconvidados = []
while len(lista_convidados) > 2: #remove os convidados até sobrar os dois primeiros da lista
    lista_desconvidados.append(lista_convidados.pop())
for i in lista_desconvidados:
    print('Lamento, você esta desconvidado, {}' .format(i))
for i in lista_convidados:
    print('Você continua convidado, {}' .format(i))
while len(lista_convidados) > 0:
    del lista_convidados[0]
print(lista_convidados)