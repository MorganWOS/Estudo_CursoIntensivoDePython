def city_country(city, country, population=''):
    if population:
        r = (f"{city}, {country} - population {population}")
    else:
        r = (f"{city}, {country}")
    return r.title()
