#time complexity=o(n^2)

arr = [1,2,3,4]

answer=[]

def productofarr(arr):
    for i in range (len(arr)):

        #product initially 1 and not 0
        product=1
        
        for j in range (len(arr)):
            
            #when not same index
            if i!=j:
                product*=arr[j]
                
        answer.append(product)
    print(answer)

productofarr(arr)
