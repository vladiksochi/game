import pygame as pg
import sys
import controls
from gun import Gun
from pygame.sprite import Group
from bullet import Bullet
from stats import Stats
from scores import Scores
import sqlite3 as sq
from askname import nik




def run():
    pg.init()
    screen = pg.display.set_mode((700, 700))
    pg.display.set_caption("Вселенская битва")
    bg_color = (0, 0, 0)
    nik(screen)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)


    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            bullets.update()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, gun, inos, bullets)



nickname = run()
if len(nickname) == 0:
    sys.exit()

