import pygame
import sys

pygame.init()

# Set up the screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Character Select")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define character images
character_images = [
    pygame.image.load("assets/images/warriorselect/ch1.png").convert_alpha(),
    pygame.image.load("assets/images/warriorselect/ch2.png").convert_alpha(),
    pygame.image.load("assets/images/warriorselect/ch3.png").convert_alpha(),
    pygame.image.load("assets/images/warriorselect/ch4.png").convert_alpha(),
    pygame.image.load("assets/images/warriorselect/ch5.png").convert_alpha(),
    pygame.image.load("assets/images/warriorselect/ch6.png").convert_alpha()
]

# Define character positions and sizes
CHARACTER_SIZE = (100, 100)
CHARACTER_GAP = 20
CHARACTER_START_X = 100
CHARACTER_START_Y = 200

# Define font
font = pygame.font.Font("assets/fonts/turok.ttf", 36)

# Define player variables
player1_selected = False
player2_selected = False
player1_character = None
player2_character = None

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_character_select():
    screen.fill(BLACK)
    draw_text("Player 1: Select Your Warrior", font, WHITE, 20, 20)
    draw_text("Player 2: Select Your Warrior", font, WHITE, 20, SCREEN_HEIGHT - 60)

    # Display character images for player 1
    for i, character_image in enumerate(character_images):
        x = CHARACTER_START_X + i * (CHARACTER_SIZE[0] + CHARACTER_GAP)
        y = CHARACTER_START_Y
        screen.blit(character_image, (x, y))
        draw_text(f"Character {i + 1}", font, WHITE, x, y + CHARACTER_SIZE[1] + 5)

    # Display character images for player 2
    for i, character_image in enumerate(character_images):
        x = CHARACTER_START_X + i * (CHARACTER_SIZE[0] + CHARACTER_GAP)
        y = SCREEN_HEIGHT - CHARACTER_START_Y - CHARACTER_SIZE[1]
        screen.blit(character_image, (x, y))
        draw_text(f"Character {i + 1}", font, WHITE, x, y - 30)

    pygame.display.flip()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if player 1 selected a character
            if not player1_selected:
                for i in range(len(character_images)):
                    x = CHARACTER_START_X + i * (CHARACTER_SIZE[0] + CHARACTER_GAP)
                    y = CHARACTER_START_Y
                    if x < mouse_x < x + CHARACTER_SIZE[0] and y < mouse_y < y + CHARACTER_SIZE[1]:
                        player1_selected = True
                        player1_character = i + 1
                        break

            # Check if player 2 selected a character
            elif not player2_selected:
                for i in range(len(character_images)):
                    x = CHARACTER_START_X + i * (CHARACTER_SIZE[0] + CHARACTER_GAP)
                    y = SCREEN_HEIGHT - CHARACTER_START_Y - CHARACTER_SIZE[1]
                    if x < mouse_x < x + CHARACTER_SIZE[0] and y < mouse_y < y + CHARACTER_SIZE[1]:
                        if i + 1 != player1_character:
                            player2_selected = True
                            player2_character = i + 1
                            break

    # If both players have selected characters, end character select
    if player1_selected and player2_selected:
        running = False

    draw_character_select()

