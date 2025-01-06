import pygame

# Crea i pulsanti per l'interfaccia
def create_buttons(window):
    font = pygame.font.Font(None, 36)
    attack_button = pygame.Rect(50, 500, 200, 50)
    heal_button = pygame.Rect(300, 500, 200, 50)
    
    pygame.draw.rect(window, (0, 255, 0), attack_button)
    pygame.draw.rect(window, (0, 0, 255), heal_button)

    window.blit(font.render("Attack", True, (255, 255, 255)), (100, 510))
    window.blit(font.render("Heal", True, (255, 255, 255)), (350, 510))

# Gestisce il click sui pulsanti
def handle_button_click(pos):
    if attack_button.collidepoint(pos):
        print("Attack button clicked")
    elif heal_button.collidepoint(pos):
        print("Heal button clicked")
