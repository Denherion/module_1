my_dist = {'Denis': 1985, 'Vlad': 1986, 'Taras': 1987}
print(my_dist)
print(my_dist['Denis'])
print(my_dist.get('Kolya'))
my_dist.update({'Sasha': 1988,
                'Alex': 1989})
a = my_dist.pop('Taras') # извлек ключ "Taras" и его значение
print(a)
print(my_dist)
# множество
my_set = {1, 1, 'Python', 12.3, 12.3}
print(my_set)
my_set.update([8, 16]) # добавляет 8 и 16 в список
my_set.remove(16)
print(my_set)

