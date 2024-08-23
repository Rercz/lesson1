immutable_var = 1, 2, 3, 'это кошка'
print(immutable_var)
#immutable_var[3] = 4 TypeError: 'tuple' object does not support item assignment потому что картеж
mutable_list = [1, 2, 3, 'это кот']
print(mutable_list)
mutable_list[3] = 3
print(mutable_list)