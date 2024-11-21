from random import choice, randint


def task1():
    class Warrior:
        def __init__(self, name):
            self.name = name
            self.health = 100

        def attack(self, enemy):
            if isinstance(enemy, Warrior):
                if enemy.health == 0:
                    print("Противник уже побежден!")
                else:
                    enemy.health -= 20
                    print(f"\n{self.name} наносит удар!\n"
                          f"{enemy.name} теряет 20 ОЗ. "
                          f"{enemy.health} ОЗ осталось")
                    if enemy.health == 0:
                        print(self.name, "победил!")
            else:
                print("Воин не станет бить того, кто сам воином не является!")

        def fight(self, enemy):
            warrior_list = [self, enemy]
            while (self.health > 0) and (enemy.health > 0):
                attacker = choice(warrior_list)
                defender = warrior_list[warrior_list.index(attacker) - 1]
                attacker.attack(defender)

    warrior1 = Warrior("Митька Большая Булава")
    warrior2 = Warrior("Владислав Длинный Меч")
    warrior1.fight(warrior2)


def task2():
    class Student:
        def __init__(self, name_surname, group, grades):
            self.name_surname = name_surname
            self.group = group
            self.grades = grades

    def average_grade(student):
        if isinstance(student, Student):
            grade_list = student.grades
            return sum(grade_list) / len(grade_list)

    student_list = [Student(
                    input("\nВведите имя и фамилию: "),
                    int(input("Номер группы: ")),
                    [int(input(f"Оценка {num + 1}: ")) for num in range(5)])
                    for _ in range(5)
                    ]
    sorted_list = sorted(student_list, key=average_grade)
    print("\nСписок студентов по возрастанию балла:")
    for elem in sorted_list:
        print(elem.name_surname)


def task3():
    class Child:
        def __init__(self, name, age, is_calm=True, is_hungry=False):
            self.name = name
            self.age = age
            self.is_calm = is_calm
            self.is_hungry = is_hungry

    class Parent:
        def __init__(self, name, age, child_list):
            self.name = name
            self.age = age
            if (not isinstance(child_list, list)) or len(child_list) == 0:
                raise ValueError("Ошибка ввода списка детей.")
            for child in child_list:
                if self.age - child.age < 16:
                    raise ValueError("Ошибка возраста ребёнка или родителя.")
            self.child_list = child_list

        def info(self):
            print(f"Имя: {self.name}\nВозраст: {self.age}, "
                  f"Список детей: {[child.name for child in self.child_list]}")

        def is_my_child(self, child):
            if isinstance(child, Child) and (child in self.child_list):
                return True
            else:
                print(f"{child.name} - не ребенок данного родителя!")
                return False

        def calm_child(self, child):
            if self.is_my_child(child):
                if not child.is_calm:
                    child.is_calm = True
                    print(f"{child.name} успокоился(ась).")
                else:
                    print("Ребенок уже спокоен.")

        def feed_child(self, child):
            if self.is_my_child(child):
                if child.is_hungry:
                    print(child.name, "накормлен(а).")
                    child.is_hungry = False
                else:
                    print("Ребенок не голоден.")

    child1 = Child("Майя", 12, is_calm=False)
    child2 = Child("Матвей", 15, is_hungry=True)
    child3 = Child("Денис", 15, is_calm=False, is_hungry=True)
    parent1 = Parent("Алексей", 40, [child1, child2])
    # Демонстрация работы методов класса "Родитель":
    parent1.info()
    parent1.calm_child(child1)
    parent1.calm_child(child2)
    parent1.feed_child(child1)
    parent1.feed_child(child2)
    parent1.feed_child(child3)


def task4():
    class Water:
        def __add__(self, other):
            if isinstance(other, Air):
                return "Storm"
            if isinstance(other, Fire):
                return "Steam"
            if isinstance(other, Earth):
                return "Mud"
            if isinstance(other, Plant):
                return "Growth"
            else:
                return "Error: able to add only other elements"

    class Air:
        def __add__(self, other):
            if isinstance(other, Water):
                return "Storm"
            if isinstance(other, Fire):
                return "Lightning"
            if isinstance(other, Earth):
                return "Dust"
            if isinstance(other, Plant):
                return "Pollination"
            else:
                return "Error: able to add only other elements"

    class Fire:
        def __add__(self, other):
            if isinstance(other, Water):
                return "Steam"
            if isinstance(other, Air):
                return "Lightning"
            if isinstance(other, Earth):
                return "Lava"
            if isinstance(other, Plant):
                return "Burning"
            else:
                return "Error: able to add only other elements"

    class Earth:
        def __add__(self, other):
            if isinstance(other, Water):
                return "Mud"
            if isinstance(other, Air):
                return "Dust"
            if isinstance(other, Earth):
                return "Lava"
            if isinstance(other, Plant):
                return "Sprout"
            else:
                return "Error: able to add only other elements"

    class Plant:
        def __add__(self, other):
            if isinstance(other, Water):
                return "Growth"
            if isinstance(other, Air):
                return "Pollination"
            if isinstance(other, Fire):
                return "Burning"
            if isinstance(other, Earth):
                return "Sprout"
            else:
                return "Error: able to add only other elements"

    element1 = Water()
    element2 = Plant()
    print(element1 + element2)
    print(element1 + "jkhs")


