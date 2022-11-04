import pygame as pg
class Gun():
    def __init__(self, screen): #Инициализация пушки

        self.screen = screen
        self.image = pg.image.load("image/1.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.center = float(self.rect.centerx)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self): #Прорисовывание пушки
        self.screen.blit(self.image, self.rect)

    def update_gun(self): #оБНОВЛЕНИЕ ПОЗИЦИИ ПУШКИ
            if self.mright and self.rect.right < self.screen_rect.right:
                self.center += 1.5
            elif self.mleft and self.rect.left > 0:
                self.center -= 1.5
            self.rect.centerx = self.center

    def create_gun(self): #Размещение пушки
        self.center = self.screen_rect.centerx