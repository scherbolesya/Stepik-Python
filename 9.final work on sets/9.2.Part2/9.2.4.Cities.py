# Cities
# Timur and Ruslan play the city game. They love this game very much and know many cities, especially Timur, 
# but by the end of the game, due to their age, they forget which cities they have already named.
# Write a program that reads information about the game and tells the guys that the next city has been renamed.

# Города
# Тимур и Руслан играют в игру города. Они очень любят эту игру и знают много городов, особенно Тимур, однако к концу игры ввиду своего возраста забывают, какие города уже называли.
# Напишите программу, считывающую информацию об игре и сообщающую ребятам, что очередной город назван повторно.

n = int(input())
s = set()
for i in range(n):
    s.add(input())
s1 = input()
if s1 in s:
    print('REPEAT')
else:
    s.add(s1)
    print('OK')

Sample Input 1:
3
Каир
Рим
Москва
Агра
Sample Output 1:
OK
Sample Input 2:
5
Лас-Вегас
Сеул
Лондон
Ницца
Адел
Лас-Вегас
Sample Output 2:
REPEAT
Sample Input 3:
2
Паттайя
Якутск
Казань
Sample Output 3:
OK
