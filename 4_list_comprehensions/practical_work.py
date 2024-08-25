def nested_list_gen():
    all_list = []
    num_list1 = []
    num_list2 = []
    num_list3 = []
    num_list4 = []
    for num in range(1, 13):
        if num % 4 == 1:
            num_list1.append(num)
        if num % 4 == 2:
            num_list2.append(num)
        if num % 4 == 3:
            num_list3.append(num)
        if num % 4 == 0:
            num_list4.append(num)
    all_list.append(num_list1)
    all_list.append(num_list2)
    all_list.append(num_list3)
    all_list.append(num_list4)

    print(all_list)


def nested_list_gen_lc():
    num_list = [[m + n for n in range(0, 10, 4)] for m in range(1, 5)]
    print(num_list)


def nested_list_gen1():
    all_list = []
    for m in range(1, 5):
        num_list = []
        for n in range(0, 10, 4):
            num_list.append(n + m)
        all_list.append(num_list)
    print(all_list)


if __name__ == '__main__':
    nested_list_gen()
    nested_list_gen_lc()
    nested_list_gen1()
