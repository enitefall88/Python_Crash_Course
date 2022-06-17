places_to_travel = ['Italy', 'Spain', 'France', 'Philipines', 'Japan']
places_to_travel.sort(reverse=True)
print(len(places_to_travel))

list_of_cities = ['Toronto', 'Madrid', 'Barcelona', 'Rome']
print(sorted(list_of_cities))
list_of_cities.reverse()
print(len(list_of_cities))
list_of_cities.sort(reverse=True)

list_of_cities.append('Sao Paolo')

list_of_cities.remove('Madrid')
print(list_of_cities)
list_of_cities.insert(2,'Rio')
print(list_of_cities)
del list_of_cities[0]
print(list_of_cities)
list_of_cities.pop()
print(list_of_cities)
