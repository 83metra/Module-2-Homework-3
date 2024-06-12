my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
number_count = 0
while number_count <= len(my_list):
    if int(my_list[number_count]) == 0:  # если в последовательности встречается 0, пропускаем его.
        number_count = number_count +1
    else:
        if int(my_list[number_count]) > 0:
            print(my_list[number_count])
            number_count = number_count + 1
        elif int(my_list[number_count]) < 0:
#           print('Выполнение задачи прервано по условию наличия отрицательного числа.')
            break