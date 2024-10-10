# Накручиваем стоимость ответа ⬆️🌶️
# eng  eyopaxcETOPAHXCBM
# рус  еуорахсЕТОРАНХСВМ

text = input()
coin_first = 0
coin_second = 0
eng = 'eyopaxcETOPAHXCBM'
rus = 'еуорахсЕТОРАНХСВМ'

for ch in text:
    coin_first += ord(ch)

for ch in text:
    if ch in eng:
        coin_second += ord(rus[eng.find(ch)])
    else:
        coin_second += ord(ch)

print(f'Старая стоимость: {coin_first * 3}🐝\n'
      f'Новая стоимость: {coin_second * 3}🐝')
