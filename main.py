from db.pokedex import Pokedex
from helper.WriteAJson import writeAJson

pokedex = Pokedex()
'''
Entrega do relatório 3 parte 2.
Desenvolvimento de 5 metodos na classe Pokedex para pesquisas utilizando MongoDB
'''

#query para verificar o tipo passando o nome
name = 'Snorlax'
type = pokedex.get_typeByName(name)[0]
print(f'{name} is a {[f for f in type]} Pokemon')

#query para buscar o pokemon mais pesado
name, weight = pokedex.get_MostHeavyPokemon()
print(f'Most heavy pokemon: {name} - {weight}Kg')

#query para buscar o pokemon mais alto
name, height = pokedex.get_MostTallPokemon()
print(f'Most tall pokemon: {name} - {height}m')

#query para buscar pela fraqueza
weak = 'Ghost'
pokemons = pokedex.get_PokemonByWeaknesses(weak)
print(f'Pokemons thats have {weak} weakness:')
for i, pokemon in enumerate(pokemons):
    print(f'{i} - {pokemon}')

#query para buscar pokemons com spaw chance > 1
pokespaws = pokedex.get_PokemonSpawChance()
print(f'Pokemons thats have Spaw chance greater than 1:')
for pokemon in pokespaws:
    print(f'{pokemon} - Spaw chance = {pokespaws[pokemon]}')