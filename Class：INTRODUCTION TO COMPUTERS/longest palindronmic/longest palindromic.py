string=input("Enter a string:")
possible=[]
n=len(string)
x=0
#方法:先固定第一個，由最後一個開始檢驗是否跟第一個數字相同，如果相同，則將節錄此字串並檢查
#是否是回文，檢驗完第一個為頭，就檢驗第二個，一樣由尾到頭檢查，依此類推。
while True:
    while True:
        if x==(n-1): #當檢驗的數字與固定的數差1時，跳出迴圈
            break
        elif string[x]==string[n-1]:#如果檢驗數字與固定數一樣，檢驗回文
            while True:
                newstring=string[x:n]
                if newstring==newstring[::-1]:#原本與倒過來是否相同，作為判斷迴圈依據
                    possible.append(newstring)#將符合迴圈的放入LIST結構
                    n=n-1
                    break
                else:
                    n=n-1
                    break
        elif string[x]!=string[n-1]: #如果檢驗數字與固定數不同，檢驗數往前一位
            n=n-1
    x=x+1 #固定數往前一位
    n=len(string)
    if x==n: #當檢查到string的最後一個字元(固定數與檢驗數都是最後一個)則跳出
        break
#________判斷最長的回文______________
i=1
t=len(possible)
if t==1: #如果只找到一個回文，則最長即是它
    print('Longest palindrome subtring is:',possible[0])
    print('Length is',len(possible[0]))
elif t==0:#如果都沒有回文，列出第一個
    print('Longest palindrome subtring is:',string[0])
    print('Length is 1')
else:#從找到的全部回文可能性中，找到最長的回文
    longest=possible[0]
    while True:
        if len(longest)<len(possible[i]):
            longest=possible[i]
        else:
            i=i+1
        if i==t:
            break
    print('Longest palindrome subtring is:',longest)
    print('Length is',len(longest))
