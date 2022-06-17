# cubes = []
# for cube in range(1,11):
#     cubes.append(cube**3)
# for cube in cubes:
#     print(cube)

cubes_of_comprehension = [cube**3 for cube in range(1,11)]
print(cubes_of_comprehension)
