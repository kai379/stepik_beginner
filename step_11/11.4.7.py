# Google search - 2 🌶️🌶️

lines_num = int(input())
# lines_num = 5
lines_list = []
# lines_list = ['Язык Python прекрасен', 'C# - отличный язык программирования', 'Stepik - отличная платформа', 'BEEGEEK FOREVER!', 'язык Python появился 20 февраля 1991']
for _ in range(lines_num):
    lines_list.append(input())


keywords_num = int(input())
# keywords_num = 2
# keywords_list = ['язык', 'python']
keywords_list = []
for _ in range(keywords_num):
    keywords_list.append(input())

list_01 = lines_list
list_02 = []
while keywords_num:
    for i in list_01:
        if keywords_list[0].lower() in i.lower():
            list_02.append(i)

    del keywords_list[0]
    list_01, list_02 = list_02, []
    keywords_num -= 1

for i in list_01:
    print(i)
