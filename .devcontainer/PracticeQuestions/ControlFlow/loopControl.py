#loop control
#break statement exits in loop permanently

for i in range(5):
    print(i)
    if i ==3:
        break
#continue skips the current iteration and continues with the next.
print()
for i in range(10):
    if i%2==0:
        continue
    print(i)

#pass statement is a null statement that does nothing
print()
for i in range(5):
    if(i==3):
        pass