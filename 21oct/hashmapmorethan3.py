n=12135213321
freq=[0]*10
arr=[]

while(n>0):
    lastdigit=n%10
    freq[lastdigit]+=1
    n//=10


for i in range(len(freq)):
    if freq[i]>=3:
        arr.append(i)

print(arr)