arr=[200,201,202,6,3,1,4]
arr = sorted(set(arr))

count = 1
maximum = 1

for i in range(len(arr)-1):

    if arr[i] + 1 == arr[i+1]:
        count += 1
    else:
        maximum = max(maximum, count)
        count = 1

maximum = max(maximum, count)

print(maximum)
