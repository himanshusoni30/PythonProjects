"""
Lists
-- maintains the order of insertion of values in list.
"""

courses = ['Math','Physics','History','Chemistry']
print(courses)
print()
print("Slicing in List")
print(courses[0:2])
print(courses[:2])
print(courses[2:3])
print(courses[2:])
print()
print("Append the list")
courses.append('Art')
print(courses)
courses_2 = ['Design','Animation']
# courses.append(courses_2)
# print(courses)
print()
print("Insert into List")
courses_2.insert(2,'Sociology')
print(courses_2)
print()
print("Extend the List")
courses.extend(courses_2)
print(courses)
print()
print("Sort the List")
courses.sort()
print(courses)
print()
print("Reverse sort the list")
courses.sort(reverse=True)
print(courses)
print()
print("Sort the list using sorted() method")
sorted(courses)
print(courses)
new_sorted = sorted(courses)
print(new_sorted)
print()
print("Length of List")
length = len(courses)
print(length)
print()
print("Print last element of List")
print(courses[-1])
print()
print("Remove item from list")
courses.remove('Chemistry')
print(courses)
print()
print("Pop out item from list")
popped = courses.pop()
print(popped)
print()
print("Reverse the contents of List")
courses.reverse()
print(courses)
print()
print("Count number of occurrences of item in list")
count = courses.count("Math")
print(count)
print()
print("Copy contents of one list to the other")
courses_3 = courses.copy()
print(courses_3)
print()
print("Clear the contents of List")
courses_3.clear()
print(courses_3)
print()
print("Iterate through the items of list using loop")
for items in courses:
    print(items,end=' ')
print()
print()
print("Concatenate the contents of list using join")
new_list = ' - '.join(courses)
print(new_list)
new_list = ' | '.join(courses)
print(new_list)
print()
print("Print the index of an item in list")
index=courses.index("Physics")
print(index)

""" 
Tuples 
-- these are immutable objects whereas lists are mutable
-- maintains the order of insertion of values in list
"""

print()
print("Tuples")
cs_courses = ('Math', 'Physics', 'History', 'Chemistry')
print(cs_courses)
print()
ind = cs_courses.index("Physics")
print("Index of item Physics in Tuple is: ",ind)
# print()
# print("Append the tuple.")
# cs_courses.append('Art')
# print(cs_courses)
print()
print("Iterate through the items of Tuple using loop")
for items in cs_courses:
    print(items, end=' ')
print()
new_tuple = ' - '.join(cs_courses)
print(new_tuple)

"""
Sets 
-- Duplicate values are not allowed to store in Sets. Also set does not maintain the order of insertion.
"""

print()
art_courses = {'Art','Animation','Graphics','Visualization'}
print("Set: ", art_courses)
print()
print("Difference between two sets.")
art_courses_2 = {'Art','Graphics', '2D', '3D'}
print(art_courses.difference(art_courses_2))
print()
print("Common between two sets.")
art_courses_2 = {'Art','Graphics', '2D', '3D'}
print(art_courses.intersection(art_courses_2))
print()
print("Union of two sets.")
art_courses_2 = {'Art','Graphics', '2D', '3D'}
print(art_courses.union(art_courses_2))
print()
print("Add duplicate values in set")
art_courses.add('Graphics')
print(art_courses)
print()
print("Iterate through the items of Set using loop")
for items in art_courses:
    print(items, end=' ')
print()
new_set = ' - '.join(art_courses)
print(new_set)