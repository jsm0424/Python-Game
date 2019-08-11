import pygame
from pygame.sprite import Sprite

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))


class Character(Sprite):

    def __init__(self, x, y):
        self.HP = 100
        self.Damage = 20
        self.range = 10
        self.speed = 0.5
        self.time = 5
        self.x = x
        self.y = y
        self.image = pygame.image.load("player.jpg")

    def motion(self):
#       if collision():
#           pygame.transform.rotate(self.image, 20)
#           pygame.transform.rotate(self.image, -20)
#       else:
            self.x = self.x + self.speed


class Monster(Sprite):

    def __init__(self, x, y):
        self.HP = 100
        self.Damage = 20
        self.range = 10
        self.speed = 0.5
        self.time = 5
        self.x = x
        self.y = y
        self.image = pygame.image.load("Monster.png")

    def motion(self):
#       if collision():
#           pygame.transform.rotate(self.image, 20)
#           pygame.transform.rotate(self.image, -20)

#       else:
            self.x = self.x - self.speed


class Home:
    def __init__(self, x, y):
        self.HP = 2000
        self.image = pygame.image.load("house_final.png")
        self.x = x
        self.y = y


class Player:
    def __init__(self):
        self.house = Home(10, 250)
        self.army = []
        self.money = 0


class Computer:
    def __init__(self):
        self.house = Home(550, 250)
        self.army = []
        self.time = 300

    def show(self):
        for i in range(len(self.army)):
            self.army[i].motion()
            screen.blit(self.army[i].image, (self.army[i].x, self.army[i].y))


#def collision():
#    if Crect.colliderect(Mobrect):
#        return True
#    else:
#        return False


TARGET_FPS = 100
clock = pygame.time.Clock()
C = Character(40, 350)
#Crect = pygame.Rect(C.image.get_rect())
P = Player()
Com = Computer()
Mob = Monster(0, 0)
#Mobrect = pygame.Rect(Mob.image.get_rect())

while True:
    screen.fill((255, 255, 255))
    screen.blit(C.image, (C.x, C.y))
    screen.blit(P.house.image, (P.house.x, P.house.y))
    screen.blit(Com.house.image, (Com.house.x, Com.house.y))
    Com.time = Com.time - 1

    if Com.time <= 0:
        Mon = Monster(550, 400)
        Mob = Mon
#        Mobrect = pygame.Rect(Mob.image.get_rect())
        Com.army.append(Mon)
        Com.time = 300

    Com.show()
    C.motion()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    pygame.display.flip()
    clock.tick(TARGET_FPS)

