'''
# list
# matrix
nested_li=[[1,2,3],[4,5,6],[7,8,9]]
for i in nested_li:
    for j in i:
        print(j, end=' ')
    print()
row=int(input("Enter the row: "))
column=int(input("Enter the column: "))
print("The value at row ",row," and column ",column," is ",nested_li[row][column])
'''
'''
# tuple
# median
tup=(2,11,7,79,3,2,11,9,7,60)
tup_copy=list(tup[:])
for i in range(len(tup_copy)-1):
    for j in range(i+1,len(tup_copy)):
        if tup_copy[i]>tup_copy[j]:
            tup_copy[i],tup_copy[j]=tup_copy[j],tup_copy[i]
print(tup)
tup_copy=tuple(tup_copy)
print(tup_copy)
if len(tup_copy)%2!=0:
    print("Median: ",tup_copy[len(tup_copy)//2])
else:
    print("Median: ",(tup_copy[(len(tup_copy)//2)-1] + tup_copy[len(tup_copy)//2])/2)
'''
'''
# set
# unique pairs of sum
nums = [2,7,11,15,3,6,4]
target = 9
num_pairs=[]
for i in nums:
    for j in nums:
        if i==j:
            continue
        if i+j==target:
            pairs=[]
            if i<j:
                pairs.append(i)
                pairs.append(j)
            else:
                pairs.append(j)
                pairs.append(i)
            num_pairs.append(tuple(pairs))
print(num_pairs)
unique_pairs=set(num_pairs)
print(list(unique_pairs))
'''
# dictionary
# remove duplicate dictionaries
data = [{"id":1,"name":"Alice"},
        {"id":2,"name":"Bob"},
        {"id":1,"name":"Alice"},
        {"id":3,"name":"John"}]
data_lists=[]
for i in data:
    dictionary=[]
    for j in i:
        dictionary.append((j,i[j]))
    data_lists.append(tuple(dictionary))
print("With duplicataes: \n",data_lists)
print("Without duplicates: \n",set(data_lists))



            
