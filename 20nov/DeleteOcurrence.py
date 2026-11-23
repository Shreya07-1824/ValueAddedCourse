arr=[10,20,10,30,10,40]
j=0
x=10
for i in range(0,len(arr),1):
    if arr[i]!=x:
        arr[j]=arr[i]
        j+=1

for i in range(j,len(arr)):
    arr[i]=0
    j+=1

print(arr)
