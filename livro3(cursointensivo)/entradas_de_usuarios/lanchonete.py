sandwich_orders = ['salada', 'vegano', 'pastrami', 'carne', 'frango', 'peixe', 'pastrami', 'pastrami']
finished_sandwiches = []
print("Estamos sem pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    order = sandwich_orders.pop()
    print(f'Seu lanche: {order}\n')
    finished_sandwiches.append(order)
print('Estão pronto os lanches:')
for i in finished_sandwiches:
    print(i,'\n')