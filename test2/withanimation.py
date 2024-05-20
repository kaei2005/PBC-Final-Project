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

# Define character images
character_images = []
character_paths = [
    "test/ch1.png",
    "test/ch2.png",
    "test/ch3.png",
    "test/ch4.png",
    "test/ch5.png",
    "test/ch6.png"
]

for path in character_paths:
    character_images.append(pygame.image.load(path).convert_alpha())

# Define character animations
character_animations = []
animation_paths = [
    "test/ch1_animation.png",
    "test/ch2_animation.png",
    "test/ch3_animation.png",
    "test/ch4_animation.png",
    "test/ch5_animation.png",
    "test/ch6_animation.png"
]

for path in animation_paths:
    animation_frames = []
    sprite_sheet = pygame.image.load(path).convert_alpha()
    frame_width = sprite_sheet.get_width() // 8  # Assuming each animation has 8 frames
    for i in range(8):
        frame = sprite_sheet.subsurface((i * frame_width, 0, frame_width, sprite_sheet.get_height()))
        animation_frames.append(frame)
    character_animations.append(animation_frames)

# Define character positions and sizes
CHARACTER_SIZE = (100, 100)
CHARACTER_GAP = 20
CHARACTER_START_X = (SCREEN_WIDTH - (len(character_images) * (CHARACTER_SIZE[0] + CHARACTER_GAP) - CHARACTER_GAP)) // 2
CHARACTER_START_Y = SCREEN_HEIGHT // 3

# Define font
font = pygame.font.Font(None, 36)

# Define player variables
current_player = 1
selected_character = None
current_animation_frames = None
current_frame_index = 0
animation_counter = 0

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)

def draw_character_select():
    screen.fill(BLACK)
    draw_text(f"Player {current_player}: Select Your Warrior", font, WHITE, 20, 20)

    # Display character images for selection
    for i, character_image in enumerate(character_images):
        x = CHARACTER_START_X + i * (CHARACTER_SIZE[0] + CHARACTER_GAP)
        y = CHARACTER_START_Y
        screen.blit(character_image, (x, y))
        draw_text(f"{i + 1}", font, WHITE, x, y + CHARACTER_SIZE[1] + 5)

    # Display selected character animation
    if current_animation_frames is not None:
        frame = current_animation_frames[current_frame_index]
        x = (SCREEN_WIDTH - frame.get_width()) // 2
        y = CHARACTER_START_Y - frame.get_height() - 20
        screen.blit(frame, (x, y))

    # Draw "Press Enter to continue" message
    if selected_character is not None:
        draw_text("Press Enter to continue", font, WHITE, SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT - 100)

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
                # Switch to the next player or end the game
                current_player += 1
                if current_player > 2:
                    running = False
                selected_character = None

    # Update and draw character selection screen
    draw_character_select()

    # Update animation frame
    if current_animation_frames is not None:
        animation_counter += 0.2
        current_frame_index = int(animation_counter) % len(current_animation_frames)

pygame.quit()
