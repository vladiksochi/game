import pygame as pg

class Bullet(pg.sprite.Sprite):
    def __init__(self, screen, gun): #Создание пули
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect (0, 0, 2, 12)
        self.color = 153, 217, 234
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)


    def update(self): #Перемещение пули вверх
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self): #Прорисовка пули
        pg.draw.rect(self.screen, self.color, self.rect)