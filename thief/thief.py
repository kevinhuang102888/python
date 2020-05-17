thief=1
while thief <=4:
    a=(thief!=1)
    b=(thief==3)
    c=(thief==4)
    d=(thief!=4)
    if a+b+c+d==3:
        break
    thief=thief+1
print("The true thief is ",thief)
