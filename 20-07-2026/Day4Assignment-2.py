marks=[]
for i in range(3):
    marks.append(int(input("Enter mark: ")))
sum=0
for i in marks:
    sum+=i
print("Average: ",sum/len(marks))
