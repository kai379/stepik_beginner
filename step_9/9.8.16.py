# Порядок книг 📚🌶️

num = int(input()) - 1
book_1 = input()
book_2 = None
is_sorted = True

if num != 0:
    while num > 0:
        book_2 = input()
        if book_1[:book_1.find(' ')] > book_2[:book_2.find(' ')]:
            is_sorted = False
            break
        if book_1[:book_1.find(' ')] == book_2[:book_2.find(' ')] and book_1[book_1.find('«'):book_1.find('»')] > book_2[book_2.find('«'):book_2.find('»')]:
            is_sorted = False
            break
        book_1 = book_2
        num -= 1

if is_sorted:
    print('YES')
else:
    print('NO')
