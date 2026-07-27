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
