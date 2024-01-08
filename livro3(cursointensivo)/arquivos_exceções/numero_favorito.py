from pathlib import Path
import json

numero_favorito = input("Qual seu numero favorito: ")
path = Path('favorite_number.json')
if path.exists():
    numbers = json.loads(path.read_text())
    if numbers == numero_favorito:
        print(numbers, 'ja armazenado!')
    else:
        content = json.dumps(numero_favorito)
        path.write_text(content)
        print("Armazenando o novo numero!")
else:
    content = json.dumps(numero_favorito)
    path.write_text(content)
