# Сортируем слова

letter01, letter02, letter03 = input(), input(), input()
letter_min = min(letter01, letter02, letter03)
letter_max = max(letter01, letter02, letter03)
letter_avg = letter01 + letter02 + letter03
letter_avg = letter_avg.replace(letter_min, '')
letter_avg = letter_avg.replace(letter_max, '')
print(letter_min, letter_avg, letter_max)
