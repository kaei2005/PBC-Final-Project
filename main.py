import pygame
import sys
import os

pygame.init()

# Set up the screen
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Character Select")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Define character images
character_images = []
character_paths = [
    "test/ch1.png",
    "test/ch2.png",
    "test/ch3.png",
    "test/ch4.png",
    "test/ch5.png"
]

for path in character_paths:
    if os.path.exists(path):
        character_images.append(pygame.image.load(path).convert_alpha())
    else:
        print(f"Error: File {path} does not exist.")
        sys.exit()

# Define character animations and their frame counts
character_animations = []
animation_paths = [
    "test/ch1_animation.png",
    "test/ch2_animation.png",
    "test/ch3_animation.png",
    "test/ch4_animation.png",
    "test/ch5_animation.png"
]

frame_counts = [8, 11, 10, 8, 10]  # Specify the number of frames for each character

for idx, path in enumerate(animation_paths):
    animation_frames = []
    sprite_sheet = pygame.image.load(path).convert_alpha()
    frame_count = frame_counts[idx]
    frame_height = sprite_sheet.get_height()
    frame_width = sprite_sheet.get_width() // frame_count

    for i in range(frame_count):
        frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
        animation_frames.append(frame)
    character_animations.append(animation_frames)

# Define character positions and sizes
CHARACTER_SIZE = (100, 100)
CHARACTER_GAP = 20

# Calculate the starting X position to center the characters
total_width = len(character_images) * CHARACTER_SIZE[0] + (len(character_images) - 1) * CHARACTER_GAP
CHARACTER_START_X = (SCREEN_WIDTH - total_width) // 2
CHARACTER_START_Y = (SCREEN_HEIGHT - CHARACTER_SIZE[1]) // 2 + 100  # Move down 100 pixels

# Define fonts
font_path = "test/turok.ttf"
font = pygame.font.Font(font_path, 36)
small_font = pygame.font.Font(font_path, 24)  # Smaller font for the "Press Enter to continue" message

# Define player variables
player1_selected = False
player2_selected = False
player1_character = None
player2_character = None

# Animation variables
selected_character = None
current_animation_frames = None
current_frame_index = 0
animation_counter = 0

# Define vertical offset for character animations
ANIMATION_VERTICAL_OFFSET = [50, 0, -30, -90, -30]  # Adjust the fourth character's animation up by 20 pixels

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_centered_text(text, font, color, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y))
    screen.blit(text_surface, text_rect)

def draw_highlighted_text(text, font, highlight_color, normal_color, highlight_word, y):
    words = text.split()
    x = SCREEN_WIDTH // 2
    total_width = sum(font.size(word)[0] for word in words) + (len(words) - 1) * font.size(' ')[0]
    start_x = x - total_width // 2

    for word in words:
        color = highlight_color if word == highlight_word else normal_color
        word_surface = font.render(word, True, color)
        word_rect = word_surface.get_rect(topleft=(start_x, y))
        screen.blit(word_surface, word_rect)
        start_x += word_surface.get_width() + font.size(' ')[0]

