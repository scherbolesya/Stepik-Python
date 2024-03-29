# BEEGEEK 1 Online School
# When admitting new employees to the BEEGEEK online school, its director tests not only the candidate’s professional qualities, but also his memory.
# The candidate is shown briefly several different numbers and then the candidate must name them. 
# Moreover, it does not matter in what order he remembers them, and whether he repeats them or not, the main thing is that he must name all the numbers without adding extra ones.
# Write a program to determine whether a candidate passes a memory test.

# Онлайн-школа BEEGEEK 1
# При приёме новых сотрудников в онлайн-школу BEEGEEK её руководитель тестирует не только профессиональные качества кандидата, но и его память.
# Кандидату показывают ненадолго несколько различных чисел, а затем кандидат должен их назвать. 
# Причем неважно, в каком порядке он их вспоминает, и повторяется он или нет, главное он должен назвать все числа, не добавляя лишних.
# Напишите программу, определяющую, успешно ли прошел кандидат тестирование памяти.

set1 = {int(i) for i in input().split()}  #Онлайн-школа BEEGEEK 1
set2 = {int(i) for i in input().split()}
print('YES' if set2 == set1 else 'NO')

Sample Input 1:
8
9
Sample Output 1:
NO
Sample Input 2:
1 2 3 4 8 5
1 2 8 2 3 4 5 2
Sample Output 2:
YES
Sample Input 3:
14 64 34 34 34 34 87 100
100 14 64 34 100
Sample Output 3:
NO
