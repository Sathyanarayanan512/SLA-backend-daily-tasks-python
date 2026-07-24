number=int(input("Enter a number: "))
temp=number
s=0
while number>0:
    digit=number%10
    s=s*10+digit
    number//=10
print("Reversed : ", s)
if temp==s:
    print("The number is palindrome")
else:
    print("The number is not a palindrome")
