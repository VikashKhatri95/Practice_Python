#Program to find the volume of a cylinder and cost when 1 litre of milk=40 rupees.
# Volume of Cylinder is pi*r*r*h

def calculateVolumeCylinder(radius,height):
    return (3.14*(radius**2))*height

radius=float(input("Enter Radius of the cylinder: "))
height=float(input("Enter height of the cylinder: "))
result=calculateVolumeCylinder(radius,height)
print(f"The volume os the cylinder is {(result):.2f} and the cost of the milk it can hold is {(result*40):.2f}")