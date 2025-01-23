pokemon = {'Name': 'Dragapult', 'Type': 'dragon', 'Weakness': 'dragon'}

for key in pokemon:
    print(key)

for value in pokemon.values():
    print(value)

for key, value in pokemon.items():
    print(key + ': ' + value)

# Explanation
# The code first defines a dictionary called `pokemon` with keys `'Name'`, `'Type'`, and `'Weakness'`.
# The first `for` loop iterates through the dictionary's keys (e.g., `'Name'`, `'Type'`, `'Weakness'`) and prints each key.
# The second `for` loop uses the `values()` method to access and print all values in the dictionary (e.g., `'Dragapult'`, `'dragon'`, `'dragon'`).
# # The third `for` loop uses the `items()` method to iterate through each key-value pair in the dictionary, formatting them into strings like `'Name: Dragapult'` and prints them.

# Anidate Dictionaries

pokemons = {
    '1': {'name': 'bulbasaur', 'type': 'grass', 'weakness': 'fire'},
    '4': {'name': 'charmander', 'type': 'fire', 'weakness': 'water'},
    '7': {'name': 'squirtle', 'type': 'water', 'weakness': 'electric'}
}

for pokemon_name, pokemon_data in pokemons.items():
    print(pokemon_name + ': ' + pokemon_data['name'])