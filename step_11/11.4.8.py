# Negatives, Zeros and Positives

n = int(input())
list_minus = []
list_zero = []
list_plus = []
for i in range(n):
    num_to_list = int(input())
    if num_to_list < 0:
        list_minus.append(num_to_list)
    elif num_to_list == 0:
        list_zero.append(num_to_list)
    else:
        list_plus. append(num_to_list)
print(*(list_minus + list_zero + list_plus), sep='\n')
