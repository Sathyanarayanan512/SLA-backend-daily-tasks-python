sum=0
while True:
    digit=int(input("Enter a digit between 0 and 6: "))
    if digit==0:
        print("Stopped")
        break
    elif digit>0 and digit<=6:
        sum+=digit
    else:
        print("Digit can't be out of range (or) invalid input")
print("Score(sum): ", sum)
