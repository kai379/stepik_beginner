# Змеиный регистр 🐍

# объявление функции
def convert_to_python_case(text):
    text_pc = text[0].lower()
    for i in range(1, len(text)):
        if text[i].isupper():
            text_pc += '_' + text[i].lower()
        else:
            text_pc += text[i]
    return text_pc


# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))
