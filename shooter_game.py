import pygame


pygame.init()

finish = False
win = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

back = pygame.transform.scale(pygame.image.load("galaxy.jpg"), (500, 400))

pygame.font.init()

font1 = pygame.font.SysFont("Arial", 36)
font2 = pygame.font.SysFont("Arial", 40)

class Ship(pygame.sprite.Sprite):   
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("rocket.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        if self.rect.y > 400:
            self.rect.y = 0
        elif self.rect.y < 0:
            self.rect.y = 400
        elif self.rect.x > 500:
            self.rect.x = 0
        elif self.rect.x < 0:
            self.rect.x = 500


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("bullet.png"), (30, 30))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        self.rect.y -= 5


        if self.rect.y < 0:
            self.kill()



class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("asteroid.png"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        self.rect.y += 5
        if self.rect.y > 400:
            self.rect.y = 0

asteroid1 = Asteroid(10, 0)
asteroid2 = Asteroid(100, 0)
asteroid3 = Asteroid(150, 0)
asteroid_list = [asteroid1, asteroid2, asteroid3]
asteroids = pygame.sprite.Group(asteroid_list)
ship = Ship(200, 300)
bullet = Bullet(50, 370)
bullets = pygame.sprite.Group()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                ship.rect.x -= 5

            if keys[pygame.K_RIGHT]:
                ship.rect.x += 5

            if keys[pygame.K_UP]:
                ship.rect.y -= 5

            if keys[pygame.K_DOWN]:
                ship.rect.y += 5
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                keys = pygame.key.get_pressed()               
                if keys[pygame.K_SPACE]:
                    b = Bullet(ship.rect.x, ship.rect.y)
                    bullets.add(b)



    if finish == False:
        ship.update()
        asteroids.update()
        bullets.update()
    win.blit(back, (0,0))
    ship.draw(win)
    asteroids.draw(win)
    bullets.draw(win)

    pygame.sprite.groupcollide(bullets, asteroids, True, True)
    l = pygame.sprite.spritecollide(ship, asteroids, True)
    if len(l) > 0:
        finish = True
    elif len(asteroid_list) < 0:
        text_win = font2.render("VICTORY, YOU WIN", 1, (0, 255, 0))
        win.blit(text_win, (10, 20))
    if finish == True: 
        text_lose = font1.render("YOUR DEAD", 1, (255, 0, 0))
        win.blit(text_lose, (10, 20))


    pygame.display.update()
    clock.tick(60)














'''


import pygame

pygame.init()

win = pygame.display.set_mode((500, 400))
clock = pygame.time.Clock()

game_over = False
font = pygame.font.Font(None, 50)
lose_msg = font.render("YOU LOSE", False, (251, 15, 18))
win_msg = font.render("VICTORY", False, (80, 255, 40))

frame_count = 0
back = pygame.transform.scale(pygame.image.load("football.jpg"), (500, 400))
pacman = pygame.transform.scale(pygame.image.load("messi.jpg"), (60, 60))
pacman_rect = pacman.get_rect()
pacman_rect.x = 250
pacman_rect.y = 300
wall1 = pygame.Rect(0, 0, 10, 400)
wall2 = pygame.Rect(0, 0, 500, 10)
wall3 = pygame.Rect(0, 375, 500, 25)
wall4 = pygame.Rect(475, 0, 475, 500)

wall5 = pygame.Rect(0, 0, 25, 400)
wall6 = pygame.Rect(0, 0, 500, 25)
wall7 = pygame.Rect(0, 375, 500, 25)
wall8 = pygame.Rect(475, 0, 475, 500)

wall9 = pygame.Rect(0, 0, 25, 400)
wall10 = pygame.Rect(0, 0, 500, 25)
wall11 = pygame.Rect(0, 375, 500, 25)
wall12 = pygame.Rect(475, 0, 475, 500)

wall13 = pygame.Rect(225, 175, 50, 50)

walls = [wall1, wall2, wall3, wall4, wall13]

class Enemy():
    def __init__(self, x, y, moves):
        self.image = pygame.transform.scale(pygame.image.load("mbappe.jpg"), (50, 50))
        self.image = pygame.transform.scale(pygame.image.load("ramos.jpg"), (50, 50))
        self.image = pygame.transform.scale(pygame.image.load("ronaldo.jpg"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moves = moves
        self.idx = 0
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    def update(self):
        if self.moves[self.idx] == 'l':
            self.rect.x -=5
        elif self.moves[self.idx] == 'r':
            self.rect.x +=5

        self.idx += 1
        if self.idx >= len(self.moves):
            self.idx = 0
enemy1 = Enemy(200, 200, ['l', 'l', 'l', 'l', 'l', 'r', 'r', 'r', 'r', 'r'])
enemy2 = Enemy(100, 300, ['l', 'l', 'l', 'l', 'l', 'r', 'r', 'r', 'r', 'r'])
enemy3 = Enemy(300, 100, ['l', 'l', 'l', 'l', 'l', 'r', 'r', 'r', 'r', 'r'])
enemy_list = [enemy1, enemy2, enemy3]

class Food():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(pygame.image.load("burger.jpg"), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, surface):
        surface.blit(self.image, self.rect)

food1 = Food(200, 300)
food2 = Food(150, 100)
food3 = Food(450, 200)
food_list = [food1, food2, food3]


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if game_over == False:
        if keys[pygame.K_LEFT]:
            pacman_rect.x -= 5
            for w in walls:
                if pacman_rect.colliderect(w):
                    pacman_rect.x += 5

        if keys[pygame.K_RIGHT]:
            pacman_rect.x += 5
            for w in walls:
                if pacman_rect.colliderect(w):
                    pacman_rect.x -= 5

        if keys[pygame.K_UP]:
            pacman_rect.y -= 5
            for w in walls:
                if pacman_rect.colliderect(w):
                    pacman_rect.y += 5

        if keys[pygame.K_DOWN]:
            pacman_rect.y += 5
            for w in walls:
                if pacman_rect.colliderect(w):
                    pacman_rect.y -= 5

    for f in food_list:
        if pacman_rect.colliderect(f.rect):
            food_list.remove(f)
    frame_count += 1

    if frame_count >= 5:
        for e in enemy_list:
            e.update()
        frame_count = 0


    win.blit(back, (0,0))
    pygame.draw.rect(win, (0, 255, 0), wall1)
    pygame.draw.rect(win, (0, 255, 0), wall2)
    pygame.draw.rect(win, (0, 255, 0), wall3)
    pygame.draw.rect(win, (0, 255, 0), wall4)
    pygame.draw.rect(win, (0, 255, 0), wall13)
    win.blit(pacman, pacman_rect)
    for f in food_list:
        f.draw(win)
    for e in enemy_list:
        e.draw(win)
    for e in enemy_list:
        if pacman_rect.colliderect(e.rect):
            game_over = True
            win.blit(lose_msg, (190, 200))
    if len(food_list) == 0:
        game_over = True
        win.blit(win_msg, (190, 200))
        

    pygame.display.update()
    clock.tick(60)

'''