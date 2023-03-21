import pygame
import random
from pygame import mixer
pygame.init()

# creating a screen
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#Bacground
bacground = pygame.image.load("../images/4401983_2326453.jpg")
#bacgroundsound
mixer.music.load("../sound/background.wav")
mixer.music.play(-1)
# Title and Icon
pygame.display.set_caption("Hamid's game")
icon = pygame.image.load("../images/spaceship (1).png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("../images/spaceship (2).png")
playerX = 750
playerY = 650
playerXchange = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyychange = []
num_of_enemies = 9
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("../images/enemy.png"))
    enemyX.append(random.randint(0, 1460))
    enemyY.append(random.randint(100, 400))
    enemyXchange.append(0.8)
    enemyychange.append(80)


# Bullet
bulletImg = pygame.image.load("../images/enemy.png")
bulletX = 0
bulletY = 580
bulletX_change = 0.8
bulletY_change = 40
bullet_state = "Ready to shoot"

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x+16, y+10))

# create a button class to handle button functionality
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, font, font_size):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.font = pygame.font.SysFont(font, font_size)

    # draw the button on the screen
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width / 2, self.y + self.height / 2))
        surface.blit(text_surface, text_rect)

    # check if the mouse is hovering over the button
    def is_hover(self, pos):
        return self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height


# create a button instance
button = Button(text="Change Color", x=0, y=0, width=110, height=40, color=(0, 128, 0), hover_color=(0, 200, 0),
                font="Arial", font_size=20)

# initial background color
bg_color = (255, 0, 0)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.is_hover(pygame.mouse.get_pos()):
                # change the background color
                bg_color = (0, 0, 255)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill(bg_color)
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerXchange = -0.8
        if event.key == pygame.K_RIGHT:
            playerXchange = 0.8
        if event.key == pygame.K_SPACE:
            fire_bullet(playerX, bulletY)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerXchange = 0
    #Checking boundaries of spaceship
    playerX += playerXchange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 1480:
        playerX = 1480

    for i in range(num_of_enemies):
        enemyX[i] += enemyXchange[i]
        if enemyX[i] <= 0:
            enemyXchange[i] = 0.6
            enemyY[i] += enemyychange[i]
        elif enemyX[i] >= 1475:
            enemyXchange[i] = -0.6
            enemyY[i] += enemyychange[i]
        enemy(enemyX[i], enemyY[i], i)
    player(playerX, playerY)
    button.draw(screen)
    pygame.display.update()
