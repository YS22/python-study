from functools import reduce
def str2float(s):
	s1,s2=s.split('.')
	return(float(reduce(lambda x,y:x*10+y,map(char2num,s1+s2))))/pow(10,s.rindex('.'))
def char2num(s):
	return{'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':0,'':0}[s]
print 'str2float(\'123.456\')=',str2float('123.456')