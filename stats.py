class Stats(): #Отслеживание статистики

    def __init__(self): #Инициализация статистики
        self.reset_stats()
        self.run_game = True


    def reset_stats(self): #Изменяющаяся статистика
        self.guns_left = 2
        self.score = 0
