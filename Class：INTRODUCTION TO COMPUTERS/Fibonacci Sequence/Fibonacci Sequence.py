n=int(input('input an integer number:'))
x0=0
x1=1
s=2
while s<=n:
	xn=x0+x1 #fibonacci sequence 的定義
	x0=x1
	x1=xn
	s=s+1
if n==1: #第一個fibonacci sequence number
	xn=1
if n==2: #第二個fibonacci sequence number
	xn=1
print('The %d-th Fibonacci sequence number is:'% (n),xn)
