# 28n + 30k + 31m = 365
N_MAX = (365 - (30 + 31)) // 28 + 1
K_MAX = (365 - (28 + 31)) // 30 + 1
M_MAX = (365 - (28 + 30)) // 31 + 1
for n in range(1, N_MAX):
    for k in range(1, K_MAX):
        for m in range(1, M_MAX):
            if 28 * n + 30 * k + 31 * m == 365:
                print(f"n = {n}, k = {k}, m = {m}")