def task5():
    class House:
        food = 50
        money = 0

    class Person:
        def __init__(self, name, house):
            self.fullness = 50
            self.name = name
            if isinstance(house, House):
                self.house = house
            else:
                raise ValueError("This is not a house.")

        def eat(self):
            self.house.food -= 5
            self.fullness += 5

        def work(self):
            self.fullness -= 5
            self.house.money += 5

        def play(self):
            self.fullness -= 5

        def buy_food(self):
            self.house.money -= 6
            self.house.food += 5

        def live_a_day(self):
            if self.fullness < 0:
                raise ValueError(f"{self.name} is ded becos hungr :(")
            dice = randint(1, 6)
            if (self.fullness < 20) and (self.house.food > 0):
                self.eat()
            elif (self.house.food < 10) and (self.house.money > 0):
                self.buy_food()
            elif self.house.money < 50:
                self.work()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            else:
                self.play()

    print("Experiment start!")
    my_house = House()
    person1 = Person("Matvey", my_house)
    person2 = Person("Alexey", my_house)
    try:
        for _ in range(365):
            person1.live_a_day()
            person2.live_a_day()
    except ValueError:
        print("Experiment unsuccessful. You should better get a cat, maybe")
        raise
    print("Experiment successful! You can finally stop being afraid of "
          "living with someone!")
    print(f"{my_house.money}, {my_house.food}\n"
          f"{person1.name}: {person1.fullness}\n"
          f"{person2.name}: {person2.fullness}")


def task6():
    class Cell:
        def __init__(self, index):
            self.index = index
            self.is_empty = True
            self.sign = " "

    class Board:
        cells = [Cell(cell_i) for cell_i in range(9)]

        def change_cell(self, cell_i, sign):
            if self.cells[cell_i - 1].is_empty:
                self.cells[cell_i - 1].is_empty = False
                self.cells[cell_i - 1].sign = sign
                return True
            else:
                print("Эта клетка уже занята")
                return False

        def winner(self):
            wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                    [2, 5, 8], [0, 4, 8], [2, 4, 6]]
            for sign in ["X", "O"]:
                for var in wins:
                    if self.cells[var[0]].sign == sign and \
                       self.cells[var[1]].sign == sign and \
                       self.cells[var[2]].sign == sign:
                        return sign
            if all([not cell.is_empty for cell in self.cells]):
                return "!"
            else:
                return None

    class Player:
        def __init__(self, name):
            self.name = name
            self.wins = 0

        def make_a_turn(self):
            while True:
                cell = input("В какую клетку сходить? ")
                if cell.isdigit() and len(cell) == 1:
                    return int(cell)
                else:
                    print("Неверный ввод. Введите номер клетки от 1 до 9")

    class Game:
        def __init__(self, board, players: list):
            if len(players) == 2 and all([isinstance(my_player, Player)
                                          for my_player in players]):
                self.players = players
            self.board = board

        def print_board(self):
            print("\n{10}   1   |   2   |   3\n{10}   {1}   |   {2}   |   {3}"
                  "\n{10}       |       |\n{10}{0}\n"
                  "{10}   4   |   5   |   6\n{10}   {4}   |   {5}   |   {6}"
                  "\n{10}       |       |\n{10}{0}\n"
                  "{10}   7   |   8   |   9\n{10}   {7}   |   {8}   |   {9}"
                  "\n{10}       |       |".format(
                   "-" * 23,
                   self.board.cells[0].sign,
                   self.board.cells[1].sign,
                   self.board.cells[2].sign,
                   self.board.cells[3].sign,
                   self.board.cells[4].sign,
                   self.board.cells[5].sign,
                   self.board.cells[6].sign,
                   self.board.cells[7].sign,
                   self.board.cells[8].sign,
                   " "*8
                  ))

        def one_turn(self, player: Player):
            if self.players.index(player) == 0:
                sign = "X"
            else:
                sign = "O"
            print(f"\nХодит {player.name} ({sign})")
            while True:
                cell = player.make_a_turn()
                if self.board.change_cell(cell, sign):
                    self.print_board()
                    break

        def one_game(self):
            flag = True
            while flag:
                for player in self.players:
                    self.one_turn(player)
                    winner = self.board.winner()
                    if winner == "!":
                        print("Ничья!")
                        flag = False
                        break
                    elif winner:
                        print("Победил", player.name)
                        player.wins += 1
                        flag = False
                        break

        def start(self):
            print(f'{" " * 10}| Крестики-нолики |')
            flag = True
            game_num = 1
            while flag:
                print(f'\n{" " * 15}|Игра  {game_num}|')
                self.print_board()
                self.one_game()
                print("\nКол-во побед: ")
                for player in self.players:
                    print(f"{player.name}: {player.wins}")
                while True:
                    game_choice = input("Продолжаем? да/нет: ")
                    if game_choice.lower() == "нет":
                        print("Выключение игры...")
                        flag = False
                        break
                    elif game_choice.lower() == "да":
                        for cell in self.board.cells:
                            cell.sign = " "
                            cell.is_empty = True
                        self.players = self.players[::-1]
                        game_num += 1
                        break
                    else:
                        print("Неправильный ввод. Попробуйте еще раз")

    board1 = Board()
    p1 = Player("matwew")
    p2 = Player("lox")
    game1 = Game(board1, [p1, p2])
    game1.start()


