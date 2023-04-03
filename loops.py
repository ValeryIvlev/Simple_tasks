# Напиши программу, которая считывает натуральное число n и n чисел, каждое  на своей строчке,
# и выводит только те числа,  которые делятся на свой порядковый номер (нумерация начинается с 1).

n = int(input())
for i in range(n):
    a = int(input())
    if a % (i + 1) == 0:
        print(a)

# В государстве X запрещено n слов, за каждое из использование каждого из которых
# (вне зависимости от регистра) полагается штраф в k единиц местной валюты
# Напишите программу, которая посчитает штраф за использования строки s,
# в которой есть запрещенные слова.

# В первой строчке вводится число n
# Во второй строчке вводится число k
# На третьей строчке вводится строка s.
# На следующих n строчках вводится по одному запрещенному слову в  нижнем регистре


n, k = int(input()), int(input())
s = input().lower()
a = 0
line = str()
while True:
    try:
        line = input()
    except EOFError:
        break
    if line != '':
        a += s.count(line)
    else:
        break
print(a * k)