import random


class Riddler:
    tries = ['попыток', 'попытка', 'попытки']

    def __init__(self):
        self.riddles = {'Маленький, серенький, на слона похож.': 'слоненок',
                        'Над нами кверху ногами.': 'таракан',
                        'Cиний, большой, с усами и полностью набит зайцами.': 'троллейбус'}

    def add_riddle(self, riddle: str, answer: str):
        """ Добавляет загадку в словарь """
        if not isinstance(riddle, str) or not isinstance(answer, str):
            print('Wrong type!!')
            return
        self.riddles[riddle] = answer

    def riddle(self):
        """ Печатает текст загадки и проверяет правильность ответов """
        question = random.choice(list(self.riddles.keys()))
        print('Загадка: ' + question)
        print('У вас 3 попытки!')
        for i in range(3, 0, -1):
            answer = input()
            if answer == self.riddles[question]:
                print('Правильно!!!')
                return True
            print(f'У вас {i - 1} {self.tries[i - 1]}!')
        print('Правильный ответ: ' + self.riddles[question])
        return False


def main():
    riddler = Riddler()
    riddler.riddle()


if __name__ == '__main__':
    main()
