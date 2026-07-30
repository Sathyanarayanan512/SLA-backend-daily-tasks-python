n=int(input("Enter rows: "))
for i in range(n):
    for j in range(n):
        if i+j==n//2 or i-j==n//2 or j-i==n//2 or i+j==(n//2)+(n-1):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
