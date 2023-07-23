""" 
KEYS
GET 
VALUES
ITEMS 
 """

# keys
my_colors = {'amarillo': 'yellow', "azul": "blue", "verde": "green"}
keys = my_colors.keys()
print(keys)

# get
get = my_colors.get("blanco", 'not found this color')
print(get)

# values
values = my_colors.values()
print(values)

# items
items = my_colors.items()
print(items)
