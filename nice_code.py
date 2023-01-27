"""Square calcuation."""

from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    if number >= 0:
        return sqrt(number)
    else:
        return 'Please type positive non-zero'


square_root = calculate_square_root(25.5)
print(message)
print(f'Мы вычислили квадратный корень из введённого вами числа.'
      f'Это будет: {square_root}')
