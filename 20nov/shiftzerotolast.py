arr=[0,0,1,2,3]
j=0

for i in range(0,len(arr),1):
    if(arr[i]!=0):
        swap(arr[i],arr[j])
        j+1

