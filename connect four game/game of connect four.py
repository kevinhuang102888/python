#用迴圈建立7X6的list
def initial():
	x=[]
	s=['|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|']#建立一個"｜"與" "交叉的list,且奇數index是空格
	t=1
	while t<7:
		x.append(s[:])
		t=t+1
	return x
#將目前的空格狀況列印出來
def printtable():
	for n in range(0,6):
		print('+---+---+---+---+---+---+---+')
		print(" ".join(x[5-n]))
	print('+---+---+---+---+---+---+---+')
	print('  0   1   2   3   4   5   6  ')
#判斷player輸入是否正確，並且填入空格
def inputcorrect(playx,letter):
	while True:	
		if  playx.isnumeric(): #判斷玩家輸入是否為數字
			if int(playx) not in range(0,7): #判斷是否在(0,6)格裡，如果超出範圍，則要求重輸入
				print('Out of range,try again ,[0-6].')
			elif x[5][2*int(playx)+1] in ('X','O'): #是否放滿，則要求玩家放其他位置
				print('This column is full. Try anothor column')
			else:
				break
		else : #如果非數字，則要求重新輸入
			print('Invalid input, try again [0-6]')
		playx=input('Player %s >>' % (letter))
	h=0
	while h<6:
		if x[h][2*int(playx)+1] in ('X','O'):
			h=h+1
			continue
		else:
			x[h][2*int(playx)+1]=letter
			break
#判斷有沒有4個連續rows都相同letter
def row4(letter):
	lowcase=letter.lower()
	p=0
	l=1
	while p<2:
		while l<14:
			if x[p][l]==x[p+1][l]==x[p+2][l]==x[p+3][l]==letter:
				x[p][l]=lowcase
				x[p+1][l]=lowcase
				x[p+2][l]=lowcase
				x[p+3][l]=lowcase
				printtable()
				print('Winner : %s' % (letter))
				return 1
			l=l+2
		p=p+1
		l=1
	return 0
#判斷有沒有4個連續columns都相同letter
def column4(letter):
	lowcase=letter.lower()
	b=0
	m=1
	while b<6:
		while m<8:
			if x[b][m]==x[b][m+2]==x[b][m+4]==x[b][m+6]==letter:
				x[b][m]=lowcase
				x[b][m+2]=lowcase
				x[b][m+4]=lowcase
				x[b][m+6]=lowcase
				printtable()
				print('Winner : %s' % (letter))
				return 1
			m=m+2
		b=b+1
		m=1
	return 0
#判斷左下到右上是否都相同letter
def diagonal(letter):
	lowcase=letter.lower()
	k=0
	e=1
	while k<3:
		while e<4:
			if x[k][e]==x[k+1][e+2]==x[k+2][e+4]==x[k+3][e+6]==letter:
				x[k][e]=lowcase
				x[k+1][e+2]=lowcase
				x[k+2][e+4]=lowcase
				x[k+3][e+6]=lowcase
				printtable()
				print('Winner : %s'%(letter))
				return 1
			e=e+2
		k=k+1
		e=1
	return 0
#判斷左上到右下是否相同letter
def diagonal2(letter):
	lowcase=letter.lower()
	c=0
	v=13
	while c<3:
		while v>6:
			if x[c][v]==x[c+1][v-2]==x[c+2][v-4]==x[c+3][v-6]==letter:
				x[c][v]=lowcase
				x[c+1][v-2]=lowcase
				x[c+2][v-4]=lowcase
				x[c+3][v-6]=lowcase
				printtable()
				print('Winner : %s'%(letter))
				return 1
			v=v-2
		c=c+1
		v=13
	return 0
#判斷是否全部空格都填滿
def full():
	if x[5][1] in ('X','O') and x[5][3] in ('X','O') and x[5][5] in ('X','O') and x[5][7] in ('X','O') and x[5][9] in ('X','O') and x[5][11] in ('X','O') and x[5][13] in('X','O'):
		print('Draw')
		return 1
	else:
		return 0
#將前面4種判斷整合，如果有一個成立，則表示遊戲結束
def process(playx,letter):
	inputcorrect(playx,letter)
	printtable()
	T_F=[row4(letter),column4(letter),diagonal(letter),diagonal2(letter),full()]
	if 1 in T_F:
		return True
	return False

#遊戲開始
x=initial()
printtable()
while True:
	playx=input('Player X >>')
	letter1='X'
	final1=process(playx,letter1)
	if final1:
		break
	playo=input('Player O >>')
	letter2='O'
	final2=process(playo,letter2)
	if final2:
		break
