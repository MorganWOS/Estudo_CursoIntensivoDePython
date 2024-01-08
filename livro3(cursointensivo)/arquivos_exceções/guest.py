from pathlib import Path

path = Path('guest_book.txt')
lista = ''
while True:
    name = input("Qual o seu nome? ") 
    if name == 'n':
        break
    lista += name + '\n'
path.write_text(lista)
print(path.read_text())
v = int(input(": "))