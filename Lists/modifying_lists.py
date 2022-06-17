bikes = ['Honda', 'Yamaha', 'Suzuki', 'Daihatsu']


# print(f"The first bike I owned was {owned_first}, and the last one was {owned_last},"
#       f" among {bikes}")
too_expensive = 'Suzuki'
bikes.remove(too_expensive)

print(f"\n{too_expensive.title()} was too expensive for me")

print(bikes[-1])
