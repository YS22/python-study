class Animal(object):
	def run(self,x,y):
		t=0
		t=x+y
		return t 
class Dog(Animal):
	pass
dog=Dog()
s=dog.run(1,3)
print s