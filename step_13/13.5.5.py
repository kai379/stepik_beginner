# Good password 🌶️
# Пароль является надежным если:
# его длина не менее 8 символов;
# он содержит как минимум одну заглавную букву (верхний регистр);
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# объявление функции
def is_password_good(password):
    has_A = False
    has_a = False
    has_num = False
    if len(password) > 7:
        for c in password:
            if c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                has_A = True
            if c in 'abcdefghijklmnopqrstuvwxyz':
                has_a = True
            if c in '0123456789':
                has_num = True
            if has_num and has_A and has_a:
                return True
    return False


# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))


# # stepik
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     flag1 = False
#     flag2 = False
#     flag3 = False
#     for c in password:
#         if c.isupper():
#             flag1 = True
#         elif c.islower():
#             flag2 = True
#         elif c.isdigit():
#             flag3 = True
#     return flag1 and flag2 and flag3
