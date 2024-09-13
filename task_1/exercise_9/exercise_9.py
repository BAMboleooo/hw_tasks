import time
import tracemalloc
from abc import ABC, abstractmethod

"""
№ 1 Написать класс, использующий наследование и полиморфизм. 

Создайте систему для управления поведением различных домашних животных,
используя принципы объектно-ориентированного программирования (ООП) и инкапсуляцию.
В этой системе вы должны определить абстрактный класс для животных, а затем создать конкретные реализации для собак, кошек и попугаев.
Каждое животное должно иметь возможность изменять своё настроение, уровень голода и усталости, а также взаимодействовать с игрушками.

Абстрактный класс Animal:

Создайте абстрактный класс Animal с полями для имени, настроения, голода и усталости.
Используйте инкапсуляцию с помощью свойства (property) для управления доступом к полям настроения, голода и усталости.
Определите абстрактный метод speak, который должен быть реализован в подклассах.
Реализуйте методы feed, rest и play, которые изменяют уровень голода и усталости, а также изменяют настроение и выводят сообщение о действиях.

Классы-потомки:

Создайте классы Dog, Cat и Parrot, наследующие от Animal.
Каждый класс должен реализовать метод speak, который возвращает строку в зависимости от уровня голода, усталости и настроения.

Класс Toy:

Реализуйте класс Toy, который будет представлять игрушку.
Игрушка должна иметь имя и булево значение, указывающее, является ли она интересной (fun).
"""
class Animal(ABC):
    pass

class Dog(Animal):
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        pass


class Parrot(Animal):
    def speak(self):
        pass


class Toy:
    pass


"""
№ 2 Написать класс с использованием магических методов (__str__, __len__, __getitem__).

для __len__ выводить длину объекта

для __str__ выводить `MyContainer with длина объекта items`

для __getitem__ выводить значение по индексу
"""
class MyContainer:
    pass


"""
№ 3 Реализация Менеджера Файлов

Напишите класс FileManager, который реализует интерфейс контекстного менеджера для работы с файлами.
Класс должен использовать методы __enter__ и __exit__ для открытия и закрытия файла.

Класс FileManager должен быть инициализирован с двумя параметрами:

filename (строка): Имя файла, с которым будет производиться работа.
mode (строка): Режим открытия файла (например, 'r' для чтения, 'w' для записи и т.д.).

При создании экземпляра класса FileManager файл не должен открываться немедленно.
Файл должен открываться только при входе в контекстный менеджер.

Метод __enter__ должен открывать файл с использованием переданного режима и возвращать объект файла.

Метод __exit__ должен закрывать файл при выходе из контекста.
Он должен принимать параметры, соответствующие стандартному интерфейсу метода __exit__,
но эти параметры не должны использоваться в реализации метода.
"""
class FileManager:
    pass


"""
№ 4 Напишите функцию, которая принимает два аргумента:

lst: Вложенный список (список, содержащий другие списки и/или элементы).
tpl: Вложенный кортеж (кортеж, содержащий другие кортежи и/или элементы).

Внутри функции:

Измерьте время выполнения операции изменения всех элементов во вложенном списке lst следующим образом:

Напишите внутреннюю рекурсивную функцию modify_list(l), которая изменяет все элементы вложенного списка l на строку "modified".
Если элемент сам является списком, рекурсивно вызывайте modify_list.
Запишите время выполнения этой операции.
Затем, измерьте время выполнения попытки изменения всех элементов во вложенном кортеже tpl следующим образом:

Напишите внутреннюю рекурсивную функцию modify_tuple(t), которая изменяет все элементы вложенного кортежа t на строку "modified".
Если элемент сам является кортежем, рекурсивно вызывайте modify_tuple.
Поскольку кортежи в Python неизменяемы, это должно вызвать исключение TypeError.
Функция должна возвращать кортеж, содержащий:

Изменённый список lst.
Сообщение об ошибке, возникшей при попытке изменения кортежа.
Время, затраченное на изменение списка.
Время, затраченное на попытку изменения кортежа.
"""


def list_tuple_operations_deep(lst, tpl):
    start_list = time.time()

    pass


"""
№ 5 Напишите функцию, которая принимает большое число n и возвращает квадраты всех чисел от 1 до n как с использованием списка,
так и с использованием генератора. Измерьте память с помощью tracemalloc.get_traced_memory(), занимаемую каждым подходом.
"""


def square_numbers(n):
    return pass # решение в 1 строку


def square_numbers_generator(n):
    pass


def memory_usage_comparison(n):
    tracemalloc.start()

    pass