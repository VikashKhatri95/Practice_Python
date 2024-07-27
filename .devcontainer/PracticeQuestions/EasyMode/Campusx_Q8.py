#Euclidean Distance between two points
#It is used to find the distance between two points 
#d=sqrt((x2-x1)^2+(y2-y1)^2)

def measuredistance(x1,x2,y1,y2):
    result=((x2-x1)**2+(y2-y1)**2)**0.5
    return result

x1=int(input("Enter x coordinate of first point"))
y1=int(input("Enter y coordinate of first point"))
x2=int(input("Enter x coordinate of second point"))
y2=int(input("Enter y coordinate of second point"))
res=measuredistance(x1,x2,y1,y2)
print(f"Distance between 2 points on the graph is: {res}")