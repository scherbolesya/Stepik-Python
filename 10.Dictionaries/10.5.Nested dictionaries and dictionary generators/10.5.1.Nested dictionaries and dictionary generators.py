# Создание вложенных словарей
# Вложенный словарь создается как обычный, только каждое значение в нем – другой словарь.

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}

# Тот же самый словарь info может быть создан по другому:

info = dict(emp1 = {'name': 'Timur', 'job': 'Teacher'},
            emp2 = {'name': 'Ruslan', 'job': 'Developer'},
            emp3 = {'name': 'Rustam', 'job': 'Tester'})
# или

ids = ['emp1', 'emp2', 'emp3']
emp_info = [{'name': 'Timur', 'job': 'Teacher'},
            {'name': 'Ruslan', 'job': 'Developer'},
            {'name': 'Rustam', 'job': 'Tester'}]
info = dict(zip(ids, emp_info))

-----------------------------------------------------------------------------------
# Обращение к элементам вложенного словаря
# Для того, чтобы получить значения определенных элементов во вложенном словаре, необходимо указать их ключи в нескольких квадратных скобках подобно тому, 
# как мы получали значения во вложенных списках.

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
print(info['emp1']['name'])
print(info['emp2']['job'])
# выводит:
Timur
Developer
# При попытке обращения по несуществующему ключу возникнет ошибка KeyError. 
# Для того, чтобы избежать возникновения такой ошибки, используйте словарный метод get(), который по умолчанию возвращает значение None, если ключ отсутствует в словаре.

-----------------------------------------------------------------------------------
# Изменение вложенных словарей
# Чтобы изменить значение определенного элемента во вложенном словаре, необходимо обратиться к его ключу и использовать оператор присвоения (=).
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
info['emp1']['job'] = 'Manager'
print(info['emp1'])
# выводит:
{'name': 'Timur', 'job': 'Manager'}

-----------------------------------------------------------------------------------
# Итерация по вложенным словарям
# Итерации по вложенным словарям осуществляются как правило двумя циклами for (иногда достаточно одного цикла).

info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
for emp in info:
    print('Employee ID:', emp)
    for key in info[emp]:
        print(key + ':', info[emp][key])
    print()
# выводит:
Employee ID: emp1
name: Timur
job: Teacher

Employee ID: emp2
name: Ruslan
job: Developer

Employee ID: emp3
name: Rustam
job: Tester

# Аналогичного результата можно было добиться с помощью метода items():
info = {'emp1': {'name': 'Timur', 'job': 'Teacher'},
        'emp2': {'name': 'Ruslan', 'job': 'Developer'},
        'emp3': {'name': 'Rustam', 'job': 'Tester'}}
for emp, inf in info.items():
    print('Employee ID:', emp)
    for key in inf:
        print(key + ':', inf[key])
    print()

--------------------------------------------------------------------------------------
# Генераторы словарей
# Пусть требуется создать словарь, ключами которого будут числа от 0 до 5, а значениями – квадраты ключей.

# Для создания требуемого словаря можно использовать код:
squares = {}
squares[0] = 0
squares[1] = 1
squares[2] = 4
squares[3] = 9
squares[4] = 16
squares[5] = 25
# или:
squares = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# или:
squares = {}
for i in range(6):
    squares[i] = i**2

# Первые два способа слишком громоздкие и не подходят, когда чисел много. Третий способ полностью решает поставленную задачу, 
# однако его можно переписать в стиле Python с использованием генератора словаря:
squares = {i: i**2 for i in range(6)}
# Общий вид генератора словаря следующий:
{ключ: значение for переменная in последовательность}
где переменная — имя некоторой переменной, последовательность — последовательность значений, которые она принимает (любой итерируемый объект), 
ключ: значение — некоторое выражение, как правило, зависящее от использованной в списочном выражении переменной, которой будут заполнены элементы словаря.

-------------------------------------------------------------------------------------------
# Примеры использования генератора словарей
# Генераторы словаря могут выполнять итерации по любому итерируемому объекту: списки, кортежи, строки, словари.
# 1. Генератор словаря при итерировании по строке.
dct = {c: c * 3 for c in 'ORANGE'}
print(dct)
# выводит:
{'O': 'OOO', 'R': 'RRR', 'A': 'AAA', 'N': 'NNN', 'G': 'GGG', 'E': 'EEE'}

# 2. Для вычисления ключа и значения в генераторе словаря могут быть использованы выражения.
# В следующем примере для вычисления ключа используется метод lower(), а для вычисления значения – метод upper().
lst = ['ReD', 'GrEeN', 'BlUe']
dct = {c.lower(): c.upper() for c in lst}
print(dct)
# выводит:
{'red': 'RED', 'green': 'GREEN', 'blue': 'BLUE'}

# 3. Извлечение из словаря элементов с определенными ключами.
dict1 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F'}
selected_keys = [0, 2, 5]
dict2 = {k: dict1[k] for k in selected_keys}
print(dict2)
# выводит:
{0: 'A', 2: 'C', 5: 'F'}

--------------------------------------------------------------------------------------------
# Условия в генераторе словарей
# В генераторах словарей можно использовать условный оператор.
# Приведенный ниже код создает словарь, ключами которого являются четные числа от 0 до 9, а значениями – квадраты ключей:
squares = {}
for i in range(10):
    if i % 2 == 0:
        squares[i] = i**2
print(squares)
# Такой код можно переписать с помощью генератора словаря в виде: 
squares = {i: i**2 for i in range(10) if i % 2 == 0}
print(squares)
# Не забываем про возможность указания шага в функции range(). Предыдущий код можно записать и без условного оператора: squares = {i: i**2 for i in range(0, 10, 2)}.

----------------------------------------------------------------------------------------------
# Генераторы вложенных словарей
# Мы также можем использовать генераторы словарей для создания вложенных словарей:
squares = {i: {j: j**2 for j in range(i + 1)} for i in range(5)}
for value in squares.values():
    print(value)
# выводит:
{0: 0}
{0: 0, 1: 1}
{0: 0, 1: 1, 2: 4}
{0: 0, 1: 1, 2: 4, 3: 9}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}