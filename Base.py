import pygame as pg
import sqlite3 as sq

class Base:  # работа с базой данных
    """__init__ - создание базы, соединения и курсора
       create_table - создание таблицы
       insert - добавление информации в таблицу
       insert_into - добавление в определённое место
       give_something - получить счёт игрока по его нику
       all - запрос на данные из всей таблицы
       del - удаление соединения"""
    def __init__(self, name='qwer.db'):  # создание базы
        self.con = sq.connect(name)  # создание соединения
        self.cur = self.con.cursor()  # создание курсора
        self.create_table()  # создание таблицы

    def create_table(self, name='score'):  # создание таблицы
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS '{name}'(nic text, score int)""")  # создание таблицы score

    def insert(self, nic_us, score, name='score'):  # добавление
        self.cur.execute(f"""INSERT INTO {name} (nic, score) VALUES('{nic_us}', '{score}')
                            """)  # добавление данных в таблицу
        self.con.commit()  # сохранение изменений
    def insert_into(self, name_us, score, name = 'score'): # перезапись счёта игрока
        self.cur.execute(f"""
        UPDATE '{name}' SET score = '{score}' WHERE nic = '{name_us}'""")
        self.con.commit()   # сохранение изменений
    def give_something(self, nic_us, name = 'score'):   # получение счёта определённого игрока
        self.cur.execute(f"""SELECT score FROM '{name}' WHERE nic = '{nic_us}'""")   # выделение нужного
        return self.cur.fetchone()   # возврат счёта игрока
    def all(self, name='score'):  # получение данных таблицы
        self.cur.execute(f"SELECT * FROM {name}")  # выделение всей таблицы
        return self.cur.fetchall()  # возврат данных

    def __del__(self):  # закрытие соединения
        self.con.close()