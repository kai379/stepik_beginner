SIZE = 10


def func(a, b, c):
	x = a + b
	print(locals())
	z = x + c
	return z


func(1, 2, 3)
