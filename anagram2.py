s1="silent"
s2="listen"
anagram=True

freq1={}


for ch in s1:
    if ch in freq1:
        freq1[ch]+=1
    else:
        freq1[ch]=1
    

for ch in s2:
    if ch in freq1:
        freq1[ch]-=1
    else:
        freq1[ch]=1

for i in freq1:
    if freq1[i]!=0:
        anagram=False
        break

if anagram:
    print("is anagram")

else:
    print("not anagram")