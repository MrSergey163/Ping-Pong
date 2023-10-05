from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self,speed,x,y,images):
        super().__init__()
        self.image = transform.scale(image.load(images),(50,50))
        self.speed = speed
        self.timer = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    

class Player(GameSprite):
    def __init__(self,speed,x,y,images):
        super().__init__(speed,x,y,images)
        self.health = 3
        self.image = transform.scale(image.load(images),(15,300))
        self.passedship = 0
        self.a = 5

    def blit(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))
    def walk(self):
        keys = key.get_pressed()
        if keys[K_s] and self.rect.y <375:
            self.rect.y+=self.speed
        if keys[K_w] and self.rect.y > -75:
            self.rect.y-=self.speed
            
class Player2(GameSprite):
    def __init__(self,speed,x,y,images):
        super().__init__(speed,x,y,images)
        self.health = 3
        self.image = transform.scale(image.load(images),(15,125))
        self.passedship = 0
        self.a = 5

    def blit(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))
    def walk(self):
        keys = key.get_pressed()
        if keys[K_DOWN] and self.rect.y <375:
            self.rect.y+=self.speed
        if keys[K_UP] and self.rect.y > -75:
            self.rect.y-=self.speed

class Ball(GameSprite):
    def __init__(self,speed,x,y,images):
        super().__init__(speed,x,y,images)
        self.speed1 = 5
    def blit(self):
        okno.blit(self.image,(self.rect.x,self.rect.y))
    def otskok(self):
        self.rect.x += self.speed1        
        self.rect.y += self.speed1
        if self.rect.colliderect(player_1.rect)      
FPS = 60                
clock = time.Clock()
okno = display.set_mode((700,500))
display.set_caption('Ping Pong')
player_1 = Player(5,0,200,'Player.png')
player_2 = Player2(5,683,200,'Player2.png')
background = transform.scale(image.load("background.png"),(700,500))
game = True
finish = False
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        okno.blit(background,(0,0))
        
        player_1.blit()
        player_1.walk()
        
        player_2.blit()
        player_2.walk()

    clock.tick(FPS)

    display.update()