num=[1,2,3,4,4,4,5,5]
k=3
def countfreq(num,k):
    count={}
    for i in num:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    sorted_count=sorted(count.items(),key=lambda x:x[1],reverse=True)

    for i in range (k):
        print(sorted_count[i][0])
countfreq(num,k)
    
