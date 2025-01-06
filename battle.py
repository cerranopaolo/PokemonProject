class Battle:
    def __init__(self, pokemon_1, pokemon_2):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.turn = 1  # Turno di battaglia iniziale
    
    def next_turn(self):
        if self.turn % 2 == 0:
            # Turno del Pokémon 1
            self.pokemon_1.use_move(self.pokemon_2)
        else:
            # Turno del Pokémon 2
            self.pokemon_2.use_move(self.pokemon_1)
        
        self.turn += 1
        self.check_winner()

    def check_winner(self):
        if self.pokemon_1.is_fainted():
            print(f"{self.pokemon_2.name} wins!")
        elif self.pokemon_2.is_fainted():
            print(f"{self.pokemon_1.name} wins!")
