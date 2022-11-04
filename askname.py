import pygame as pg
def nik(scr):
    nik = True
    nicname = ""
    while nik:  # цикл ввода ника

        f = pg.font.SysFont('serif', 48)
        a = f.render('Youre name', False, (155, 55, 0))  # создание надписи введи имя
        scr.blit(a, (250, 100))  # прорисовка надписи введи имя на экране
        text_nik = f.render(nicname, False, (155, 55, 0))  # создание надписи ника игрока
        scr.blit(text_nik, (250, 250))  # вывод ника на экран

        for i in pg.event.get():  # цикл обработки событий
            if i.type == pg.QUIT:  # закрытие окна
                nik = False  # выход из цикла ввода ника
                run = False  # выход из основного цикла

            if i.type == pg.KEYDOWN:  # обработка событий нажатия клавишь
                if i.key == pg.K_RETURN and len(nicname) != 0:   # обработка нажатия на enter

                    nik = False  # выход из цикла ввода ника

                elif i.key == pg.K_BACKSPACE:  # обработка нажатия на backspace
                    scr = pg.display.set_mode((1350, 700))  # очищение экрана
                    nicname = nicname[0:len(nicname) - 1]  # удаление последнего символа
                    text_nik = f.render(nicname, False, (255, 0, 0))  # перезапись надписи ника
                    scr.blit(text_nik, (1100 / 2, 250))  # прорисовка ника

                elif len(nicname) < 14:  # ограничение 14 символов
                    nicname += i.unicode  # добавление символа нажатой кнопки в конец ника
        nic = f.render(nicname, False, (155, 55, 0))  # создание надписи введи имя
        scr.blit(nic, (250, 250))
        pg.display.flip()
    return nicname