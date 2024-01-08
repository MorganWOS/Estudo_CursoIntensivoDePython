from cidade_pais import city_country

def test_cidade_pais():
    cc = city_country("santiago", "chile", '5000')
    assert cc == 'Santiago, Chile - Population 5000'