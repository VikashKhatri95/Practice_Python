#Prime or not
def checkprime(num):
    if(num==1):
        print("Prime Number")
    else:
        i=c=1
        while(i*i<num+1):
            if(num//(i*i)==0):
                c=0
            else:
                c=1
            i=i+1
        if(c==1):
            print("prime")
        else:
            print("not prime")
    
num=int(input("Enter a number to check for prime: "))
checkprime(num)
    