def draw_character_select():
    screen.fill(BLACK)
    if not player1_selected:
        draw_text("Player 1: Select Your Warrior", font, WHITE, 20, 20)
    elif not player2_selected:
        draw_text("Player 2: Select Your Warrior", font, WHITE, 20, 20)

    # Display character images in a single row centered on the screen
    for i, character_image in enumerate(character_images):
        x = CHARACTER_START_X + i * (CHARACTER_SIZE[0] + CHARACTER_GAP)
        y = CHARACTER_START_Y

        if player1_selected and not player2_selected and i == player1_character - 1:
            continue  # Skip the character already selected by player 1

        # Scale
        character_image_scaled = pygame.transform.scale(character_image, CHARACTER_SIZE)
        screen.blit(character_image_scaled, (x, y))
        draw_text(f"{i + 1}", font, WHITE, x, y + CHARACTER_SIZE[1] + 5)

    # Display selected character animation
    if current_animation_frames is not None:
        frame = current_animation_frames[current_frame_index]
        # Scale the frame to make it larger
        scaled_frame = pygame.transform.scale(frame, (frame.get_width() * 2, frame.get_height() * 2))
        x = (SCREEN_WIDTH - scaled_frame.get_width()) // 2
        y = CHARACTER_START_Y - scaled_frame.get_height() + 50  # Move down 50 pixels
        # Apply vertical offset based on character index
        y += ANIMATION_VERTICAL_OFFSET[selected_character]
        screen.blit(scaled_frame, (x, y))

    # Draw "Press Enter to continue" message
    if selected_character is not None:
        draw_highlighted_text("Press Enter to continue", small_font, YELLOW, WHITE, "Enter", SCREEN_HEIGHT - 80)  # Move down to 80 pixels from the bottom

   
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

            # Check if a character is clicked
            for i in range(len(character_images)):
                x = CHARACTER_START_X + i * (CHARACTER_SIZE[0] + CHARACTER_GAP)
                y = CHARACTER_START_Y
                if x < mouse_x < x + CHARACTER_SIZE[0] and y < mouse_y < y + CHARACTER_SIZE[1]:
                    selected_character = i
                    current_animation_frames = character_animations[selected_character]
                    current_frame_index = 0
                    animation_counter = 0
                    break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and selected_character is not None:
                if not player1_selected:
                    player1_selected = True
                    player1_character = selected_character + 1
                    selected_character = None
                    current_animation_frames = None
                elif not player2_selected:
                    player2_selected = True
                    player2_character = selected_character + 1
                    running = False

    # Update and draw character selection screen
    draw_character_select()

    # Update animation frame
    if current_animation_frames is not None:
        animation_counter += 0.03  # Adjust animation speed as needed
        current_frame_index = int(animation_counter) % len(current_animation_frames)

pygame.quit()

# After both players have selected characters, print selections
print(f"Player 1 selected character {player1_character}")
print(f"Player 2 selected character {player2_character}")

"""結束選角"""

import pygame
from pygame import mixer
from fighter import Fighter

mixer.init()
pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brawler")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#player scores. [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#define fighter variables
'''
WARRIOR_SIZE = 162
WARRIOR_SCALE = 4
WARRIOR_OFFSET = [72, 56]
WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
WIZARD_SIZE = 250
WIZARD_SCALE = 3
WIZARD_OFFSET = [112, 107]
WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]
'''
MARTIAL_HERO_SIZE = 840/10
MARTIAL_HERO_SIZE_y = 396/7
MARTIAL_HERO_SCALE = 3 # 待改
MARTIAL_HERO_DATA = [MARTIAL_HERO_SIZE, MARTIAL_HERO_SIZE_y, MARTIAL_HERO_SCALE]

HERO_KNIGHT_SIZE = 840/11
HERO_KNIGHT_SIZE_y = 396/7
HERO_KNIGHT_SCALE = 3
HERO_KNIGHT_DATA = [HERO_KNIGHT_SIZE, HERO_KNIGHT_SIZE_y, HERO_KNIGHT_SCALE]

EVIL_WIZARD_SIZE = 870/8
EVIL_WIZARD_SIZE_y = 518/7
EVIL_WIZARD_SCALE = 3
EVIL_WIZARD_DATA = [EVIL_WIZARD_SIZE, EVIL_WIZARD_SIZE_y, EVIL_WIZARD_SCALE]

MEDIEVAL_KING_SIZE = 541/8
MEDIEVAL_KING_SIZE_y = 366/7
MEDIEVAL_KING_SCALE = 4
MEDIEVAL_KING_DATA = [MEDIEVAL_KING_SIZE, MEDIEVAL_KING_SIZE_y, MEDIEVAL_KING_SCALE]

MEDIEVAL_WARRIOR_SIZE = 96
MEDIEVAL_WARRIOR_SIZE_y = 530/7
MEDIEVAL_WARRIOR_SCALE = 3
MEDIEVAL_WARRIOR_DATA = [MEDIEVAL_WARRIOR_SIZE,  MEDIEVAL_WARRIOR_SIZE_y, MEDIEVAL_WARRIOR_SCALE]
DATA = [EVIL_WIZARD_DATA, HERO_KNIGHT_DATA, MARTIAL_HERO_DATA, MEDIEVAL_KING_DATA, MEDIEVAL_WARRIOR_DATA]

#load music and sounds
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
magic_fx.set_volume(0.75)

#load background image
bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

