# Стоимость ответа
# @кодер 666, пишите в комментариях по делу, не засоряйте чат бредом
# 164457🐝

text = input()
coin = 0

for ch in text:
    coin += ord(ch)

print(f"Текст сообщения: '{text}'\n"
      f"Стоимость сообщения: {coin * 3}🐝")
