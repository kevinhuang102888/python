length=int(input('Input the total number of students(n>0) :'))
i=list(range(1,length+1))
#將三倍數的位置去除
while len(i)>2:
	h=len(i)#原來的字串
	s=3
	while (s) <=len(i):#先將三倍數的位置變成零
		i[s-1]=0
		s=s+3
	while i.count(0)>0:#移除0
		i.remove(0)
	#判斷原來字串的字數是否為三倍數，移動字串的尾巴
	if (h%3)==1:
		i=[i[-1]]+i[:-1]
	elif (h%3)==2:
		i=[i[-2]]+[i[-1]]+i[:-2]
	elif (h%3)==0:
		continue
print("The last ID is : %d" % i[1])
