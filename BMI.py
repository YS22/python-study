h=1.75
w=80.5
BMI=80.5/1.75**2
print(BMI)
if BMI>32:
	print('yingzhongfeipang')
elif 28<BMI<32:
	print('feipang')
elif 25<BMI<28:
	print('guozhong')
elif 18.5<BMI<25:
	print('zhengchang')
elif BMI<18.5:
	print('guoqing')