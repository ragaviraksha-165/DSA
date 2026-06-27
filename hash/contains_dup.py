arr=[2,6,3,1,4]
def contains_dup(arr):
    seen=set()
    for i in arr:
        if i in seen:
            return True
        seen.add(i)
    return False
print(contains_dup(arr))
