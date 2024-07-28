#Count number of dogs and hens
def Count(heads,legs):
    dogsCount=(legs/2)-heads
    hensCount=heads-dogsCount
    return dogsCount,hensCount

totalHeads=int(input("Enter Total Heads"))
totalLegs=int(input("Enter Total Legs"))
numOfDogs,numOfHens=Count(totalHeads,totalLegs)
print(f"Total number of Dogs are {numOfDogs} and number of Hens are {numOfHens}")
