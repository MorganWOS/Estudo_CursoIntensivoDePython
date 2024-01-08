def make_album(nome_artista, titulo_album, numero_musicas=None):
    dic = {'artista' : nome_artista, 'titulo' : titulo_album}
    
    if numero_musicas:
        dic['numero de musicas'] = numero_musicas
    
    return dic

while True:
    print('Escreva "não" para sair do programa')
    nome = input("Nome do artista: ")
    if nome == 'não':
        break
    titulo = input("Titulo do album: ")
    if titulo == 'não':
        break
    querer = input("Colocar o numero de musicas?(s/n): ")
    if querer == 's':
        numero_musica = input("Numero de musicas: ")
        album = make_album(nome, titulo, numero_musica)
    else:
        album = make_album(nome, titulo)
    print(album,'\n')