login_function=lambda username,password:"Login Successful" if username=="SathyaB" and password==9999999999 else "Invalid Username or Password"
user=input("Enter username: ")
pwd=int(input("Enter password: "))
print(login_function(user,pwd))

