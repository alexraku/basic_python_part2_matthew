import os


def task1():
    file = open("numbers.txt", "r")
    text = file.read()
    print("Содержимое файла numbers.txt\n", text)
    file.close()

    all_num = text.split()
    all_num = [int(elem) for elem in all_num]
    num_sum = sum(all_num)

    new_file = open("answer.txt", "w")
    new_file.write(str(num_sum))
    new_file.close()

    new_file = open("answer.txt", "r")
    text2 = new_file.read()
    print("\nСодержимое файла answer.txt\n", text2)
    new_file.close()


def task2():
    file = open("zen.txt", "r")
    line_list = [line for line in file]
    file.close()

    for elem in line_list[::-1]:
        print(elem, end="")


def task3():
    def dir_and_file_count(my_path):
        dir_size = 0
        files_num = 0
        dir_num = 0

        for elem in os.listdir(my_path):
            elem_path = os.path.join(my_path, elem)
            if os.path.isfile(elem_path):
                files_num += 1
                dir_size += os.path.getsize(elem_path)
            else:
                dir_num += 1
                subdir_fn, subdir_dn, subdir_s = dir_and_file_count(elem_path)
                dir_size += subdir_s
                files_num += subdir_fn
                dir_num += subdir_dn

        return files_num, dir_num, dir_size

    path = os.path.abspath(os.path.join("..", "..", "..",
                                        "basic_python_part2_matthew"))
    print(path)
    file_count, dir_count, size = dir_and_file_count(path)
    print("Размер каталога (в Кбайтах):", size // 1024)
    print("Количество подкаталогов:", dir_count)
    print("Количество файлов:", file_count)


def task4():
    file = open("first_tour.txt", "r")
    print("Содержимое файла first_tour.txt:",)
    passing_score = 0
    winner_list = []
    for line in file:
        print(line)
        line_list = line.split()
        if len(line_list) == 1:
            passing_score = line_list[0]
        else:
            surname, name, score = line_list
            if score > passing_score:
                winner_list.append(f"{name[0]}. {surname} {score}\n")
    file.close()

    new_file = open("second_tour.txt", "w")
    winners_num = len(winner_list)
    new_file.write(f"{winners_num}\n")
    winner_list = sorted(winner_list)[::-1]
    for elem_i in range(winners_num):
        new_file.write(f"{elem_i + 1}) {winner_list[elem_i]}")
    new_file.close()

    new_file = open("second_tour.txt", "r")
    text = new_file.read()
    print(f"\nСодержимое файла second_tour.txt:\n{text}")
    new_file.close()


def task5():
    file = open("text.txt", "r", encoding="utf-8")
    text = file.read()
    print(f"Содержимое файла text.txt\n{text}")

    sym_dict = dict()
    sym_count = 0
    for sym in text:
        if sym.isalpha():
            sym_count += 1
            sym = sym.lower()
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1
    file.close()

    sym_list = sorted([(round(value / sym_count * 100, 3), key)
                       for key, value in sym_dict.items()])
    new_file = open("analysis.txt", "w", encoding="utf-8")
    for elem in sym_list[::-1]:
        new_file.write(f"{elem[1]}  {elem[0]}\n")
    new_file.close()

    file = open("analysis.txt", "r", encoding="utf-8")
    text = file.read()
    print(f"\nСодержимое файла analysis.txt\n{text}")
    file.close()


def task6():
    file = open("book.txt", "r", encoding="utf-8")
    text = file.read()

    sym_count = 0
    sym_dict = dict()
    for sym in text:
        if sym.isalpha():
            sym_count += 1
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1
    file.close()

    sym_list = sorted([(round(value / sym_count * 100, 6), key)
                       for key, value in sym_dict.items()])
    new_file = open("war_and_peace_analysis.txt", "w", encoding="utf-8")
    for elem in sym_list[::-1]:
        new_file.write(f"{elem[1]}  {elem[0]}\n")
    new_file.close()


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    # task4()
    task5()
    # task6()
