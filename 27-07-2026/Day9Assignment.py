'''
for i in range(1, 10):
    if i<= 5:
        print(i, end=' ')
    else:
        print(i-5, end=' ')
'''
'''
size=int(input("Enter the no. of numbers: " ))
i=1
first_done=False
if size%2==0:
    size+1
while(i>0):
    print(i, end=' ')
    if i<=size//2 and first_done==False:
        i+=1
    if i==(size//2)+1:
        print(i, end=' ')
        first_done=True
    if first_done==True:
        i-=1
print("\nEnd")
'''
i=1
first_done=False
while i>=1:
    print(i, end=' ')
    if i<=5 and first_done==False:
        i+=1
    if i==5:
        print(i, end=' ')
        first_done=True
    if first_done==True:
        i-=1
print("\nEnd")
