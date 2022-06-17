# def display_message():
#     print("I am learning functions")
#
# display_message()

# def favourite_book(title):
#     print(f"One of my fav books is {title.title()}")
#
# favourite_book('hobbit')

# def make_shirt(text='I love Python', size='l'):
#     print(f"The shirt is of {size} size and has text {text} on it")
#
# make_shirt()
# make_shirt(size='l')
# make_shirt(size='m')
# make_shirt(text='blah')

# def describe_city(city, country='Sweden'):
#     print(f"{city} is in {country}")
#
# describe_city('stockholm')
# describe_city('Johannesburg', 'South Africa')
# describe_city('Molde')

# def city_country(city, country):
#     return (f"{city.title()}, {country.title()}")
#
# print(city_country('santiago', 'chile'))
# print(city_country('brasil', 'brazil'))
# print(city_country('ottawa', 'canada'))


def make_album(artist_name, album_title, number_of_songs=None):
    album_dict = {
        'artist_name': artist_name,
        'album_title': album_title,
    }
    if number_of_songs:
        album_dict['number_of_songs'] = number_of_songs
    return  album_dict

# privateering = make_album('dire straits', 'privateering')


# print(stairway_to_heaven, another_brick)
while True:
    print("You can press q anytime to quit")

    artist = input("Enter an artist ")
    if artist == 'q':
        break

    album = input("Enter an album name ")
    if album == 'q':
        break

    number_of_songs = input("Enter how many songs there are in the album ")
    if number_of_songs == 'q':
        break
    print(make_album(artist, album, number_of_songs))
