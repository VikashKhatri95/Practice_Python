#Overlapping Rectangles
# Python program to check if rectangles overlap
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# Returns true if two rectangles(l1, r1) 
# and (l2, r2) overlap
def do_overlap(l1, r1, l2, r2):
	
	# if rectangle has area 0, no overlap
	if l1.x == r1.x or l1.y == r1.y or r2.x == l2.x or l2.y == r2.y:
		return False
	
	# If one rectangle is on left side of other
	if l1.x > r2.x or l2.x > r1.x:
		return False

	# If one rectangle is above other
	if r1.y > l2.y or r2.y > l1.y:
		return False

	return True

# Driver Code 
# L1=(0,2)
# R1=(1,1)
# L2=(-2,0)
# R2=(0,-3)
l1 = Point(0, 10)
r1 = Point(10, 0)
l2 = Point(5, 5)
r2 = Point(15, 0)

if(do_overlap(l1, r1, l2, r2)):
	print("Rectangles Overlap")
else:
	print("Rectangles Don't Overlap")

