cities = {
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'nearby mountains': 'andes',
        'spoken language': 'spanish',
        },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'nearby mountains': 'alaska range',
        'spoken language': 'english',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'nearby mountains': 'himilaya',
        'spoken language': 'sanskrit',
        }
    }

for city_info, fields in cities.items():
   country = fields['country']
   city =  city_info
   population = fields['population']
   interesting_facts = fields['nearby mountains']
   language = fields['spoken language']
   print(f"\nIn {country.title()}, the capital is {city.title()} and"
      f" the spoken language is {language.title()}. It has {interesting_facts.title()} around.")

