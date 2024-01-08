from pathlib import Path

path = Path("/home/morganwos/programação/projetos(python)/livro3(cursointensivo)/arquivos_exceções/learning_python.txt")
content = path.read_text().strip()
lines = content.splitlines()
for line in lines:
    print(line.replace('Python', 'C'))