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

# Напиши программу, которая создаст список размером n*m , заполненный нулями,
# и выведет его в виде таблицы
# (между элементами таблицы в одной строке выводите пробел в качестве разделителя)
# На единственной строчке вводится 2 числа через пробел - n и m


n = input().split()
m = int(n[1])
x = int(n[0])
for _ in range(x):
    for _ in range(m):
        print(0, end=' ')
    print()

# Напишите программу, которая считывает целое число и выводит соответствующую ему римскую цифру.
# Если число находится вне диапазона 1-10, то программа должна вывести текст «ошибка».
# В таблице приведены римские цифры для чисел от 1 до 10.

l = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX","X"]
n = int(input())
if 1 <= n <= 10:
    for i in range(n):
        s = "Пасхалка))"
    print(l[i])
else:
    print("ошибка")