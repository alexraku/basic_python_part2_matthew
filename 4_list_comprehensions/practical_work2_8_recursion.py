def task1():
    def one_to_num(num, start=1):
        if start == num:
            print(num)
        else:
            print(start)
            one_to_num(num, start + 1)

    number = int(input("Введите число: "))
    one_to_num(number)


def task2():
    def key_search(my_dict, key, depth=5):
        if depth == 1:
            return
        if key in my_dict:
            return my_dict[key]
        for elem in my_dict.values():
            if isinstance(elem, dict):
                search_try = key_search(elem, key, depth - 1)
                if search_try:
                    return search_try

    site = {
        'html': {
            'head': {
                'title': 'Мой сайт'
            },
            'body': {
                'h2': 'Здесь будет мой заголовок',
                'div': 'Тут, наверное, какой-то блок',
                'p': 'А вот здесь новый абзац'
            }
        }
    }

    my_key = input("Введите искомый ключ: ")
    while True:
        question = input("Хотите ввести максимальную глубину? y/n: ")
        if question == "y":
            my_depth = int(input("Введите максимальную глубину: "))
            print(key_search(site, my_key, my_depth))
            break
        if question == "n":
            print(key_search(site, my_key))
            break
        print("Ошибка ввода. Попробуйте ещё раз.")


def task3():
    def deep_copy(data):
        if isinstance(data, (str, int, bool, tuple)):
            return data
        new_dict = dict()
        for key, value in data.items():
            new_dict[key] = deep_copy(value)
        return new_dict

    def site_change(my_site, product):
        for key, value in my_site.items():
            if isinstance(value, dict):
                site_change(value, product)
            if "{product}" in value:
                new_value = value.format(product=product)
                my_site[key] = new_value

    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам {product} недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на {product}',
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }

    sites_num = int(input("Сколько сайтов: "))
    sites_dict = dict()
    for _ in range(sites_num):
        product_name = input("Введите название продукта для нового сайта: ")
        new_site = deep_copy(site)
        site_change(new_site, product_name)
        sites_dict[product_name] = new_site
        for key, value in sites_dict.items():
            print(f"\nСайт для {key}:")
            print(value)


def task4():
    def my_sum(*args):
        summ = 0
        for elem in args:
            if isinstance(elem, list):
                for elem1 in elem:
                    num = my_sum(elem1)
                    summ += num
            else:
                summ += elem
        return summ

    print(my_sum([[1, 2, [3]], [1, [4, [7, 6, [12]], 4]], 3], 5, 1))


def task5():
    def change_to_one_list(list_list):
        new_list = []
        for elem in list_list:
            if isinstance(elem, list):
                small_list = change_to_one_list(elem)
                new_list.extend(small_list)
            else:
                new_list.append(elem)
        return new_list

    nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
                 [[11, 12, 13], [14, 15], [16, 17, 18]]]
    print(change_to_one_list(nice_list))


def task6():
    def quicksort(my_list):
        if len(my_list) == 1:
            return my_list
        base_elem = my_list[-1]
        less_list = []
        same_list = []
        more_list = []

        for elem in my_list:
            if elem < base_elem:
                less_list.append(elem)
            elif elem == base_elem:
                same_list.append(elem)
            else:
                more_list.append(elem)

        if len(less_list) > 1:
            less_list = quicksort(less_list)
        if len(more_list) > 1:
            more_list = quicksort(more_list)
        return less_list + same_list + more_list

    print(quicksort([4, 9, 2, 7, 5]))


if __name__ == '__main__':
    task1()
    # task2()
    # task3()
    # task4()
    # task5()
    # task6()