#load spritesheets
'''
warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()
'''
martial_hero_sheet = pygame.image.load("assets/images/warriors/Martial Hero/Sprite/Martial Hero 3_image.png").convert_alpha()
hero_knight_sheet = pygame.image.load("assets/images/warriors/Hero Knight/Sprites/Hero Knight_image.png").convert_alpha()
evil_wizard_sheet = pygame.image.load("assets/images/warriors/EVil Wizard/Sprites/EVil Wizard 2_image.png").convert_alpha()
medieval_king_sheet = pygame.image.load("assets/images/warriors/Medieval King Pack/Sprites/Medieval King Pack 2_image.png").convert_alpha()
medieval_warrior_sheet = pygame.image.load("assets/images/warriors/Medieval Warrior Pack/Sprites/Medieval Warrior Pack 3_image.png").convert_alpha()
sheet = [evil_wizard_sheet, hero_knight_sheet, martial_hero_sheet, medieval_king_sheet, medieval_warrior_sheet]
#load vicory image
victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

#define number of steps in each animation
'''
WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]
'''
MARTIAL_HERO_ANIMATION_STEPS = [10, 8, 3, 7, 7, 3, 11]
HERO_KNIGHT_ANIMATION_STEP = [11, 8, 3, 7, 7, 4, 11]
EVIL_WIZARD_ANIMATION_STEP = [8, 8, 2, 8, 7, 3, 7]
MEDIEVAL_KING_ANIMATION_STEP = [8, 8, 2, 4, 4, 4, 6]
MEDIEVAL_WARRIOR_ANIMATION_STEP = [10, 6, 2, 4, 4, 3, 9]
STEPS = [EVIL_WIZARD_ANIMATION_STEP, HERO_KNIGHT_ANIMATION_STEP, MARTIAL_HERO_ANIMATION_STEPS, MEDIEVAL_KING_ANIMATION_STEP, MEDIEVAL_WARRIOR_ANIMATION_STEP]
#define font
count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

#function for drawing text
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#function for drawing background
def draw_bg():
  scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
  screen.blit(scaled_bg, (0, 0))

#function for drawing fighter health bars
def draw_health_bar(health, x, y):
  ratio = health / 100
  pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 34))
  pygame.draw.rect(screen, RED, (x, y, 400, 30))
  pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

# 幫我檢查
#create two instances of fighters
DATA[player1_character - 1].append([72, 56])
DATA[player2_character - 1].append([112, 107])
fighter_1 = Fighter(player1_character, 200, 310, False, DATA[player1_character - 1], sheet[player1_character - 1], STEPS[player1_character - 1], sword_fx)
fighter_2 = Fighter(player2_character, 700, 310, True, DATA[player2_character - 1], sheet[player2_character - 1], STEPS[player2_character - 1], magic_fx)

#game loop
run = True
while run:

  clock.tick(FPS)

  #draw background
  draw_bg()

  #show player stats
  draw_health_bar(fighter_1.health, 20, 20)
  draw_health_bar(fighter_2.health, 580, 20)
  draw_text("P1: " + str(score[0]), score_font, RED, 20, 60)
  draw_text("P2: " + str(score[1]), score_font, RED, 580, 60)

  #update countdown
  if intro_count <= 0:
    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
    fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
  else:
    #display count timer
    draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
    #update count timer
    if (pygame.time.get_ticks() - last_count_update) >= 1000:
      intro_count -= 1
      last_count_update = pygame.time.get_ticks()

  #update fighters
  fighter_1.update()
  fighter_2.update()

  #draw fighters
  fighter_1.draw(screen)
  fighter_2.draw(screen)

  #check for player defeat
  if round_over == False:
    if fighter_1.alive == False:
      score[1] += 1
      round_over = True
      round_over_time = pygame.time.get_ticks()
    elif fighter_2.alive == False:
      score[0] += 1
      round_over = True
      round_over_time = pygame.time.get_ticks()
  else:
    #display victory image
    screen.blit(victory_img, (360, 150))
    if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
      round_over = False
      intro_count = 3
      # fighter_1 = Fighter(1, 200, 310, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
      # fighter_2 = Fighter(2, 700, 310, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

  #event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False


  #update display
  pygame.display.update()

#exit pygame
pygame.quit()
