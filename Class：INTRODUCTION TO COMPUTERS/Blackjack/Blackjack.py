import random
def begingame():
    shape=['spade']*13+['heart']*13+['diamond']*13+['club']*13
    figure=['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']*4
    a=[(figure[x],shape[x]) for x in range(0,52)]
    random.shuffle(a)
    return a
def totalvalue(b):
    from functools import reduce
    number=[b[x][0] for x in range(0,len(b))]
    new=[11 if x=='ace' else 10 if x=='jack' or x=='queen'or x=='king' else x for x in number]
    new2=[int(x) for x in new]
    if sum(new2)>21:
        if 11 in new2:
            total=sum(new2)
            i=0
            while i < new2.count(11):
                total = total -10 
                if total < 22:
                    return total
                i=i+1
            return total
        else:
            return sum(new2)
    else:
        return sum(new2)
def currentvalue(b,c):
    if c==0:
        if totalvalue(b)==21:
            print('Your current value is Blackjck!(21)')
        elif totalvalue(b)<21:
            print('Your current value is',totalvalue(b))
        else:
            print('Your value is Bust!(>21)')
            hand=[x+'-'+y for (x,y) in b]
            print('with the hand :',','.join(hand))
            print()
            print('*** Dealer wins ***')
            return None
    else:
        if totalvalue(b)==21:
            print('Dealer\'s current value is Blackjck!(21)')
        elif totalvalue(b) <21:
            print('Dealer\'s current value is',totalvalue(b))
        else:
            print('Dealer\'s current value is Bust!(>21)')
    hand=[x+'-'+y for (x,y) in b]
    print('with the hand :',','.join(hand))
def shuffle(a):
    b=[a.pop(),a.pop()]
    c=[a.pop(),a.pop()]
    return b,c
def Gamelogic(j,a,c):
    print()
    currentvalue(a,c)
    if j>21:
        return j
    else:
        if c==1:
            if j>17:
                return j
            while j<17:
                y=deck.pop()
                print()
                print('Dealer draws',y[0],"-",y[1])
                a.append(y)
                j=totalvalue(dealer)
            print()
            currentvalue(a,c)
            return j
        else:
            print()
            k=int(input('Hit or stay? (Hit=1 , Stay=0):'))
            if k==1:
                x=deck.pop()
                print('You draw',x[0],"-",x[1])
                a.append(x)
                j=totalvalue(a)
                return Gamelogic(j,a,c)
            if k==0:
                return j
def winner(a,b):
    print()
    if (a>b and a<22 and b<22) or(a<22 and b>21):
        print('*** You beat the dealer! ***')
    elif a<b  :
        print('*** Dealer wins ***')
    else:
        print('*** You tied the dealer ,nobody wins ***')
def again(q):
    print()
    q=input('Want to play again?(y/n):')
    if q=='y':
        return True
    else :
        return False
q=True
while q:
    deck=begingame()
    player,dealer=shuffle(deck)
    total1=totalvalue(player)
    total2=totalvalue(dealer)
    h=Gamelogic(total1,player,0)
    if h>21:
        q=again(q)
        continue
    n=Gamelogic(total2,dealer,1)
    winner(h,n)
    q=again(q)
