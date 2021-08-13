from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(40,40))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:    self.rect.y += self.speed

class Enemy(GameSprite):
    side="left"
    def update(self):
        if self.rect.x <= 410:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        sprite.Sprite.__init__(self)
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
    

        # picture of the wall - a rectangle of the desired size and color
        self.image = Surface([self.width, self.height])
        self.image.fill((color_1, color_2, color_3))
    
        # each sprite should store the rect (rectangle) property
        self.rect = self.image.get_rect()
        self.rect = Rect(wall_x, wall_y, wall_width, wall_height)
    def draw_wall(self):
        draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))




 
win_width = 700
win_height = 500
display.set_caption("Labyrinth")
window = display.set_mode((win_width, win_height))

hero = Player("hero.png",50,400,5)
enemy= Enemy("cyborg.png", 600,250,5)
enemy2= Enemy("cyborg.png", 600,100,5)
enemy3 =Enemy("cyborg.png", 600,350,5)
w1 = Wall (255, 0, 255, 300, 200, 200, 10)
w2 = Wall(0,255,0,300,200,10,200)
w3 = Wall(255,0,0,200,200,300,10)
w4 = Wall(255,0,0,200,0,10,200)
w5=Wall(255,0,0,400,100,300,10)
w6=Wall(255,0,0,400,400,300,10)
walls = sprite.Group()
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)



pacman= GameSprite("pac-1.png", 255,100,5)
run = True
finish = False
while run:
    time.delay(50)
    window.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT:
            run=False
    if not finish: 
        for w in walls:
            w.draw_wall()
        hero.reset()
        hero.update()
        enemy.update()
        enemy2.update()
        enemy3.update()
        enemy.reset()
        enemy2.reset()
        enemy3.reset()
        pacman.reset()
        if sprite.collide_rect(hero,pacman):
            finish = True
            img = image.load('thumb.jpg')
            window.fill((255,255,255))
            window.blit(transform.scale(img, (win_width,win_height)),(0,0))
        if sprite.collide_rect(hero,enemy) or sprite.collide_rect(hero,enemy2)or sprite.collide_rect(hero,enemy3) or sprite.spritecollide(hero,walls,False) :
            finish = True
            img = image.load('game-over_1.png')
            window.fill((255,255,255))
            window.blit(transform.scale(img, (win_width,win_height)),(0,0))


        display.update()