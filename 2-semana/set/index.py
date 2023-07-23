my_set = {1, 2, 3, 4}
print(my_set)

my_list = [1, 2, 3, 4, 4, 5]
my_set_by_list = set(my_list)
print(my_set_by_list)

""" add """
my_set.add(5)
print(my_set)

""" update """
my_set.update([6, 7, 8, 9, 10])

print(my_set)
print(len(my_set))

""" discard """
my_set.discard(6)
print(my_set)

""" remove (err) """
my_set.remove(3)
print(my_set)

boolean = 2 in my_set
print(boolean)
