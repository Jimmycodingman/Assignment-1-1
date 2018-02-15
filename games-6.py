x=int(input("entre num of coin "))
t=1
while x<=0:
    print ("entre mun greater than 0")
    x=int (input())
while x>0:
    if t%2==1:
        p1=int(input("player one :"))
        for i in range (x):
            if p1==i*i:
                x=x-p1
                valid=True
                break
    else:
        p2=int(input("player two :"))
        for i in range (x):
            if p2==i*i:
               x=x-p2
               valid=True
               break
    if valid==True:
            print ("reminder",x)
            if x>0:
               t=t+1
            else:
               continue
    elif valid==False:
        print ("try again")
    valid=False
if t%2==1:
    print ("player one won")
else:
    print ("player two won")
               
               
