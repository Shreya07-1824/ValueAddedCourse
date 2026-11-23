n1=1221
n2=22113
anagram=True

freq=[0]*10
while(n1>0):
    l=n1%10
    freq[l]+=1
    n1=n1//10

while(n2>0):
    l=n2%10
    freq[l]-=1
    n2=n2//10

for i in freq:
    if i!=0:
        anagram=False

if anagram:
    print("anagram")
else:
    print("not anagram")