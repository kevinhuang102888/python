y=int(input('Please input Year:'))
m=int(input('Please input Month:'))
d=1
#________________萬曆年公式_________________
a=(14-m)//12
y1=y-a
m1=m+12*a-2
w=(d+y1+(y1//4)-(y1//100)+(y1//400)+(31*m1)//12)%7
#__________________________________________
print('Sun','Mon','Tue','Wed','Thu','Fri','Sat')#星期的標題
#判斷是幾月，並找出相對應的日子，再印出來
#先將所有字串接起來，在每28字元(一個數字報含空白是4個*7)為一列去分割
if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
	string='    '*(w)#第一排共有幾個空白
	x=1
	while x<32:
		new='%02d'%(x)+'  '
		string=string+new
		x=x+1 
	print(string[:28])
	print(string[28:56])
	print(string[56:84])
	print(string[84:112])
	print(string[112:140])
	print(string[140:])
if m==4 or m==6 or m==9 or m==11:
	string='    '*(w)
	x=1
	while x<31:
		while x<32:
			new='%02d'%(x)+'  '
			string=string+new
			x=x+1 
	print(string[:28])
	print(string[28:56])
	print(string[56:84])
	print(string[84:112])
	print(string[112:140])
	print(string[140:])
#判斷是否為閏年，才能知道2月是28天或29天	
if m==2:
	if ((y)%4==0 )and (y%100 !=0) or (y%400==0):
		string='    '*(w)
		x=1
		while x<30:
			new='%02d'%(x) +'  '
			string=string+new
			x=x+1 
		print(string[:28])
		print(string[28:56])
		print(string[56:84])
		print(string[84:112])
		print(string[112:140])
		print(string[140:])
	else:
		string='    '*(w)
		x=1
		while x<29:
			new='%02d  '% (x)
			string=string+new
			x=x+1 
		print(string[:28])
		print(string[28:56])
		print(string[56:84])
		print(string[84:112])
		print(string[112:140])
		print(string[140:])
