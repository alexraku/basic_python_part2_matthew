from random import randint, choice
from math import pi
from abc import ABC, abstractmethod


def task1():
    class Property:
        def __init__(self, worth):
            self.__worth = worth

        def get_worth(self):
            return self.__worth

        def tax(self):
            pass

    class Apartment(Property):
        def tax(self):
            my_tax = self.get_worth() / 1000
            return my_tax

    class Car(Property):
        def tax(self):
            my_tax = self.get_worth() / 200
            return my_tax

    class CountryHouse(Property):
        def tax(self):
            my_tax = self.get_worth() / 500
            return my_tax

    money = int(input("Сколько у вас денег? "))
    price = int(input("Сколько стоит ваше имущество? "))
    while True:
        my_choice = input("Выберите тип имущества:"
                          "\n  1)Квартира\n  2)Автомобиль\n  3)Дача \n> ")
        if my_choice == "1":
            my_property = Apartment(price)
            break
        elif my_choice == "2":
            my_property = Car(price)
            break
        elif my_choice == "3":
            my_property = CountryHouse(price)
            break
        else:
            print("Неправильный ввод.\n")
    tax = my_property.tax()
    print("Ваш налог:", tax)
    if money >= tax:
        print("Поздравляем! Вы можете оплатить налоги!")
    else:
        difference = tax - money
        print(f"К сожалению, вам не хватает {difference} для оплаты налогов.")


def task2():
    class KillError(Exception):
        pass

    class DrunkError(Exception):
        pass

    class CarCrashError(Exception):
        pass

    class GluttonyError(Exception):
        pass

    class DepressionError(Exception):
        pass

    def one_day():
        if randint(1, 10) == 4:
            raise choice([KillError("Совершил убийство (-50 от кармы)"),
                          DrunkError("Напился (-10 от кармы)"),
                          CarCrashError("Вызвал ДТП (-20 от кармы)"),
                          GluttonyError("Придался обжорству (-5 от кармы)"),
                          DepressionError("Впал в депрессию от такой "
                                          "жизни (просто грустно)")
                          ])
        return randint(1, 7)

    karma = 0
    with open("karma.log", "w", encoding="utf-8") as file:
        while karma < 500:
            try:
                karma += one_day()
            except KillError as exc:
                karma -= 50
                file.write(f"{exc}\n")
            except DrunkError as exc:
                karma -= 10
                file.write(f"{exc}\n")
            except CarCrashError as exc:
                karma -= 20
                file.write(f"{exc}\n")
            except GluttonyError as exc:
                karma -= 5
                file.write(f"{exc}\n")
            except DepressionError as exc:
                file.write(f"{exc}\n")
        else:
            print("Достиг просветления")


def task3():
    class MyDict(dict):
        """
        Класс, наследующий все свои свойства от dict, за исключением метода get
        """
        def get(self, __key):
            """
            Немного измененный метод словарей get

            :return: __key если он присутствует в словаре
                     0 в ином случае
            :rtype: int, str, tuple или bool
            """
            if __key not in self:
                return 0
            else:
                return self[__key]

    my_dict = MyDict()
    my_dict["232"] = 343
    my_dict["s"] = 666
    print(my_dict.get("s"))
    print(my_dict.get("234"))


# Задание 4 нужно запускать из файла game.py


def task5():
    class Stack:
        def __init__(self):
            self.__content = []

        def __str__(self):
            return '; '.join(self.__content)

        def __len__(self):
            return len(self.__content)

        def get_content(self):
            return self.__content

        def push(self, new_elem):
            self.__content.append(new_elem)

        def pop(self):
            if self.__content:
                return self.__content.pop(-1)
            else:
                return None

    class TaskManager:
        def __init__(self):
            self.__tasks = dict()

        def do_task(self):
            if self.__tasks:
                needed_priority = min(self.__tasks)
                task = self.__tasks[needed_priority].pop()
                print(f"\nЗадача выполнена - {task}")
                if len(self.__tasks[needed_priority]) == 0:
                    self.__tasks.pop(needed_priority)
            else:
                print("\nСписок задач пустой, нечего выполнять.")

        def new_task(self, task, priority):
            if priority not in self.__tasks:
                self.__tasks[priority] = Stack()
            self.__tasks[priority].push(task)

        def __str__(self):
            result = "\n".join([f"{key} - {value}" for key, value in
                               sorted(self.__tasks.items())])
            if result:
                return result
            else:
                return "Список задач пуст."

    manager = TaskManager()
    manager.new_task("сделать уборку", 4)
    manager.new_task("помыть посуду", 4)
    manager.new_task("отдохнуть", 1)
    manager.new_task("поесть", 2)
    manager.new_task("сдать ДЗ", 2)
    print(f"Задачи:\n{manager}")
    for _ in range(6):
        manager.do_task()
        print(f"\nОставшиеся задачи:\n{manager}")


def task6():
    class Shape(ABC):
        @abstractmethod
        def area(self, *args):
            pass

    class Circle(Shape):
        def area(self, radius):
            area = pi * radius ** 2
            return area

    class Rectangle(Shape):
        def area(self, side1, side2):
            area = side1 * side2
            return area

    class Triangle(Shape):
        def area(self, base, height):
            area = base * height / 2
            return area

    shape1 = Circle()
    print("Площадь круга:", shape1.area(5))
    shape2 = Rectangle()
    print("Площадь прямоугольника:", shape2.area(5, 2))
    shape3 = Triangle()
    print("Площадь треугольника:", shape3.area(3, 5))
    # shape4 = Shape()


if __name__ == '__main__':
    task1()
    # task2()
    # task3()
    # task5()
    # task6()
