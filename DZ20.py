def add_one(some_list):
    str1 = ''.join(str(i) for i in lst1)
    number = int(str1) + 1
    lst_lst = list()

    a = 1
    howm = len(str(number))
    x = number // 10 ** (howm - a)
    lst_lst.append(x)
    a += 1
    if howm > 1:
        while True:
            if a == howm:
                x = number % 10
                lst_lst.append(x)
                break
            x = number // 10 ** (howm - a) % 10
            lst_lst.append(x)
            a += 1
    return (lst_lst)

lst1 = [1, 2, 3, 4]
add_one(lst1)
print(add_one(lst1))
