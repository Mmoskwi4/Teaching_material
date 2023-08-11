from random import randint
"""Имортирует метод случайного значения"""
class Die():
    """Простая модель кубика"""
    def __init__(self, sides=6):
        """Определяет кубик и колличество граней"""
        self.sides = sides
    def roll_die(self, count_roll):
        """Брасаем кубик любое колличество раз и определяем выпавшие числа"""
        self.count_roll = count_roll
        side = int(self.sides)
        i = 0
        while i < self.count_roll:
            i += 1
            print(f'Ваше число: {randint(1, side)}')
roll = Die(20)
roll.roll_die(15)