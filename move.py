class Move:
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def use(self, target_pokemon):
        # Calcola i danni e riduci la salute del Pokémon target
        damage = self.power
        target_pokemon.take_damage(damage)