def task7():
    class Matrix:
        def __init__(self, rows, columns):
            self.rows = rows
            self.columns = columns
            self.__data = list()

        @property
        def data(self) -> list:
            return self.__data

        @data.setter
        def data(self, mtrx: list):
            if not isinstance(mtrx, list):
                raise ValueError(f"Значение передаваемое в матрицу должно "
                                 f"быть списком.")
            if isinstance(mtrx, list) and len(mtrx) != self.rows:
                raise ValueError(f"Количество строк должно быть {self.rows}. "
                                 f"Матрица не записана.")

            for row in mtrx:
                if not isinstance(row, list):
                    raise ValueError(f"Значение передаваемое в матрицу должно "
                                     f"быть списком списков.")
                if len(row) != self.columns:
                    raise ValueError(f"Количество столбцов должно быть "
                                     f"{self.columns}. Матрица не записана.")
            self.__data = mtrx

        def __str__(self):
            mtrx_str = "\n".join(["\t".join([str(num) for num in row])
                                 for row in self.data])
            return mtrx_str

        def __add__(self, other):
            if not (self.rows == other.rows and
                    self.columns == other.columns):
                raise ValueError("Матрицы непригодны для умножения.")
            a_mtrx = Matrix(self.rows, self.columns)
            a_data = []
            for row1, row2 in zip(self.data, other.data):
                row_data = []
                for num1, num2 in zip(row1, row2):
                    row_data.append(num1 + num2)
                a_data.append(row_data)
            a_mtrx.data = a_data
            return a_mtrx

        def __sub__(self, other):
            if not (self.rows == other.rows and
                    self.columns == other.columns):
                raise ValueError("Матрицы непригодны для умножения.")
            s_mtrx = Matrix(self.rows, self.columns)
            s_data = []
            for row1, row2 in zip(self.data, other.data):
                row_data = []
                for num1, num2 in zip(row1, row2):
                    row_data.append(num1 - num2)
                s_data.append(row_data)
            s_mtrx.data = s_data
            return s_mtrx

        def transpose(self) -> "Matrix":
            t_data = list()
            t_mtrx = Matrix(self.columns, self.rows)
            for _ in range(self.columns):
                t_data.append([])
            for row in self.data:
                for index, column in enumerate(row):
                    t_data[index].append(column)
            t_mtrx.data = t_data
            return t_mtrx

        def __mul__(self, other) -> "Matrix":
            other_mtrx = other.transpose()
            if not (self.rows == other_mtrx.rows and
                    self.columns == other_mtrx.columns):
                raise ValueError("Матрицы непригодны для умножения.")
            min_val = min(self.rows, self.columns)
            m_mtrx = Matrix(min_val, min_val)
            m_data = []
            row_index = 0
            for row1 in self.data:
                m_data.append([])
                for row2 in other_mtrx.data:
                    row_sum = 0
                    for num1, num2 in zip(row1, row2):
                        row_sum += num1 * num2
                    m_data[row_index].append(row_sum)
                row_index += 1
            m_mtrx.data = m_data
            return m_mtrx

    m1 = Matrix(2, 3)
    m1.data = [[1, 2, 3], [4, 5, 6]]
    m2 = Matrix(2, 3)
    m2.data = [[7, 8, 9], [10, 11, 12]]
    print(f"Матрица 1:\n{m1}")
    print(f"\nМатрица 2:\n{m2}")
    print(f"\nСумма матриц:\n{m1 + m2}")
    print(f"\nРазность матриц:\n{m1 - m2}")

    m3 = Matrix(3, 2)
    m3.data = [[1, 2], [3, 4], [5, 6]]
    print(f"\nМатрица 3:\n{m3}")
    print(f"\nПроизведение матриц 1 и 3:\n{m1 * m3}")
    print(f"\nТранспонирование матрицы 1:\n{m1.transpose()}")


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    task7()
