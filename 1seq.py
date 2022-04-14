count = int(input("количество элементов: "))
my_list = []
for i in range(count):
    my_list.append(int(input("Введите {0}-й элемент: ".format(i+1))))
my_list.sort()
print(my_list)