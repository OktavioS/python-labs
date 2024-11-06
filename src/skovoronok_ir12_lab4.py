"""
Методи є приватними з позначкою '__' перед їх назвою, Захищені методи з позначкою '_' перед ними,
а публічні - просто назва
"""

class Shoes:
    def __init__(self, company_name = '', price = 0, size = 0, color = '', publicInteger = 0, publicString = ''):
        self.__company_name = company_name
        self.__price = price
        self.__size = size
        self.__color = color
        self.publicInteger = publicInteger
        self.publicString = publicString


    def get_comp_name(self):
        return self.__company_name

    def get_price(self):
        return self.__price

    def get_size(self):
        return self.__size

    def get_color(self):
        return self.__color

    def set_comp_name(self, company_name):
        self.__company_name = company_name

    def set_price(self, price):
        self.__price = price

    def set_size(self, size):
        self.__size = size

    def set_color(self, color):
        self.__color = color

    @ staticmethod
    def test():
        print('Hello')

    def __del__(self):
        print(f'\nОб\'єкт {self.__company_name} видалено\n'
              f'Об\'єкт {self.__price} видалено\n'
              f'Об\'єкт {self.__size} видалено\n'
              f'Об\'єкт {self.__color} видалено\n')



    def __str__(self):
        return f'\nName of the company: {self.__company_name}\n' \
               f'Price: {self.__price}€\n' \
               f'Size: {self.__size}\n' \
               f'Color: {self.__color}'

    def __repr__(self):
        return (f'Shoes(company name = {self.__company_name}, price = {self.__price}, size = {self.__size}, '
                f'color = {self.__color})')

def main():
    CP = Shoes('C.P. Company x Asics', 350, 44, 'Black; White')
    NB = Shoes('New Balance', 120, 41, 'Black; Grey')
    Nike = Shoes('Nike', 110, 43, 'Black; Grey; Yellow; Blue')

    print(CP)
    print(NB)
    print(Nike)

    print(f'Ціна кросівок C.P. Company: {CP.get_price()}€\n')
    CP.set_size(45)
    print(f'Розмір об\'єкта {CP.get_comp_name()} змінено на {CP.get_size()}')



main()