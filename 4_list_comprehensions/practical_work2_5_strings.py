def menu():
    dishes = ", ".join(input("Доступное меню: ").split(";"))
    print("Сейчас в меню есть", dishes)


def the_longest_word():
    text = input("Введите строку: ").split()
    longest_word = ""
    for word in text:
        if "." in word:
            word = "".join([sym for sym in word if sym != "."])
        if len(word) > len(longest_word):
            longest_word = word
    print("Самое длинное слово:", longest_word)
    print(f"Длина этого слова: {len(longest_word)} символов")


def files():
    bad_starts = ("@", "№", "$", "%", "^", "&", "*", "()")
    good_ends = (".txt", ".docx")
    file_name = input("Название файла: ")
    if file_name.startswith(bad_starts):
        print("Ошибка: название начинается недопустимым символом.")
    elif not file_name.endswith(good_ends):
        print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
    else:
        print("Файл назван верно.")


def capital_letters():
    text = input("Введите строку: ").split()
    for word_i in range(len(text)):
        text[word_i] = text[word_i].title()
    print("Результат:", " ".join(text))


def password():
    while True:
        your_password = input("Придумайте пароль: ")
        if len(your_password) < 8:
            print("Пароль ненадёжный. Попробуйте ещё раз.\n")
            continue
        num_count = 0
        u_flag = False
        for sym in your_password:
            if sym.isupper():
                u_flag = True
            if sym.isdigit():
                num_count += 1
        if u_flag and num_count >= 3:
            print("Это надёжный пароль.")
            break
        else:
            print("Пароль ненадёжный. Попробуйте ещё раз.\n")


def compression():
    string = input("Введите строку: ") + "."
    new_string = []
    sym2 = string[0]
    sym_count = 0
    for sym in string:
        if sym == sym2:
            sym_count += 1
        else:
            new_string.append(sym2)
            new_string.append(str(sym_count))
            sym_count = 1
        sym2 = sym
    print("Закодированная строка:", "".join(new_string))


def ip_address2():
    ip = input("Введите IP: ").split(".")
    if len(ip) != 4:
        print("Адрес - это четыре числа, разделённые точками.")
    else:
        for num in ip:
            if not num.isdigit():
                print("{} - это не натуральное число.".format(num))
                break
            elif int(num) > 255:
                print("{} превышает 255.".format(num))
                break
        else:
            print("IP-адрес корректен.")


def running_string():
    str1 = input("Первая строка: ")
    str2 = input("Вторая строка: ")
    str2 = [sym for sym in str2]
    for num in range(1, len(str2) + 1):
        sym = str2[-1]
        str2.remove(str2[-1])
        str2.insert(0, sym)
        if "".join(str2) == str1:
            print("Первая строка получается из второй со сдвигом", num)
            break
    else:
        print("Первую строку нельзя получить из второй "
              "с помощью циклического сдвига.")


def comment_analysis():
    def count_uppercase_lowercase(string):
        u_counter = 0
        l_counter = 0
        for sym in string:
            if sym.isupper():
                u_counter += 1
            elif sym.islower():
                l_counter += 1
        return u_counter, l_counter

    text = input("Введите строку для анализа: ")
    uppercase, lowercase = count_uppercase_lowercase(text)
    print("Количество заглавных букв:", uppercase)
    print("Количество строчных букв:", lowercase)


if __name__ == '__main__':
    menu()
    # the_longest_word()
    # files()
    # capital_letters()
    # password()
    # compression()
    # ip_address2()
    # running_string()
    # running_string()
    # comment_analysis()
