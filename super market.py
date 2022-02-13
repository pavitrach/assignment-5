'''alm=300
cas=500
pent=150
wal=200
cho=100'''
alm=int(input("how many kgs of almonds: "))
cas=int(input("how many kgs of cashew: "))
pent=int(input("how many kgs of peanuts: "))
wal=int(input("how many packets of walnuts: "))
cho=int(input("how many packets of chocolates: "))
bill=(alm*300)+(cas*500)+(pent*150)+(wal*200)+(cho*100)
dis=0
tax=0
if bill>=5000:
    dis=bill*10/100
    tax=bill*10/100
elif bill>=3000:
    dis=bill*8/100
    tax=bill*10/100
    if bill>=2000:
        dis=bill*5/100
        tax=bill*18/100
    elif bill>=1000:
        dis=bill*3/100
        tax=bill*18/100
else :
    print("discount is not applied")
totalbill=bill-dis+tax
print("bill:",bill)
print("tax=",tax)
print("total bill:",totalbill)

    
