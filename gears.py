from pygame import *

class GameSprite (sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_y, player_speed_x):
        #?вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)


        #*каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed_y = player_speed_y
        self.speed_x = player_speed_x

        #*каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    #?метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#TODO Создаём класс игрока
class Cammer(GameSprite):
    #*метод для управления спрайтом стрелками клавиатуры
    def update(self):
        global x_fon
        global y_fon
        keys = key.get_pressed()
        if keys[K_a]:
            x_fon += self.speed_x
        if keys[K_d]:
            x_fon -= self.speed_x
        if keys[K_w] :
            y_fon += self.speed_y
        if keys[K_s]:
            y_fon -= self.speed_y

window = display.set_mode((700, 700))
display.set_caption('Gears')
background = transform.scale(image.load("background.png"), (2400, 1400))

game = True
x_fon = 0
y_fon = 0
cam = Cammer(('player.png'), 300, 300, 100, 100, 3, 3)
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False

    window.blit(background, (x_fon, y_fon))
    cam.reset()
    
    cam.update()
    display.update()