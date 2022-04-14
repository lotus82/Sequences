lst_1 = list(map(int, input("Введите элементы 1-го списка через запятую: ").split(sep=",")))
lst_2 = list(map(int, input("Введите элементы 2-го списка через запятую: ").split(sep=",")))
set_uniq = set(lst_1).difference(set(lst_2))
lst_out = []
for el in lst_1:
    if el in set_uniq:
        lst_out.append(el)
print(lst_out)
