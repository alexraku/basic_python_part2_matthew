import os


def task1():
    # Способ 1:
    class NumSquares:
        def __init__(self, end_num: int):
            self.__end_num = end_num
            self.__num = 0

        def __iter__(self):
            self.__num = 0
            return self

        def __next__(self):
            self.__num += 1
            if self.__num > self.__end_num:
                raise StopIteration
            return self.__num ** 2

    squares_to20 = NumSquares(20)
    for num in squares_to20:
        print(num, end=" ")
    print()

    # Способ 2
    def squares(end_num: int):
        number = 1
        while number <= end_num:
            yield number ** 2
            number += 1

    for num in squares(20):
        print(num, end=" ")
    print()

    # Способ 3
    num_squares = (num ** 2 for num in range(1, 21))
    for num in num_squares:
        print(num, end=" ")


def task2():
    def gen_file_path(needed_dir, top=os.path.sep):
        all_dir = os.walk(top)
        for dir_path, dir_names, file_names in all_dir:
            if dir_path.endswith(needed_dir):
                for file in file_names:
                    yield os.path.join(dir_path, file)
                else:
                    break

    my_dir = "practical_work2_9_files"
    start = os.path.abspath(os.path.join("..", "..", "..", "..",
                                         "PycharmProjects"))
    # Можно убрать переменную start, тогда программа будет искать директорию
    # начиная с корневого диска, что увеличит время ее работы
    paths = gen_file_path(my_dir, start)
    print("Пути до файлов в директории practical_work2_9_files:")
    for path in paths:
        print("   ", path)


def task3():
    def file_lengths(my_dir):
        if os.path.exists(my_dir):
            file_list = os.listdir(my_dir)
            for my_file in file_list:
                if my_file.endswith(".py"):
                    with open(
                        os.path.join(my_dir, my_file), "r", encoding="utf-8"
                    ) as py_file:
                        line_count = 0
                        for line in py_file:
                            if not ("#" in line or line.isspace()):
                                line_count += 1
                        yield my_file, line_count
        else:
            print("Не существует директории по указаному пути.")

    print("Питоновские файлы в директории 4_list_comprehensions:")
    for file, num in file_lengths(os.path.join(
            "..", "..", "4_list_comprehensions")):
        print(f"    {file}  -  {num} строк")


def task4():
    class Node:
        def __init__(self, data, next_node=None):
            self.__data = data
            self.__next = next_node

        def get_data(self):
            return self.__data

        def get_next(self):
            return self.__next

        def set_next(self, new_next):
            self.__next = new_next

    class LinkedList:
        def __init__(self):
            self.__head = None
            self.__iter_start = False
            self.__cur_node = self.__head

        def __str__(self):
            if self.__head:
                list_str = "["
                node = self.__head
                while node.get_next():
                    list_str += f"{str(node.get_data())}, "
                    node = node.get_next()
                list_str += f"{str(node.get_data())}]"
                return list_str
            else:
                return "None"

        def __iter__(self):
            self.__cur_node = self.__head
            self.__iter_start = False
            return self

        def __next__(self):
            if not self.__iter_start:
                self.__iter_start = True
            else:
                new_node = self.__cur_node.get_next()
                if new_node:
                    self.__cur_node = new_node
                else:
                    raise StopIteration
            return self.__cur_node.get_data()

        def __find(self, node_i: int):
            if self.__head:
                node = self.__head
                index = 0
                while True:
                    if index == node_i:
                        return node
                    node = node.get_next()
                    if not node:
                        break
                    index += 1
            return None

        def append(self, data):
            new_node = Node(data)
            if self.__head:
                node = self.__head
                while node.get_next():
                    node = node.get_next()
                node.set_next(new_node)
            else:
                self.__head = new_node

        def get(self, node_i: int):
            node = self.__find(node_i)
            if node:
                return node.get_data()
            return None

        def remove(self, node_i: int):
            prev_node = self.__find(node_i - 1)
            node = prev_node.get_next()
            if node:
                prev_node.set_next(node.get_next())

    my_list = LinkedList()
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    print('Текущий список:', my_list)
    print('Получение третьего элемента:', my_list.get(2))
    print('Удаление второго элемента.')
    my_list.remove(1)
    print('Новый список:', my_list)


def task5():
    def error_log_generator(log_path):
        with open(log_path, "r") as r_file:
            for line in r_file:
                if "ERROR" in line:
                    yield line

    with open("errors.log", "w") as w_file:
        for error in error_log_generator("trading_operations.log"):
            w_file.write(error)


if __name__ == '__main__':
    task1()
    # task2()
    # task3()
    # task4()
    # task5()
