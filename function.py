import math
def quadratic(a, b, c):
	deta=(b**2)-4*a*c
	S=math.sqrt(deta)
	root1=(-b+ S)/(2*a)
	root2=(-b-S)/(2*a)
	return root1,root2