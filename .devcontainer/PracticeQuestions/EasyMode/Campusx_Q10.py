#Take CP and SP and tell whether it is a profit or loss
#Profit=SP-CP
#Loss=CP-SP

def checkProfitOrLoss(sp,cp):
    if(sp>cp):
        print(f"Profit of {(((sp-cp)*100)/cp):.2f}%")
    else:
        print(f"Loss of {(((cp-sp)*100)/cp):.2f}%")

sp=float(input("Enter Selling Price"))
cp=float(input("Enter Cost Price"))
checkProfitOrLoss(sp,cp)