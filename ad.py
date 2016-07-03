def is_p(n):
	return int(str(n)[::-1])==n
l=filter(is_p,range(1,1000))
print l