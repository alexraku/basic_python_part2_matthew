from random import randint


def task1():
    """
    Есть файл people.txt, в котором построчно хранится N имён пользователей.
    Напишите программу, которая берёт количество символов в каждой строке файла
    и в качестве ответа выводит общую сумму. Если в какой-либо строке меньше
    трёх символов (не считая литерала \n), то вызывается ошибка и сообщение, в
    какой именно строке она возникла. Программа при этом не завершается и
    обрабатывает все имена файла.
    Также при желании можно вывести все ошибки в отдельный файл errors.log.
    """
    with open("people.txt", "r", encoding="utf-8") as people_file:
        with open("errors.log", "w") as errors_file:
            sym_count = 0
            for line_num, line in enumerate(people_file):
                try:
                    line_len = len(line.strip())
                    if line_len < 3:
                        raise ValueError("name length less than three letters")
                    sym_count += line_len
                except ValueError as exc:
                    errors_file.write(f"line {line_num + 1}: {exc}\n")
    print("Общее кол-во символов:", sym_count)


def task2():
    """
    Напишите программу, которая запрашивает у пользователя число до тех пор,
    пока сумма запрашиваемых чисел не станет больше либо равна 777. Каждое
    введённое число при этом дозаписывается в файл out_file.txt. Сделайте так,
    чтобы перед дозаписью программа с вероятностью 1 к 13 выдавала пользователю
    случайное исключение и завершалась.
    """
    with open("out_file.txt", "w") as file:
        num_sum = 0
        while num_sum < 777:
            try:
                num = int(input("Введите число: "))
                if randint(1, 13) == 7:
                    raise NameError
                num_sum += num
                file.write(f"{num}\n")
            except ValueError:
                print("\nОшибка ввода. Попробуйте ещё раз\n")
            except NameError:
                print("Вас постигла неудача!")
                break
        else:
            print("Вы успешно выполнили условие для "
                  "выхода из порочного цикла!")


def task3():
    """
    У вас есть файл с протоколом регистрации пользователей на сайте —
    registrations.txt. Каждая строка содержит имя, имейл и возраст, разделённые
    пробелами. Например: Василий test@test.ru 27.
    Напишите программу, которая проверяет данные из файла для каждой строки:
    Присутствуют все три поля.
    Поле «Имя» содержит только буквы.
    Поле «Имейл» содержит @ и точку.
    Поле «Возраст» представляет число от 10 до 99.
    В результате проверки сформируйте два файла:
    registrations_good.log для правильных данных; записывать строки как есть;
    registrations_bad.log — для ошибочных; записывать строку и вид ошибки.
    """
    def find_error(string):
        data = string.split()
        if len(data) != 3:
            raise IndexError("Не присутствуют все три поля")
        name, email, age = data
        age = int(age)
        if not name.isalpha():
            raise NameError("Поле «Имя» содержит не только буквы")
        if not ("@" in email and "." in email):
            raise SyntaxError("Поле «Имейл» не содержит @ и/или точку")
        if age < 10 or age > 99:
            raise ValueError("Поле «Возраст» не является числом от 10 до 99")

    with open("registrations.txt", "r", encoding="utf-8") as read_file:
        with open("registrations_good.log", "w", encoding="utf-8") \
                as good_file:
            with open("registrations_bad.log", "w", encoding="utf-8") \
                    as bad_file:
                for line in read_file:
                    try:
                        find_error(line)
                        good_file.write(line)
                    except (IndexError, NameError, SyntaxError, ValueError) \
                            as exc:
                        bad_file.write(f"{line.strip()}       {exc}\n")


def task4():
    """
    Реализуйте программу — чат, в котором могут участвовать сразу несколько
    человек, то есть программу, которая может работать одновременно для
    нескольких пользователей. При запуске запрашивается имя пользователя.
    После этого он выбирает одно из действий:
    1. Посмотреть текущий текст чата.
    2. Отправить сообщение (затем вводит сообщение).
    """
    def show_chat():
        with open("group_chat.txt", "r", encoding="utf-8") as chat:
            print(chat.read())

    def send_a_message():
        message = input("Введите сообщение: ")
        with open("group_chat.txt", "a", encoding="utf-8") as chat:
            if is_first_message:
                chat.write(f"{name}:\n    {message}\n")
            else:
                chat.write(f"    {message}\n")

    name = input("Введите имя пользователя: ")
    is_first_message = True
    while True:
        print("\nВыберите действие:\n"
              f"1. Посмотреть текущий текст чата.\n2. Отправить сообщение\n"
              f"3. Выйти из программы\n  > ", end="")
        choice = input()
        if choice == "1":
            show_chat()
        elif choice == "2":
            send_a_message()
            if is_first_message:
                is_first_message = False
        elif choice == "3":
            print("\nЗавершение работы...")
            break
        else:
            print("Ошибка ввода. попробуйте ещё раз")


def task5():
    """
    Вы работаете в компании, занимающейся финансовыми вычислениями.
    Вам необходимо разработать функцию для вычисления квадратного корня числа,
    которая будет использоваться в анализе финансовых данных и расчёте
    инвестиционных показателей. Вы понимаете, что передача отрицательного
    числа или возникновение других ошибок вычисления могут привести к
    непредсказуемым результатам.
    Напишите функцию, которая будет:
    Вычислять и возвращать квадратный корень полученного числа.
    Обрабатывать исключения для отрицательных чисел и других возможных ошибок.
    """
    def sqrt(num):
        try:
            if num < 0:
                raise ValueError("Нельзя извлечь квадратный корень из "
                                 "отрицательного числа!")
            return num ** 0.5
        except ValueError as exc:
            print(exc)

    try:
        number = int(input("Введите число: "))
        square_root = sqrt(number)
        if square_root:
            print(square_root)
    except ValueError:
        print("Ошибка. Введена строка.")


if __name__ == '__main__':
    task1()
    # task2()
    # task3()
    # task4()
    # task5()
