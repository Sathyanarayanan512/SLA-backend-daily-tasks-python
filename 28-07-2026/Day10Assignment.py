rows=int(input("Enter the number of rows: "))+1
for i in range(1,rows):
    for j in range(1,i):
        print(" ", end=' ')
    for k in range(rows,i,-1):
        print("*", end=' ')
    print()
