import pygame as pg

class Ino(pg.sprite.Sprite):#Класс пришельца

    def __init__(self, screen): #Инициализация и определение начальной позиции
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pg.image.load("image/ino.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self): #Вывод пришельца на экран
        self.screen.blit(self.image, self.rect)

    def update(self): #Передвижение пришельцев
        self.y += 0.1
        self.rect.y = self.y
