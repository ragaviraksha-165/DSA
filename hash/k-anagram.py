s1 = "aabc"
s2 = "abdd"
k = 2
count=uncount=0
ans1=sorted(s1)
ans2=sorted(s2)
print(ans1,ans2)
if len(ans1)==len(ans2):
    for i in ans1:
        if i in ans2:
            count+=1
            ans2.remove(i) #remove so it doesnt conside duplicate
        else:
            uncount+=1
else:
    print("not possible")
print("count=",count,"uncount=",uncount)
if count==k:
    print("True")
