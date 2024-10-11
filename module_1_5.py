immutable_var = (52, 25, 1, True, "Слава")
print(immutable_var)
mutable_list = [52, 25, 1]
print(mutable_list)
mutable_list[0] = 69
mutable_list[1] = 96
print(mutable_list)

# immutable_var[0] = 100     # Попытка изменить элемент кортежа
# TypeError: 'tuple' object does not support item assignment #ошибка
#Кортежи являются неизменяемыми структурами данных.
# Это означает, что после создания кортежа его элементы нельзя изменить или перезаписать.