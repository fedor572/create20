from random import choice
first = 'Мама мыла раму'
second = 'Рамена мало было'
my_func = lambda x,y:  x == y
result = list(map(my_func,first, second))
print(result)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w') as f:
            for data in data_set:
                f.write(f'{data}\n')
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Возможно', 'Определенно')
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())
print(first_ball())