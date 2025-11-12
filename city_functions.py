
def city_country(city, country, population=None):
    if population:
        formatted = f"{city.title()}, {country.title()} – population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted 