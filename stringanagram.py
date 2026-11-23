s1="silent"
s2="listen"

freq1={}
freq2={}

for ch in s1:
    if ch in freq1:
        freq1[ch]+=1
    else:
        freq1[ch]=1

for ch in s2:
    if ch in freq2:
        freq2[ch]+=1
    else:
        freq2[ch]=1

if freq1==freq2:
    print("strings are anagram")

else:
    print("not anagram")