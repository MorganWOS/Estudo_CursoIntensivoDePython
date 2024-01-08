current_users = ['Morgan', 'Arthur', 'Wesley', 'Carol', 'Elizabeth']
new_users = ['Morgan', 'Carol', 'John', 'Lothus', 'Duth']
current_users_min = []
for i in current_users:
    i = i.lower()
    current_users_min.append(i)
for name in new_users:
    if name.lower() in current_users_min:
        print("Nome ja em uso!")
    else:
        print("Nome disponivel!")
