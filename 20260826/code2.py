#PROGRAM TO CREATE A ROBOT CARTOON ANIMATION USING PYGAME

import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Cartoon Animation")

clock = pygame.time.Clock()

# Colors
WHITE = (245, 245, 245)
BLUE = (60, 150, 220)
DARK = (40, 45, 55)
BLACK = (10, 10, 10)
RED = (240, 70, 70)
GREEN = (70, 220, 120)
GROUND = (100, 200, 100)


def draw_robot(x, y, t):
    # Walking animation
    leg_move = math.sin(t * 0.15) * 18
    arm_move = math.sin(t * 0.15) * 15

    # Antenna
    pygame.draw.line(screen, DARK, (x + 50, y), (x + 50, y - 35), 5)
    pygame.draw.circle(screen, RED, (x + 50, y - 40), 8)

    # Head
    pygame.draw.rect(screen, BLUE, (x, y, 100, 70), border_radius=15)

    # Eyes
    pygame.draw.circle(screen, WHITE, (x + 30, y + 30), 12)
    pygame.draw.circle(screen, WHITE, (x + 70, y + 30), 12)

    pygame.draw.circle(screen, BLACK, (x + 30, y + 30), 5)
    pygame.draw.circle(screen, BLACK, (x + 70, y + 30), 5)

    # Smile
    pygame.draw.arc(screen, BLACK, (x + 30, y + 35, 40, 25), 0, math.pi, 3)

    # Body
    pygame.draw.rect(screen, DARK, (x + 15, y + 70, 70, 100), border_radius=12)

    # Body screen
    pygame.draw.rect(screen, GREEN, (x + 30, y + 90, 40, 30), border_radius=5)

    # Arms
    pygame.draw.line(
        screen, BLUE,
        (x + 15, y + 85),
        (x - 20, y + 120 + arm_move),
        12
    )

    pygame.draw.line(
        screen, BLUE,
        (x + 85, y + 85),
        (x + 120, y + 120 - arm_move),
        12
    )

    # Legs
    pygame.draw.line(
        screen, DARK,
        (x + 35, y + 170),
        (x + 25 + leg_move, y + 220),
        15
    )

    pygame.draw.line(
        screen, DARK,
        (x + 65, y + 170),
        (x + 75 - leg_move, y + 220),
        15
    )

    # Feet
    pygame.draw.ellipse(
        screen, BLACK,
        (x + 5 + leg_move, y + 210, 40, 15)
    )

    pygame.draw.ellipse(
        screen, BLACK,
        (x + 55 - leg_move, y + 210, 40, 15)
    )


# Main animation loop
running = True
x = -100
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Background
    screen.fill(WHITE)

    # Ground
    pygame.draw.rect(screen, GROUND, (0, 430, WIDTH, 70))

    # Move robot
    x += 3

    if x > WIDTH:
        x = -120

    draw_robot(x, 180, t)

    t += 1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()