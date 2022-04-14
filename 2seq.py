# 1-й вариант(разделитель "запятая")
#print(list(set(list(map(int, input("Введите элементы списка через запятую: ").split(sep=","))))))

# 2-й вариант(выбор разделителя)
numbers = input("Введите элементы списка через разделитель: ")
s = ","
if (";" in numbers):
    s = ";"
elif ("/" in numbers):
    s = "/"
print(list(set(list(map(int, numbers.split(sep=s))))))