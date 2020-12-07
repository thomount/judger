x = eval(input())
if x >= 90 and x <= 100:
	print('very good')
elif x >= 80 and x < 90:
	print('good')
elif x >= 60 and x < 80:
	print('standard')
elif x <= 60:
	print('come on')
else:
	print('overflow')