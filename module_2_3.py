my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_list = len(my_list)
n = 0
while len_list != n:
    if my_list[n] > 0: print(my_list[n])
    n += 1
    if my_list[n] < 0:
        break
