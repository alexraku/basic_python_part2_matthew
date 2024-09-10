def songs2():
    violator_songs = {
        'world in my eyes': 4.86,
        'sweetest perfection': 4.43,
        'personal jesus': 4.56,
        'halo': 4.9,
        'waiting for the night': 6.07,
        'enjoy the silence': 4.20,
        'policy of truth': 4.76,
        'blue dress': 4.29,
        'clean': 5.83
    }
    total_time = 0
    songs_num = int(input("Сколько песен выбрать? "))

    for my_song in range(1, songs_num + 1):
        while True:
            song = input(f"\nНазвание {my_song} песни: ").lower()
            if song in violator_songs:
                total_time += violator_songs[song]
                break
            print("Данной песни нет в списке. Выберите другую, пожалуйста.")
    print("Общее время звучания песен:", round(total_time, 2), "минуты.")


def cryptocurrency():
    data = {
        "address": "0x544444444444",
        "ETH": {
            "balance": 444,
            "totalIn": 444,
            "totalOut": 4
        },
        "count_txs": 2,
        "tokens": [
            {
                "fst_token_info": {
                    "address": "0x44444",
                    "name": "fdf",
                    "decimals": 0,
                    "symbol": "dsfdsf",
                    "total_supply": "3228562189",
                    "owner": "0x44444",
                    "last_updated": 1519022607901,
                    "issuances_count": 0,
                    "holders_count": 137528,
                    "price": False
                },
                "balance": 5000,
                "totalIn": 0,
                "total_out": 0
            },
            {
                "sec_token_info": {
                    "address": "0x44444",
                    "name": "ggg",
                    "decimals": "2",
                    "symbol": "fff",
                    "total_supply": "250000000000",
                    "owner": "0x44444",
                    "last_updated": 1520452201,
                    "issuances_count": 0,
                    "holders_count": 20707,
                    "price": False
                },
                "balance": 500,
                "totalIn": 0,
                "total_out": 0
            }
        ]
    }
    print("Ключи:", [key for key in data],
          "\nЗначения:", [value for value in data.values()])
    data["ETH"]["total_diff"] = 100
    data["tokens"][0]["fst_token_info"]["name"] = "doge"
    data["ETH"]["totalOut"] = data["tokens"][0].pop("total_out") + \
        data["tokens"][1].pop("total_out")
    data["tokens"][1]["sec_token_info"]["total_price"] = \
        data["tokens"][1]["sec_token_info"].pop("price")


def products():
    goods = {
        'Лампа': '12345',
        'Стол': '23456',
        'Диван': '34567',
        'Стул': '45678',
    }
    store = {
        '12345': [
            {'quantity': 27, 'price': 42},
        ],
        '23456': [
            {'quantity': 22, 'price': 510},
            {'quantity': 32, 'price': 520},
        ],
        '34567': [
            {'quantity': 2, 'price': 1200},
            {'quantity': 1, 'price': 1150},
        ],
        '45678': [
            {'quantity': 50, 'price': 100},
            {'quantity': 12, 'price': 95},
            {'quantity': 43, 'price': 97},
        ],
    }
    for product in goods:
        total_quantity = 0
        total_price = 0
        for purchase in store[goods[product]]:
            total_price += purchase["price"] * purchase["quantity"]
            total_quantity += purchase["quantity"]
        print("{} - {} штук, стоимость: {:,d} рублей.".format(
            product,
            total_quantity,
            total_price
        ))


def histogram2():
    text = input("Введите текст: ")
    sym_dict = dict()
    for sym in text:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    print("Оригинальный словарь частот:")
    for elem in sorted(sym_dict):
        print(elem, ":", sym_dict[elem])

    inverted_dict = {num: [] for num in set(sym_dict.values())}
    for sym in sym_dict:
        for word_count in inverted_dict:
            if sym_dict[sym] == word_count:
                inverted_dict[word_count].append(sym)
    print("\nИнвертированный словарь частот:")
    for elem in inverted_dict:
        print(elem, ":", inverted_dict[elem])


def synonym_dictionary():
    pairs_num = int(input("Введите кол-во пар слов: "))
    synonym_dict = dict()
    for num in range(1, pairs_num + 1):
        word_pair = input(f"{num}-я пара: ").lower().split(" - ")
        synonym_dict[word_pair[0]] = word_pair[1]
    rev_synonym_dict = {synonym_dict[key]: key for key in synonym_dict}
    while True:
        word = input("Введите слово: ").lower()
        if word in synonym_dict:
            print("Синоним:", synonym_dict[word])
            break
        elif word in rev_synonym_dict:
            print("Синоним:", rev_synonym_dict[word])
            break
        else:
            print("Такого слова в словаре нет.")


def pizza():
    orders = int(input("Введите кол-во заказов: "))
    total_orders = dict()

    for order_num in range(1, orders + 1):
        order = input(f"{order_num}-й заказ: ").split()
        pizza_num = int(order[2])
        if order[1] in total_orders.get(order[0], ""):
            total_orders[order[0]][order[1]] += pizza_num
        elif order[0] in total_orders:
            total_orders[order[0]][order[1]] = pizza_num
        else:
            total_orders[order[0]] = dict()
            total_orders[order[0]][order[1]] = pizza_num

    for name in sorted(total_orders):
        print(f"\n{name}:")
        for pizza_type in total_orders[name]:
            print(f"{pizza_type}: {total_orders[name][pizza_type]}")


def three_lists():
    array_1 = [1, 5, 10, 20, 40, 80, 100]
    array_2 = [6, 7, 20, 80, 100]
    array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

    set1 = set(array_1)
    set2 = set(array_2)
    set3 = set(array_3)

    print("Задача 1:")
    same_numbers = []
    for elem in array_1:
        if (elem in array_2) and (elem in array_3):
            same_numbers.append(elem)
    print("Решение без множеств:", same_numbers)
    same_numbers = set1 & set2 & set3
    print("Решение с множествами:", sorted(same_numbers))

    print("Задача 2")
    numbers = []
    for elem in array_1:
        if not (elem in array_2 or elem in array_3):
            numbers.append(elem)
    print("Решение без множеств:", numbers)
    numbers = set1 - set2 - set3
    print("Решение с множествами:", sorted(numbers))


def again_palindrome():
    string = input("Введите строку: ")
    sym_dict = dict()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    counter = 0
    for sym_count in sym_dict.values():
        if sym_count % 2 == 1:
            counter += 1
        if counter > 1:
            print("Нельзя сделать палиндромом")
            break
    else:
        print("Можно сделать палиндромом")


if __name__ == '__main__':
    songs2()
    # cryptocurrency()
    # products()
    # histogram2()
    # synonym_dictionary()
    # pizza()
    # three_lists()
    # again_palindrome()
