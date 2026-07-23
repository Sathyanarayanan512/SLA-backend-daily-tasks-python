limit=int(input("Enter the limit: "))   #10
for i in range(1, limit):
    if i%3==0:
        print(i*10, end=' ')
    else:
        print(i, end=' ')
