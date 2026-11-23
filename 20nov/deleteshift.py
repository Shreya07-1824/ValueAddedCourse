arr=[10,20,30,40,50,60]
pos=2

for i in range(pos,len(arr)-1,1):
    arr[i]=arr[i+1]

arr[-1]=0
print(arr)