immutable_var = [1, 2, 3, True]
tuple = immutable_var
print(tuple)
#immutable_var = [1, 2, 3, false]   #неизменяемость вляется особенностью кортежа (tupl),поэтому: NameError: name 'false' is not defined. Did you mean: 'False'?
mutable_list = [1, 2, 3, 'Как уже достал этот дождь']
print(mutable_list)
mutable_list[3] = 'Как я любдю дождь'
print(mutable_list)