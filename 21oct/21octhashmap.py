n=12023568
freq=[0]*10

while(n>0):
    lastDigit=n%10
    freq[lastDigit]+=1
    n//=10

for i in range(len(freq)):
    if freq[i]==0:
        continue
    print(i,"=",freq[i])