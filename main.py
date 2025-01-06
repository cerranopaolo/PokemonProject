import pygame
from pokemon import Pokemon
from move import Move
from battle import Battle
from ui import create_buttons, handle_button_click

# Inizializzazione pygame e impostazione della finestra di gioco
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pokemon Battle Game")

# Carica i dati iniziali dei Pokémon e delle mosse
pokemon_1 = Pokemon(name="Pikachu", level=5)
pokemon_2 = Pokemon(name="Charmander", level=5)

# Carica mosse
move_1 = Move(name="Thunderbolt", power=40)
move_2 = Move(name="Scratch", power=30)

# Inizia la battaglia
battle = Battle(pokemon_1, pokemon_2)

# Loop principale del gioco
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_button_click(event.pos)

    # Aggiorna l'interfaccia utente
    window.fill((255, 255, 255))
    create_buttons(window)
    pygame.display.update()

pygame.quit()
