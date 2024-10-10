# Самое тяжелое слово

word_test = None
word_max = input()
word_test_sum = 0
word_max_sum = 0

for ch in word_max:
    word_max_sum += ord(ch)

for i in range(3):
    word_test = input()
    for ch in word_test:
        word_test_sum += ord(ch)
    if word_test_sum > word_max_sum:
        word_max = word_test
        word_max_sum = word_test_sum
        word_test_sum = 0
    else:
        word_test_sum = 0
print(word_max)
