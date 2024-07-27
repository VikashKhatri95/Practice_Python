def minAngleBetweeHourandMin(h, m):
    # Validate the input
    if h < 0 or m < 0 or h > 12 or m >= 60:
        return 'Wrong input'
    
    if h == 12:
        h = 0
    
    if m == 60:
        m = 0
        h += 1
    
    # Calculate the angles
    minute_angle = m * 6
    hour_angle = (h * 30) + (m * 0.5)
    
    # Find the difference between the two angles
    angle = abs(hour_angle - minute_angle)
    
    # Find the minimum angle
    if angle > 180:
        angle = 360 - angle
    
    return angle

hour = int(input("Enter Hour: "))
minute = int(input("Enter Minute: "))
result = minAngleBetweeHourandMin(hour, minute)
print(f"Minimum Angle is {result}")
