students_set = {'Johnny', 'Bilbo', 'Steve', 'Hendrik', 'Aaron'}
sort_list = sorted(list(students_set))
#print(sort_list)
#print(sort_list[0])
result_dictionary = {}
for name in sort_list:
      grades = []
      grades_count = int(input('Введите количество оценок ' + name + ' '))
      for i in range(grades_count):
       grades.append(int(input('Введите оценки ' + name + ' ')))
      mean_value = (sum(grades)/grades_count)
      result_dictionary[name] = mean_value
      #print(mean_value)
print(result_dictionary)
