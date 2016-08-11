L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]
def name(t):
	return t[0]
L2=sorted(L,key=name)
print(L2)