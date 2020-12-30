import pygame 
import random
import time
pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
FPS = 60

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

MAIN_FONT = pygame.font.SysFont("helvetica", 40)

BLACK = (0, 0, 0)
WHITE =  (255, 255, 255)
LIGHT_GREY = (240, 255, 240)
CORAL = (240, 128, 128)
DARK_BLUE = (0, 32, 63)
LIGHT_BLUE = (173, 239, 209)

clock = pygame.time.Clock()

class Ball(): 
    VEL_X = 5
    VEL_Y = 5 

    def __init__(self):
        self.width = 10 
        self.height = 10

        self.x  = (SCREEN_WIDTH / 2 - self.width / 2) 
        self.y = (SCREEN_HEIGHT / 2 - self.height / 2)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self): 
        self.rect.x += self.VEL_X
        self.rect.y += self.VEL_Y

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT: 
            self.VEL_Y *= -1

    def draw(self, screen): 
        pygame.draw.rect(screen, CORAL, (self.rect))

class Player(): 
    VEL = 5 

    def __init__(self):
        self.width = 5 
        self.height = 80

        self.x  = (SCREEN_WIDTH - self.width) 
        self.y = (SCREEN_HEIGHT / 2 - self.height / 2)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def move_up(self): 
        if self.rect.y >= 0: 
            self.rect.y -= self.VEL

    def move_dowm(self): 
        if self.rect.bottom <= SCREEN_HEIGHT: 
            self.rect.y += self.VEL

    def draw(self, screen): 
        pygame.draw.rect(screen, LIGHT_BLUE, (self.rect))

class Opponnent(): 
    VEL = 4.5 

    def __init__(self):
        self.width = 5 
        self.height = 80

        self.x  = 0 
        self.y = (SCREEN_HEIGHT / 2 - self.height / 2)

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen): 
        pygame.draw.rect(screen, DARK_BLUE, (self.rect)) 

def restart(ball, player, opponnent): 
    ball.VEL_X = random.choice((-5, 5))
    ball.VEL_Y = random.choice((-5, 5))

    ball.rect.x = (SCREEN_WIDTH / 2 - ball.width / 2) 
    ball.rect.y = (SCREEN_HEIGHT / 2 - ball.height / 2)

    player.rect.x = (SCREEN_WIDTH - player.width)
    player.rect.y = (SCREEN_HEIGHT / 2 - player.height / 2)

    opponnent.rect.x = 0
    opponnent.rect.y = (SCREEN_HEIGHT / 2 - opponnent.height / 2)

def main(screen): 
    run = True 
    score_player = 0
    score_opponnent = 0
    player = Player()
    opponnent = Opponnent()
    ball = Ball()

    def redraw_game_win(screen): 
        screen.fill(BLACK)
        player.draw(screen)
        opponnent.draw(screen)
        ball.draw(screen)
        pygame.draw.aaline(screen, LIGHT_GREY, (SCREEN_WIDTH / 2, 0),(SCREEN_WIDTH / 2, SCREEN_HEIGHT))
        score_pl_text = MAIN_FONT.render(str(score_player), 1, LIGHT_GREY)
        score_op_text = MAIN_FONT.render(str(score_opponnent), 1, LIGHT_GREY)

        screen.blit(score_pl_text, (250 - score_pl_text.get_width(), 50))
        screen.blit(score_op_text, (350, 50))

        pygame.display.update()

    while run: 
        clock.tick(FPS)

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                run = False

        ball.move()

        if opponnent.rect.y > ball.rect.y and ball.rect.x <= SCREEN_WIDTH / 2 - 50 and opponnent.rect.top >= 0: 
            opponnent.rect.y -= opponnent.VEL
        if opponnent.rect.y < ball.rect.y and ball.rect.x <= SCREEN_WIDTH / 2 - 50 and opponnent.rect.bottom <= SCREEN_HEIGHT: 
            opponnent.rect.y += opponnent.VEL

        if ball.rect.colliderect(player.rect) or ball.rect.colliderect(opponnent.rect): 
            ball.VEL_X *= -1

        keys = pygame.key.get_pressed()     

        if keys[pygame.K_UP]: 
            player.move_up()
        if keys[pygame.K_DOWN]: 
            player.move_dowm()

        if ball.rect.left < 0: 
            score_player += 1
        if ball.rect.right > SCREEN_WIDTH: 
            score_opponnent += 1

        if ball.rect.left < 0 or ball.rect.right > SCREEN_WIDTH:
            restart(ball, player, opponnent)

        redraw_game_win(screen)

main(screen)