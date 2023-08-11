from random import choice
"""Имортирует метод случайного значения"""
class Lottery():
    """Простая модель лотерейного билета"""


    def __init__(self, count_letters, count_numbers):
        """Определяет лотерейный билет и значения в нём"""
        self.count_letters = count_letters
        self.count_numbers = count_numbers


    def generation_ticket(self):
        """Генерирует билет который содержит выйграшную комбинацию"""
        self.alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        let = 0
        num = 0
        self.lottery_ticket = []

        while let < self.count_letters:
            letter = choice(self.alph)
            self.lottery_ticket.append(letter)
            let += 1

        while num < self.count_numbers:
            number = choice(self.numbers)
            self.lottery_ticket.append(number)
            num += 1
        print(f'Билет с данный комбинацией является выйгрышным: {self.lottery_ticket}')


    def probability(self):
        """Цикл подбора билета, который содержит выйграшную комбинацию"""
        self.your_ticket = []
        self.count = 0



        while self.lottery_ticket != self.your_ticket:
            self.count += 1
            self.q = 0

            for l in range(self.count_letters):
                l = choice(self.alph)
                if l != self.lottery_ticket[self.q]:
                    self.your_ticket = []
                    break
                else:
                    self.your_ticket.append(l)
                    self.q += 1



                if len(self.your_ticket) == self.count_letters:
                    for n in range(self.count_numbers):
                        n = choice(self.numbers)
                        if n != self.lottery_ticket[self.q]:
                            self.your_ticket = []
                            break
                        else:
                            self.your_ticket.append(n)
                            self.q += 1


                    if self.lottery_ticket != self.your_ticket:
                        self.your_ticket = []

                    else:
                        print(f'Ваш билет совпал: {self.your_ticket}')
                        print(f'Колличество попыток, чтобы достать билет: {self.count}')

win_ticket = Lottery(4, 4)
win_ticket.generation_ticket()
win_ticket.probability()