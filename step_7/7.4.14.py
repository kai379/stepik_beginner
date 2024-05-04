# Ведьмаку заплатите чеканной монетой
# Всем известно, что ведьмак способен одолеть любых чудовищ,
# однако его услуги обойдутся недешево. К тому же ведьмак не принимает купюры,
# он принимает только чеканные монеты. В мире ведьмака существуют монеты с номиналами 1,5,10,25.

payment = int(input())
count = 0
while payment >= 25:
    count += 1
    payment -= 25
while payment >= 10:
    count += 1
    payment -= 10
while payment >= 5:
    count += 1
    payment -= 5
while payment >= 1:
    count += 1
    payment -= 1
print(count)
