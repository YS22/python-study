import math
def quadratic(a,b,c):
	if b**2-4*a*c<0:
		print('wujie')
	else :
				x1=(-b-math.sqrt(b**2-4*a*c))/2*a
				x2=(-b+math.sqrt(b**2-4*a*c))/2*a
				return x1,x2
l=quadratic(input(),input(),input())
print(l)
