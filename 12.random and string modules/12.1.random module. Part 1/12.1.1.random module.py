# random module.
Модуль random предоставляет функции для генерации псевдослучайных чисел, букв и случайного выбора элементов последовательности (списка, строки и т.д.).
Для использования этих функций в начале программы необходимо подключить модуль, что делается командой import:

import random
После подключения модуля мы можем использовать его функции.

# Функция randint()
Функция randint() принимает два обязательных аргумента a и b и возвращает псевдослучайное целое число из отрезка [a;b].
Следующий код выводит два псевдослучайных целых числа: num1 из отрезка [0;17] и num2 из отрезка [−5;5].

import random
num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)

Левая и правая граница a и b включаются в диапазон генерируемых псевдослучайных чисел. Результатом вызова функции random.randint(2, 9) может быть любое число от 2 до 9, включая 2 и 9.
Следующий код выводит 10 псевдослучайных целых чисел из диапазона [1;100]:

import random
for _ in range(10):
    print(random.randint(1, 100))

Среди этих чисел возможны повторения.

# Функция randrange()
Если вы помните, как применять функцию range(), то почувствуете себя непринужденно с функцией randrange(). Функция randrange() принимает такие же аргументы, что и функция range(). Различие состоит в том, что функция randrange()
не возвращает саму последовательность чисел. Вместо этого она возвращает случайно выбранное число из последовательности чисел.
Следующий код присваивает переменной num псевдослучайное число в диапазоне от 0 до 9:

import random
num = random.randrange(10)

Аргумент 10 задает конечный предел последовательности значений. Функция возвратит случайно выбранное число из последовательности чисел от 0 до конечного предела, исключая сам предел.
Следующий код задает начальное значение и конечный предел последовательности:

import random
num = random.randrange(5, 10)

Таким образом в переменной num будет храниться псевдослучайное число в диапазоне от 5 до 9.
Следующий код задает начальное значение, конечный предел и величину шага:

import random
num = random.randrange(0, 101, 10)

Таким образом в переменной num будет храниться псевдослучайное число из последовательности чисел: 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.

# Функция random()
Функции randint() и randrange() возвращают псевдослучайное целое число. А вот функция random() возвращает псевдослучайное число с плавающей точкой (вещественное число). В функцию random() никаких аргументов не передается. Функция random() возвращает случайное число с плавающей точкой в диапазоне от 
0.0 до 1.0 (исключая 1.0).
Следующий код выводит случайное число с плавающей точкой из диапазона [0.0;1.0):

import random
num = random.random()
print(num)

# Функция uniform()
Функция uniform() тоже возвращает случайное число с плавающей точкой, но при этом она позволяет задавать диапазон для отбора значений.
Следующий код выводит псевдослучайное число с плавающей точкой из диапазона [1.5;17.3] (включительно):

import random
num = random.uniform(1.5, 17.3)
print(num)

# Функция seed()
Как уже было сказано псевдослучайные числа вычисляются на основе некой формулы. Генерация случайных чисел инициируется начальным значением. Оно используется в вычислении, возвращающем следующее случайное число в ряду. Когда модуль random импортируется, он получает системное время из внутреннего генератора тактовых импульсов компьютера и использует его как начальное значение. Системное время – целое число, представляющее собой текущую дату и время вплоть до сотой секунды. Если бы всегда использовалось одно и то же начальное значение, функции генерации случайных чисел всегда  возвращали бы один и тот же ряд псевдослучайных чисел. Поскольку системное время меняется каждую сотую долю секунды, можно утверждать, что всякий раз, когда импортируется модуль random, будет создана отличающаяся от предыдущих последовательность случайных чисел.
Вместе с тем, некоторые программы требуют генерации одной и той же последовательности случайных чисел. Для этого можно вызвать функцию seed(), задав начальное значение.
Следующий код генерирует 10 псевдослучайных чисел, и при этом содержит инструкцию, явно устанавливающую начальное значение для генератора случайных чисел:

import random
random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел
for _ in range(10):
    print(random.randint(1, 100))

Результат выполнения такого кода:
67
54
39
47
38
23
99
91
91
70
Если выполнить код еще раз, получим ту же самую последовательность псевдослучайных чисел.

# Примечания
Примечание 1. Подключение модуля следующим образом:
from random import *

позволяет в дальнейшем не писать название модуля и символ точки при вызове функций модуля.
Примечание 2. Функции модуля random на самом деле являются методами одноименного класса random.
Примечание 3. В Python для генерации псевдослучайных чисел используется один из самых совершенных алгоритмов генерации псевдослучайных чисел – "вихрь Мерсенна", разработанный в 1997 году. Реализация выполнена на языке C, является быстрой и потокобезопасной.
Примечание 4. Настоящие случайные числа можно получить с сайта. Данный сайт использует атмосферный шум для создания по-настоящему случайных чисел.
Примечание 5. Пусть r – случайное число из интервала (0;1). Для того, чтобы перевести такое число в интервал (a;b) можно воспользоваться формулой a+(b−a)⋅r.
