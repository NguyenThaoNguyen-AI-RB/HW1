from project.pokemon import Pokemon
class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []
    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return f"This pokemon is already caught"
    def release_pokemon(self, pokemon_name):
        self.pokemon_name = pokemon_name
        for pokemon in self.pokemons:
            if pokemon.name == self.pokemon_name:
                self.pokemons.remove(pokemon)
                return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"
    def trainer_data(self):
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for pokemon in self.pokemons:
            result.append(f"- {pokemon.pokemon_details()}")
        return "\n".join(result)