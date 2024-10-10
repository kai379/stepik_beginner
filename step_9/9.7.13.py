# Сбой в системе ⚠️🌶️🌶️
# Hello, my name is [u-1061][u-1072][u-1082][u-1080]!
# Username: [u-1042][u-1072][u-1089][u-1103]; City: [u-1050][u-1072][u-1079][u-1072][u-1085][u-1100]

text = input()

while '[' in text:
    text = text[:text.find('[')] + chr(int(text[text.find('[') + 3:text.find(']')])) + text[text.find(']') + 1:]

print(text)
