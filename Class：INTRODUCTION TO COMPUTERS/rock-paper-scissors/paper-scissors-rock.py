#________________剪刀石頭布的結果_________________________
print('%-15s %-15s %-15s'%("Player A","Player B","Result"))
print('%-15s %-15s %-15s'%("Rock","Rock","Tie"))
print('%-15s %-15s %-15s'%("Rock","Paper","Player B"))
print('%-15s %-15s %-15s'%("Rock","Scissors","Player A"))
print('%-15s %-15s %-15s'%("Paper","Rock","Player A"))
print('%-15s %-15s %-15s'%("Paper","Paper","Tie"))
print('%-15s %-15s %-15s'%("Paper","Scissors","Player B"))
print('%-15s %-15s %-15s'%("Scissors","Rock","Player B"))
print('%-15s %-15s %-15s'%("Scissors","Paper","Player A"))
print('%-15s %-15s %-15s'%("Scissors","Scissors","Tie"))
print("-"*44)
while True:
#___________先排除輸入錯誤的因素_______________
	A=input('Player A? ')
	while A!='rock'and A!='scissors' and A!='paper': 
		if A=="bye":
			break
		print("Invalid input. Please enter again.")
		A=input('Player A? ')
	if A=="bye":
		print()
		break
	B=input('Player B? ')
	while B!='rock'and B!="paper" and B!="scissors":
		if B=="bye":
			break
		print("Invalid input. Please enter again.")
		B=input('Player B? ')
#______________________________________________
	if B=="bye":  #離開
		print()
		break	
        #討論A和B的結果
	if A=="rock":
		if B =="rock":
			print(A,B)
			print("outcome:",'Tie')
		elif B=='paper':
			print(A,B)
			print('outcome:','Player B win!')
		else:
			print(A,B)
			print('outcome:','Player A win!')
	elif A=="paper":
		if B =="rock":
			print(A,B)
			print("outcome:",'Player A Win!')
		elif B=='paper':
			print(A,B)
			print('outcome:','Tie')
		else:
			print(A,B)
			print('outcome:','Player B Win!')
	elif A=='scissors':
		if B =="rock":
			print(A,B)
			print("outcome:",'Player B Win!')
		elif B=='paper':
			print(A,B)
			print('outcome:','Player A Win!')
		else:
			print(A,B)
			print('outcome:','Tie') 
	if A=="bye" :  #離開
		break
	print()
