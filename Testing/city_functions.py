def city_country(city, country, population=''):
    if population:
        formatted_string = f"{city}, {country} population - {population}"
    else:
        formatted_string = f"{city}, {country}"
    capitalized = formatted_string.title()
    return capitalized

