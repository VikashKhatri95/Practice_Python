#Take three angles and find whether it can form a triangle or not

def CheckTriangle(angle1,angle2,angle3):
    if(angle1>0 and angle2>0 and angle3>0):
        if (angle1+angle2+angle3)==180:
            print("Can form Triangle")
        else:
            print("Sum of angles not equals 180, So cannot be a triangle")
    else:
        print("Since it requires all angles to be >0 So these angles cannot form triangle")
try:
    angle1=float(input("Enter First Angle"))
    angle2=float(input("Enter Second Angle"))
    angle3=float(input("Enter Third Angle"))
    CheckTriangle(angle1,angle2,angle3)
except ValueError:
    print("Enter Valid Angles")
