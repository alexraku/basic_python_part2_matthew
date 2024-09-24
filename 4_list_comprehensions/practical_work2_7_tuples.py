from random import randint


def task1():
    students = {
        1: {
            'name': 'Bob',
            'surname': 'Vazovski',
            'age': 23,
            'interests': ['biology', 'swimming']
        },
        2: {
            'name': 'Rob',
            'surname': 'Stepanov',
            'age': 24,
            'interests': ['math', 'computer games', 'running']
        },
        3: {
            'name': 'Alexander',
            'surname': 'Krug',
            'age': 22,
            'interests': ['languages', 'health food']
        }
    }

    def interests_surnames(info_dict):
        interests = []
        surnames = 0
        for person in info_dict.values():
            # хорошо что используешь dict.get() если ключа не будет в словаре
            # то ничего страшного не произойдет.
            interests.extend(person.get('interests', []))
            surnames += len(person.get('surname', ""))
        return set(interests), surnames

    for s_id, student in students.items():
        missing_attributes = []
        if not("name" in student and student["name"]):
            missing_attributes.append("name")
        if not("surname" in student and student["surname"]):
            missing_attributes.append("surname")
        if not("age" in student and student["age"]):
            missing_attributes.append("age")
        if not("interests" in student and student["interests"]):
            missing_attributes.append("interests")
        if missing_attributes:
            print(f"У студента {s_id} отсутствуют следующие характеристики: "
                  f"{missing_attributes}")

    #упрощение функции проверки
    required_fields = ['name', 'surname', 'age', 'interests']
    for s_id, student in students.items():
        missing_attributes = [attr for attr in required_fields if not student.get(attr)]
        if missing_attributes:
            print(f"У студента с ID: {s_id}, отсутствуют аттрибуты: {', '.join(missing_attributes)}")

    pairs = [(s_id, value.get("age", "_")) for s_id, value in students.items()]
    print("Список пар «ID студента — возраст»:", pairs)

    interest_list, surname_len = interests_surnames(students)
    print("Полный список интересов всех студентов:", interest_list)
    print("Общая длина всех фамилий студентов:", surname_len)


def task2():

    def is_prime(num):
        num2 = 2
        if num < num2:
            return False
        while num2 <= num ** 0.5:
            if num % num2 == 0:
                return False
            num2 += 1
        else:
            return True

    def prime_index_list(obj):
        return [elem for elem_index, elem in enumerate(obj)
                if is_prime(elem_index)]

    print(prime_index_list('О Дивный Новый мир!'))


def task3():
    # Тут все сделано хорошо!
    players = {
        ("Ivan", "Volkin"): (10, 5, 13),
        ("Bob", "Robbin"): (7, 5, 14),
        ("Rob", "Bobbin"): (12, 8, 2)
    }

    new_list = [name + score for name, score in players.items()]
    print(new_list)


def task4():
    # посмотри, еще есть 3й вариант
    num_list = [randint(0, 10) for _ in range(10)]
    print("Оригинальный список:", num_list)

    # вариант 1:
    new_list = [(num_list[num], num_list[num + 1]) for num in range(0, 9, 2)]
    print("Новый список:", new_list)

    # вариант 2
    n_list1 = [num_list[num] for num in range(0, 9, 2)]
    n_list2 = [num_list[num] for num in range(1, 10, 2)]
    new_list = list(zip(n_list1, n_list2))
    print("Новый список:", new_list)

    # вариант 3
    n_list = [(n1, n2) for n1, n2 in zip(num_list[0::2], num_list[1::2])]
    print("Новый список:", n_list)


def task5():
    # Посмотри еще один вариант реализации tpl_sort
    def tpl_sort(num_tuple):
        for elem in num_tuple:
            if not isinstance(elem, int):
                return num_tuple
        return tuple(sorted(num_tuple))

    def tpl_sort_1(num_tuple):
        if all(map(lambda elem: isinstance(elem, int), num_tuple)):
            return tuple(sorted(num_tuple))
        return num_tuple

    def tpl_sort_2(num_tuple):
        if all(isinstance(elem, int) for elem in num_tuple):
            return tuple(sorted(num_tuple))
        return num_tuple

    tpl = (6, 3, -1, 8, 4, 10, -5)
    print(tpl_sort_1(tpl))


def task6():
    def add_contact():
        name_surname = tuple(input("Введите имя и фамилию нового контакта "
                                   "(через пробел): ").title().split())
        if name_surname in contacts:
            print("Такой человек уже есть в контактах")
        else:
            phone_num = int(input("Введите номер телефона: "))
            contacts[name_surname] = phone_num

    def find_person():
        needed_surname = input("Введите фамилию для поиска: ")
        flag = False
        for (name, surname), phone_num in contacts.items():
            if surname.lower() == needed_surname.lower():
                print(name, surname, phone_num)
                flag = True
        if not flag:
            print("Людей с такой фамилией нет в словаре контактов")

    contacts = dict()
    while True:
        choice = input("Введите номер действия: \n   "
                       "1.Добавить контакт\n   2.Найти человека\n> ")
        if choice == "1":
            add_contact()
            print("Текущий словарь контактов:", contacts)
            print()
        elif choice == "2":
            find_person()
            print()
        else:
            print("Неправильный ввод. Попробуйте ещё раз\n")


def task7():
    obj1 = "abcd"
    obj2 = (10, 20, 30, 40)
    max_len = min(len(obj1), len(obj2))

    result = ((obj1[num], obj2[num]) for num in range(max_len))
    print(result)
    for tpl in result:
        print(tpl)

def my_zip(first, second) -> tuple:
    border = min(len(first), len(second))
    for index in range(border):
        yield first[index], second[index]


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
    task7()
