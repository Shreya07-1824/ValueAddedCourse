n1=1221
n2=2213
freq1=[0]*10
freq2=[0]*10
isAnagram=False

while(n1>0):
    lastDigit=n1%10
    freq1[lastDigit]+=1
    n1//=10

    while n2>0:
       lastDigit=n2%10
       freq2[lastDigit]+=1
       n2//=10

# if freq1==freq2:       
#        isAnagram=True

if freq1==freq2:
    print("numbers are anagram")
else:
    print("numbers are not anagram")