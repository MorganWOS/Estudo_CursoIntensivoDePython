cities = {
    'sao paulo' : {
        'pais' : 'brasil',
        'populacao' : '200.000.000',
        'fato' : 'terra da garoa'},
    'tokio' : {
        'pais' : 'japao',
        'populacao' : '125.000.000',
        'fato' : 'animes'
    },
    'roma' : {
        'pais' : 'italia',
        'populacao' : '59.000.000',
        'fato' : 'coliseu'
    }}
for city, d in cities.items():
    print('\n',city.title())
    for x, y in d.items():
        print(x,':', y.title())