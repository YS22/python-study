class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s : %d - %s' %(self.name,self.score,self.get_grade()))
	def get_grade(self):
		if self.score>=90:
			return 'youliang'
		elif self.score>=60:
			return 'jige'
		else:
			return 'cha'
n1=Student('xiaoling',95)
n2=Student('xiaoyang',63)
n3=Student('vforbox ',50)
n1.print_score()
n2.print_score()
n3.print_score()