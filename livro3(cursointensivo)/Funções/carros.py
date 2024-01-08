def informações_carro(fabricante, modelo, **kwargs):
    kwargs['fabricante'] = fabricante
    kwargs['modelo'] = modelo

    for i, y in kwargs.items():
        print(i, ":", y, '\n')

informações_carro('chevrolet', 'camaro', cor='azul', portas='4')