class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = 100  # Default HP
        self.attack = 50  # Default attack stat
        self.defense = 50  # Default defense stat
        self.speed = 50  # Default speed stat
    
    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
    
    def is_fainted(self):
        return self.hp == 0

    def use_move(self, target_pokemon):
        # Usare una mossa sul Pokémon avversario
        move = target_pokemon.get_move()
        target_pokemon.take_damage(move.power)
