#time complexity=o(n)

nums = [1,2,3,4]
def productExceptSelf(nums):

    n = len(nums)
    answer = [1] * n

    # Store left products
    left = 1
    for i in range(n):
        answer[i] = left
        left *= nums[i]

    # Multiply by right products
    right = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right
        right *= nums[i]

    return answer
print(productExceptSelf(nums))
