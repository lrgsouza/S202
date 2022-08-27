from db.database import Database


class Pokedex:
    def __init__(self):
        self.db = Database(database="pokedex", collection="pokemons")
        self.db.resetDatabase()
        self.collection = self.db.collection

    def find(self, filters: dict):
        response = self.collection.find(filters)
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getAllPokemons(self):
        response = self.collection.find({}, {"name": 1, "_id": 0})
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon)
        return pokemons

    def getPokemonByName(self, name: str):
        response = self.collection.find({"name": name},
                                        {"_id": 0, "name": 1,
                                         "next_evolution": 1, "prev_evolution": 1,
                                         "type": 1, "weaknesses": 1})
        result = {}
        for pokemon in response:
            result = pokemon
        return result

    def getPokemonsByType(self, type: list):
        response = self.collection.find({"type": {"$all": type}}, {
            "_id": 0, "name": 1, "type": 1})
        result = []
        for pokemon in response:
            result.append(pokemon)
        return result

    def getPokemonEvolutionsByName(self, name: str):
        pokemon = self.getPokemonByName(name)

        evolutions = [pokemon['name']]
        hasNextEvolutions = ('next_evolution' in pokemon)
        hasPrevEvolutions = ('prev_evolution' in pokemon)

        if hasNextEvolutions:
            nextEvolutions = list(pokemon['next_evolution'])
            for evolution in nextEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        if hasPrevEvolutions:
            previousEvolutions = list(pokemon['prev_evolution'])
            for evolution in previousEvolutions:
                evolution = self.getPokemonByName(evolution['name'])
                evolutions.append(evolution['name'])

        return evolutions

    ### ======= RELATORIO ======= ###
    def get_typeByName(self,name: str):
        #buscando pokemon
        pokemon = self.getPokemonByName(name)
        #verificando tipo
        type = [pokemon['type']]
        #retorna tipo
        return type

    def get_MostHeavyPokemon(self):
        response = self.collection.find({}, {"name": 1,"weight": 1 ,"_id": 0})
        weight_dict = {}
        poke_name = 'Not Found'
        weight = 0.0
        for pokemon in response:
            weight_dict[pokemon['name']] = float(pokemon['weight'].split()[0])
        for pokemon in weight_dict:
            if weight_dict[pokemon] > weight:
                weight = weight_dict[pokemon]
                poke_name = pokemon

        return poke_name, weight

    def get_MostTallPokemon(self):
        response = self.collection.find({}, {"name": 1,"height": 1 ,"_id": 0})
        height_dict = {}
        poke_name = 'Not Found'
        height = 0.0
        for pokemon in response:
            height_dict[pokemon['name']] = float(pokemon['height'].split()[0])
        for pokemon in height_dict:
            if height_dict[pokemon] > height:
                height = height_dict[pokemon]
                poke_name = pokemon

        return poke_name, height

    def get_PokemonByWeaknesses(self, weakness: str):
        response = self.collection.find({"weaknesses": {"$all": [weakness]}},{"name": 1, "_id": 0})
        pokemons = []
        for pokemon in response:
            pokemons.append(pokemon['name'])
        return pokemons

    def get_PokemonSpawChance(self):
        response = self.collection.find({"spawn_chance": {"$gt": 1.0}},{"name": 1, "spawn_chance": 1, "_id": 0})
        pokemons_spaw = {}
        for pokemon in response:
            pokemons_spaw[pokemon['name']] = pokemon['spawn_chance']

        return pokemons_spaw