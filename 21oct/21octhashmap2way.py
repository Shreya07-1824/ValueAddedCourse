n1=1221
n2=2211
freq1=[0]*10

isAnagram=True

while(n1>0):
    lastDigit=n1%10
    freq1[lastDigit]+=1
    n1//=10

    while n2>0:
       lastDigit=n2%10
       freq1[lastDigit]-=1
       n2//=10

for i in freq1:
    if i!=0:
        isAnagram=False

if isAnagram:
    print("anagram")
else:
    print("not anagram")
        

    