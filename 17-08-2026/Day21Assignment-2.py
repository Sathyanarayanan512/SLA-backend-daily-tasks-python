basic=int(input("Enter basic salary: "))
if basic<=20000:
    hra=20
    da=50
elif basic<=40000:
    hra=25
    da=60
else:
    hra=30
    da=70
gross=basic+((basic/100)*hra)+((basic/100)*da)
print("Gross salary: ",gross)
