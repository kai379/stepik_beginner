# Шифр Цезаря


def select_lang():
    print('Выберите язык')
    print('1) Английский - введите eng\n'
          '2) Русский - введите rus')
    language = input().lower()
    while language not in ('rus', 'eng'):
        print('Такого варианта нет. Введите корректное значение')
        print('1) Английский - введите eng\n'
              '2) Русский - введите rus')
        language = input().lower()
    return language


def choose_direction():
    print('Выберите направление: ')
    print('1) Шифрование - введите enс\n'
          '2) Дешифрование - введите dec')
    direction = input().lower()
    while direction not in ('enc', 'dec'):
        print('Такого варианта нет. Введите корректное значение')
        print('1) Шифрование - введите enс\n'
              '2) Дешифрование - введите dec')
        direction = input().lower()
    return direction


def choose_step():
    print('Выберите шаг сдвига (число от 1): ')
    step_p = input()
    while not step_p.isdigit():
        print('Такого варианта нет. Введите ЧИСЛО.')
        step_p = input()
    return int(step_p)


def shift(direction, language, step_sh):
    eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    text = input('Введите текст:\n')
    text_transform = ''

    # направление движения
    step_dir = None
    if direction == 'dec':
        step_dir = -step_sh
    elif direction == 'enc':
        step_dir = step_sh

    rot_n = None
    if language == 'eng':
        rot_n = 26
    elif language == 'rus':
        rot_n = 32

    for c in text:
        if not c.isalpha():
            text_transform += c
        elif c in eng_lower_alphabet:
            text_transform += eng_lower_alphabet[(eng_lower_alphabet.index(c) + step_dir) % rot_n]
        elif c in eng_upper_alphabet:
            text_transform += eng_upper_alphabet[(eng_upper_alphabet.index(c) + step_dir) % rot_n]
        elif c in rus_lower_alphabet:
            text_transform += rus_lower_alphabet[(rus_lower_alphabet.index(c) + step_dir) % rot_n]
        elif c in rus_upper_alphabet:
            text_transform += rus_upper_alphabet[(rus_upper_alphabet.index(c) + step_dir) % rot_n]
    return text_transform


process = True
while process:
    print('Программа в работе.')
    direc = choose_direction()
    lang = select_lang()
    step = choose_step()
    print(shift(direc, lang, step))

    print('----------------------------')
    print('Продолжить работу или выйти?\n'
          '1 - Продолжить\n'
          '2 - Выйти')
    answer = input()
    while answer not in ('1', '2'):
        print('Такого варианта нет. Введите корректное значение')
        print('1 - Продолжить\n'
              '2 - Выйти')
        answer = input()
    if answer == '2':
        process = False
