import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 600, 700
CAR_WIDTH, CAR_HEIGHT = 50, 100
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)
ROAD_COLOR = (50, 50, 50)
LANE_COLOR = (255, 255, 0)
FPS = 60

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Load Car Image
car_image = pygame.image.load("g/car.png")  # Replace with actual car image
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

car_image = pygame.image.load("g/car.png")  # Replace with actual car image
car_image = pygame.transform.scale(car_image, (CAR_WIDTH, CAR_HEIGHT))

# Player Car
player_x = WIDTH // 2 - CAR_WIDTH // 2
player_y = HEIGHT - CAR_HEIGHT - 20
player_speed = 5

# Enemy Car
enemy_width, enemy_height = 50, 100
enemy_x = random.choice([150, 250, 350])  # Lanes
enemy_y = -enemy_height
enemy_speed = 5

# Game Loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(ROAD_COLOR)  # Background
    pygame.draw.rect(screen, LANE_COLOR, (190, 0, 10, HEIGHT))  # Left lane
    pygame.draw.rect(screen, LANE_COLOR, (390, 0, 10, HEIGHT))  # Right lane

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get Key Presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 120:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < 420:
        player_x += player_speed

    # Move Enemy Car
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_height
        enemy_x = random.choice([150, 250, 350])  # Respawn in random lane

    # Check Collision
    if player_x < enemy_x + enemy_width and player_x + CAR_WIDTH > enemy_x and player_y < enemy_y + enemy_height and player_y + CAR_HEIGHT > enemy_y:
        print("Game Over!")
        running = False

    # Draw Cars
    screen.blit(car_image, (player_x, player_y))  # Player Car
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))  # Enemy Car

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
