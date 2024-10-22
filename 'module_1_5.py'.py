immutable_var = 1, 2, 'apple', 'Maxim'
print(immutable_var)
#immutable_var(1) = 3 # я не могу изменить данный элемент, поскольку он не изменяем
print(immutable_var)
mutable_list = [1, 2, 'apple', 'Maxim']
mutable_list[0] = 0
print(mutable_list)
mutable_list[3] = 'Roma'
print(mutable_list)