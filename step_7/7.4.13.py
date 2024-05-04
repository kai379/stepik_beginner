# Количество пятерок

count = 0
grade = int(input())
while 6 > grade >= 0:
    if grade == 5:
        count += 1
    grade = int(input())
print(count)
