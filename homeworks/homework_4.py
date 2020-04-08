from sys import argv
from func_home_4 import calc_employee, func_com, fact
from functools import reduce
from itertools import count, cycle, groupby
'''
#Задание 1:
# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.



try:
    script_name, prod, rate, prize = argv
    name_script = script_name
    result = calc_employee(prod, rate, prize)
    print(f'Salary of an employee (including bonus) is: {result}')
except ValueError:
    print('Parameters entered incorrectly!')
    print(f'To start use the command: python homework_4.py [production in hours] [rate per hour] [bonus]')
#######################################################################################################################
#Задание 2:
#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
#Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.

my_list = [2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 10, 15, 14, 16]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(new_list)
#######################################################################################################################
#Задание 3:
#Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
#Подсказка: использовать функцию range() и генератор.

my_list = [elem for elem in range(20, 241)]
print([elem for elem in my_list if elem % 20 == 0 or elem % 21 == 0])
#######################################################################################################################
#Задание 4:
#Представлен список чисел.
# Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

my_list = [5, 5, 1, 2, 3, 4, 3, 3, 3, 4, 6, 6, 6, 7, 8, 9, 10, 10]
new_list = sorted(set(my_list), key=lambda d: my_list.index(d))
print(new_list)
#######################################################################################################################
# Задание 5:
#Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
#Подсказка: использовать функцию reduce().

my_list = [num for num in range(100, 1001) if num%2 == 0]
print(reduce(func_com, my_list))
#######################################################################################################################
#Задание 6:
#Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'abc', 'cba']
# а):
for i in count(1):
    print(i)
# б):
for elem in cycle(my_list):
    print(elem)
#######################################################################################################################
#Задание 7:
#Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые 15 чисел.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

n = int(input('Введите число, факториал которого нужно найти: '))
for num, elem in enumerate(fact(n)):
    print(elem)
    if num == 13:
        break
'''