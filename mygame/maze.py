#создай игру "Лабиринт"!
from pygame import * 


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (40, 40))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def clear(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < (height - self.rect.height - 5):
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < (width - self.rect.width - 5):
            self.rect.x += self.speed


class Player2(GameSprite):
    direction = 'left'

    def update(self):
        if self.rect.x >= 620:
            self.direction = 'left'
        if self.rect.x <= 520:
            self.direction = 'right'
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

class wall(sprite.Sprite):
    def __init__(self, width, height, x, y, color):
        super().__init__()
        self.image = Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

width, height = 700, 500
window = display.set_mode((width, height))
display.set_caption('MAZE:Лабиринт')

sprite1 = Player(('run.png'), 0, 100, 5)
sprite2 = Player2(('dino.png'),620, 300, 2)
tres = GameSprite(('tres.png'), 600, 450, 0)
background = transform.scale(image.load('fon.jpg'), (width, height))

w1 = wall(405, 10, 100, 20, (108, 80, 134))
w2 = wall(10, 200, 100, 20, (108, 80, 134))
w3 = wall(10,300,500,150,(108, 80, 134))
w4 = wall(10, 350, 250, 100, (108, 80, 134))
w5 = wall(80, 10, 175, 100, (108, 80, 134))
w6 = wall(400, 10, 100, 440, (108, 80, 134))
w7 = wall(10, 300, 350, 25, (108, 80, 134))

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

def check_lose():
    if sprite.collide_rect(sprite1, w1): return True
    if sprite.collide_rect(sprite1, w2): return True
    if sprite.collide_rect(sprite1, w3): return True
    if sprite.collide_rect(sprite1, w4): return True
    if sprite.collide_rect(sprite1, w5): return True
    if sprite.collide_rect(sprite1, w6): return True
    if sprite.collide_rect(sprite1, sprite2): return True
    return False

def check_win():
    if sprite.collide_rect(sprite1, tres): return True
    return False

font.init()
my_font  = font.SysFont("Arial", 70)
# my_font  = font.Font(None, 70)
win = my_font.render('Действительно победил?', True, (220, 220, 220), (0,0,0))
los = my_font.render('Попался?', True, (220, 220, 220), (0,0,0))


clock = time.Clock()
FPS = 60

game = True
finish = False
while game:
    if not finish:
        window.blit(background, (0, 0))
        sprite1.update()
        sprite1.clear()
        sprite2.update()
        sprite2.clear()
        tres.clear()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        if check_lose():
            result = los
            finish = True
        if check_win():
            result = win
            finish = True
    else:
        window.blit(result, (50, 200))

    for e in event.get():
        if e.type == QUIT:
            game = False

    clock.tick(FPS)
    display.update()