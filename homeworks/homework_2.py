'''
#Задание 1:

#Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_num = 20
my_num_str = '20'
my_dict = {
    'name': 'Vasya',
    'age': 20,
    'surname': 'Pupkin'
}
my_list = [9, 23.01, ['a', my_num, my_num_str], 'str', True, (1, 2, 3, 4, 5), my_dict]
for elem in my_list:
    print(elem)
    print(type(elem))
print('Выполнено')
#########################################################################################
#Задание 2:

#Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = list(input('Введите числа: '))
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
    print(i)
print(f'Список: {my_list}')
#########################################################################################
#Задание 3:

#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
my_dict = {
    '1': 'Зима',
    '2': 'Зима',
    '3': 'Весна',
    '4': 'Весна',
    '5': 'Весна',
    '6': 'Лето',
    '7': 'Лето',
    '8': 'Лето',
    '9': 'Осень',
    '10': 'Осень',
    '11': 'Осень',
    '12': 'Зима'
}
month = input('Введите номер месяца: ')
print(f'{month}-й номер месяца - это {my_dict[month]}')
#Решение через list:
seasons_list = ['',
                'Зима',
                'Зима',
                'Весна',
                'Весна',
                'Весна',
                'Лето',
                'Лето',
                'Лето',
                'Осень',
                'Осень',
                'Осень',
                'Зима'
]
month = int(input('Введите номер месяца: '))
print(f'{month}-й номер месяца - это {seasons_list[month]}')
#########################################################################################
#Задание 4:

#Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.
my_str = input('Введите строку: ')
for num, elem in enumerate(my_str.split(' '), 1):
    print(num, elem[:10])
#########################################################################################
#Задание 5:

#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
my_list.append(int(input('Введите новый элемент рейтинга: ')))
print(sorted(my_list, reverse=True))
#########################################################################################
#Задание 6:

# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик,
# например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Выход - q \nЛюбая клавиша - продолжить: ') == 'q':
        break
    num += 1
    for f in features.keys():
        user_data = input('{}: '.format(f))
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(features[f])
    goods.append((num, features))
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)
'''