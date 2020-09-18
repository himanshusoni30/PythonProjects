# animal = input("Please enter the animal: ")
"""
None condition check if variable value is None
"""
animal = None
if animal is None:
	print(str(animal) + " is not an animal")
else:
	print(animal + " is my favourite too.")

"""
Empty condition check if variable value is empty
"""
animal = ' '
if animal:
	print(str(animal) + " is not an animal")
else:
	print(str(animal) + " is my favourite too.")

"""
zero condition check if variable value is zero '0'
"""
animal = 0
if animal == False:
	print(str(animal) + " is not an animal")
else:
	print(animal + " is my favourite too.")