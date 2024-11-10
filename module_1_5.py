immutable_var = 1, 2, 'a', 'b'
print(immutable_var)
# immutable_var[0] = 200
# Кортеж изменить нельзя, так как переменная "кортеж" является неизменяемым объектом.
mutable_list = [1, 2, 'a', 'b', 'Modified']
mutable_list[0] = 200
print(mutable_list)