import math
def move(x,y,step, angle=0):
	nx=x + step * math.cos(angle)
	ny=y - step * math.sin(angle)
	return nx, ny
r=move(input() ,input(),input(),math.pi/input())
print(r)