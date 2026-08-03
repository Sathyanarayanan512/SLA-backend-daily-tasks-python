list_data=[22,3,11,4,6,90]
for i in range(len(list_data)-1):
    for j in range(i+1, len(list_data)):
        if list_data[i]>list_data[j]:
            temp=list_data[i]
            list_data[i]=list_data[j]
            list_data[j]=temp
print(list_data)
