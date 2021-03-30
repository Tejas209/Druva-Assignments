# write a simple code to find the cube of list of numbers
my_list = [1, 3, 5, 7, 9]
cube_list = [x ** 3 for x in my_list]
print(cube_list)

# above program using lambda function
letters = list(map(lambda x: x**3, my_list))
print(letters)

# Double the value of each key values and save it in another dictionary with the same key name
d1 = {'a': 1, 'b': 2, 'c': 3}
myDict = {x: x**2 for x in d1.values()}
print(myDict)


