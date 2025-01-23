# Dictionaries
# Make a dictionary
# Using Keys
my_dictionary = {'name': 'John', 'age': 36, 'city': 'New York'}
# Using function dict()
my_dictionary2 = dict(name='John', age=36, city='New York')

# Accessing items
print('Accessing Items')
print(my_dictionary['name'] + ' is ' + str(my_dictionary['age']) + ' years old.\nThis is using keys')
print(my_dictionary2['name'] + ' is ' + str(my_dictionary2['age']) + ' years old.\nThis is using dict')

# Modifying items
print('Modifying Items')
my_dictionary['age'] = 40
print(my_dictionary['age'])

#delete items
print('Deleting Items')
del my_dictionary['city']
print(my_dictionary)

# Uselfull Methods
print('Uselfull Methods')
print(my_dictionary.get('city'))
print(my_dictionary.get('city', 'Not Found'))
print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())



