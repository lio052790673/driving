country = input('請問你是哪國人?')
age = input('請輸入你的年齡:')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('你可以考駕照')
	else :
		print('你不能考駕照')
		pass
elif country == '美國':
	if age >= 16:
		print('你可以考駕照')
	else :
		print('你不能考駕照')
		pass
else :
	print('無法判定')	
	pass