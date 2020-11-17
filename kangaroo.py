#sample input
x1 = 21
v1 = 6
x2 = 47
v2 = 3


def kangaroo(x1, v1, x2, v2):
	jumps = 0
	while True:
		if x1<x2 and v1<=v2:
			return 'NO'
			break
		elif x2<x1 and v1>=v2:
			return 'NO'
			break
		else:
			jumps += 1
			x1 += v1
			x2 += v2
			if x1 == x2:
				return 'YES'
				break
			else:
				continue


kangaroo(x1,v1,x2,v2)