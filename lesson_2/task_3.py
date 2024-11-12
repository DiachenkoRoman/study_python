#--------------------------VARIABLES-------------------------
from operator import index

list_append = [1, 2, 3]
list_extend = [4, 5, 6]
extension = [7, 8, 9]

#--------------------------SUBTASK 1-------------------------

list_append.append(4)
list_append.append(5)

print(list_append)

#--------------------------SUBTASK 2-------------------------

list_extend.extend(extension)

print(list_extend)

#--------------------------SUBTASK 3--------------------------

print(list_extend.index(6))

#--------------------------SUBTASK 4--------------------------

print(len(list_append))