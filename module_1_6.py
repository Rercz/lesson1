my_dict = {'Сергей':1959,'Владимир':1870,'Иосиф':1878}
print(my_dict)
print(my_dict['Сергей'])
print(my_dict.get('Лаврентий'))
a = my_dict.pop('Владимир')
print(a)
my_dict.update({'Лаврентий':1899,'Никита':1894,'Леонид':1906})
print(my_dict)
my_set = ['Иосиф',1879,12.1906,1,2,1,2,5]
my_set = set(my_set)
print(my_set)
my_set.add('Никита')
my_set.add(55)
print(my_set)
my_set.discard('Иосиф')
print(my_set)


