nums=[10,1,1,5,4]

def containsduplicate(nums):
    seen=set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False
print(containsduplicate(nums))
